# Doc2Action AI / Agent Guide

## Purpose

Doc2Action is an AI-powered document assistant that turns complex PDF
documents into an action-oriented result: a concise summary, important
deadlines, required information, next steps, and warnings.

## Current architecture

```text
Browser
  ↓
API Gateway
  ↓
Short-lived S3 upload URL
  ↓
Private S3 bucket
  ↓
AWS Lambda
  ↓
Amazon Textract
  ↓
Amazon Bedrock / Amazon Nova Lite
  ↓
DynamoDB
  ↓
Browser
```

## Important implementation facts

- AWS infrastructure is defined in `template.yaml`.
- Runtime is Python 3.13.
- The default Bedrock model configured by the SAM template is
  `amazon.nova-lite-v1:0`.
- The main Lambda handlers are:
  - `app.get_upload_url`
  - `app.start_document_processing`
  - `app.get_document_result`
- API routes are:
  - `POST /upload-url`
  - `POST /process`
  - `GET /result/{documentId}`
- Uploaded documents are stored in a private S3 bucket.
- Upload URLs are short-lived and intended for one upload object.
- DynamoDB stores document/application state.
- Textract performs document text detection.
- Bedrock performs action-oriented understanding.

## Documentation rules

When changing the project:

1. Do not claim an AWS service is deployed unless it exists in
   `template.yaml` or has been verified in AWS.
2. Do not commit AWS access keys, secret keys, tokens, or private URLs.
3. Keep README and documentation consistent with the actual code.
4. Update deployment instructions when API routes or CloudFormation
   resources change.
5. Treat AI-generated deadlines and tasks as assistance; the original
   document remains the source of truth.
6. Use fictional/non-sensitive documents for demos.

## Validation

Before submitting changes:

```bash
sam build
sam deploy --guided
```

For an existing deployment, verify the API URL, upload flow, PDF
processing, Textract result, Bedrock response, and final action cards.
