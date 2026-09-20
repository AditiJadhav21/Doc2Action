# Project Guide

## What is Doc2Action?

Doc2Action is an AI-powered document assistant. It accepts a private PDF
and produces an action-oriented understanding of the document.

The current project is particularly suited to notices and documents where
users need to identify deadlines, eligibility, required documents, next
steps, and warnings.

## Core workflow

```text
1. Select PDF
2. Request upload URL
3. Upload to private S3
4. Start document processing
5. Textract extracts text
6. Retrieve processing result
7. Bedrock analyzes the extracted information
8. Display action-oriented result
```

## Main components

### Frontend

The frontend provides the document upload and result experience.

Relevant files include:

```text
frontend/
index.html
script.js
style.css
```

### Upload Lambda

Handler:

```text
app.get_upload_url
```

Purpose:

- Create the upload flow.
- Work with the private S3 bucket.
- Store document state in DynamoDB.

### Processing Lambda

Handler:

```text
app.start_document_processing
```

Purpose:

- Read the uploaded document from S3.
- Start Amazon Textract document text detection.
- Maintain document state.

### Result Lambda

Handler:

```text
app.get_document_result
```

Purpose:

- Retrieve Textract results.
- Invoke Amazon Bedrock.
- Return the processed document result to the application.

## API

| Method | Route | Purpose |
|---|---|---|
| POST | `/upload-url` | Create the upload flow |
| POST | `/process` | Start document processing |
| GET | `/result/{documentId}` | Retrieve the processed result |

## Important files

```text
template.yaml
    AWS SAM / CloudFormation infrastructure

app.py
    Python Lambda handlers

requirements.txt
    Python dependencies

frontend/
    Frontend application

docs/
    Project and deployment documentation

demo/
    Demo resources
```

## Development principle

Keep extraction and AI understanding separate.

```text
Textract = extract information
Bedrock  = understand and organize information
Frontend = present the result
```

This makes the architecture easier to debug and extend.
