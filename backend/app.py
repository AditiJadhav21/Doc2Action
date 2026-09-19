import json
import os
import re
import uuid
from datetime import datetime, timezone

import boto3

s3 = boto3.client("s3")
textract = boto3.client("textract")
bedrock = boto3.client("bedrock-runtime")
table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
BUCKET = os.environ["BUCKET_NAME"]
MODEL = os.environ["BEDROCK_MODEL_ID"]


def response(status, body):
    return {"statusCode": status, "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": os.getenv("ALLOWED_ORIGIN", "*"),
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    }, "body": json.dumps(body, default=str)}


def body(event):
    try:
        return json.loads(event.get("body") or "{}")
    except json.JSONDecodeError:
        return None


def get_upload_url(event, context):
    data = body(event)
    if data is None:
        return response(400, {"message": "Request body must be JSON."})
    name = os.path.basename(str(data.get("fileName", "")))
    content_type = data.get("contentType", "application/pdf")
    if not name.lower().endswith(".pdf") or content_type != "application/pdf":
        return response(400, {"message": "Only PDF files are accepted."})
    document_id = str(uuid.uuid4())
    key = f"uploads/{document_id}/{name}"
    upload_url = s3.generate_presigned_url("put_object", Params={
        "Bucket": BUCKET, "Key": key, "ContentType": "application/pdf"
    }, ExpiresIn=300)
    table.put_item(Item={"documentId": document_id, "fileName": name, "s3Key": key,
                         "status": "UPLOADED", "createdAt": datetime.now(timezone.utc).isoformat()})
    return response(200, {"documentId": document_id, "uploadUrl": upload_url})


def start_document_processing(event, context):
    data = body(event)
    document_id = (data or {}).get("documentId")
    if not document_id:
        return response(400, {"message": "documentId is required."})
    item = table.get_item(Key={"documentId": document_id}).get("Item")
    if not item:
        return response(404, {"message": "Document not found."})
    if item.get("status") not in ("UPLOADED", "FAILED"):
        return response(409, {"message": "This document is already being processed."})
    try:
        job = textract.start_document_text_detection(DocumentLocation={"S3Object": {"Bucket": BUCKET, "Name": item["s3Key"]}})
        table.update_item(Key={"documentId": document_id}, UpdateExpression="SET #s=:s, textractJobId=:j",
                          ExpressionAttributeNames={"#s": "status"},
                          ExpressionAttributeValues={":s": "PROCESSING", ":j": job["JobId"]})
        return response(202, {"documentId": document_id, "status": "PROCESSING"})
    except Exception as exc:
        return response(500, {"message": f"Could not start Textract: {str(exc)}"})


def textract_text(job_id):
    lines, token = [], None
    while True:
        args = {"JobId": job_id}
        if token:
            args["NextToken"] = token
        page = textract.get_document_text_detection(**args)
        job_status = page["JobStatus"]
        if job_status in ("IN_PROGRESS", "SUCCEEDED"):
            lines.extend(block["Text"] for block in page.get("Blocks", []) if block.get("BlockType") == "LINE")
        if job_status != "SUCCEEDED":
            return job_status, ""
        token = page.get("NextToken")
        if not token:
            return "SUCCEEDED", "\n".join(lines)


def analyse(text):
    prompt = """Extract practical information from this notice. Return ONLY valid JSON with this exact shape:
{"summary":"", "deadlines":[""], "eligibility":[""], "requiredDocuments":[""], "nextSteps":[""], "importantWarnings":[""]}.
Use empty arrays when the document has no answer. Do not invent facts. Keep each item concise. Notice text:\n""" + text[:45000]
    result = bedrock.converse(modelId=MODEL, messages=[{"role": "user", "content": [{"text": prompt}]}],
                              inferenceConfig={"maxTokens": 1500, "temperature": 0.1})
    answer = result["output"]["message"]["content"][0]["text"].strip()
    answer = re.sub(r"^```(?:json)?\s*|\s*```$", "", answer).strip()
    return json.loads(answer)


def get_document_result(event, context):
    document_id = event.get("pathParameters", {}).get("documentId")
    item = table.get_item(Key={"documentId": document_id}).get("Item")
    if not item:
        return response(404, {"message": "Document not found."})
    if item.get("status") == "COMPLETE":
        return response(200, {"documentId": document_id, "status": "COMPLETE", "result": item["result"]})
    if item.get("status") != "PROCESSING":
        return response(200, {"documentId": document_id, "status": item.get("status")})
    try:
        status, text = textract_text(item["textractJobId"])
        if status == "IN_PROGRESS":
            return response(200, {"documentId": document_id, "status": "PROCESSING"})
        if status != "SUCCEEDED":
            table.update_item(Key={"documentId": document_id}, UpdateExpression="SET #s=:s",
                              ExpressionAttributeNames={"#s": "status"}, ExpressionAttributeValues={":s": "FAILED"})
            return response(200, {"documentId": document_id, "status": "FAILED", "message": "Textract could not read this document."})
        result = analyse(text)
        table.update_item(Key={"documentId": document_id}, UpdateExpression="SET #s=:s, #r=:r",
                          ExpressionAttributeNames={"#s": "status", "#r": "result"},
                          ExpressionAttributeValues={":s": "COMPLETE", ":r": result})
        return response(200, {"documentId": document_id, "status": "COMPLETE", "result": result})
    except Exception as exc:
        return response(500, {"message": f"Analysis failed: {str(exc)}"})
