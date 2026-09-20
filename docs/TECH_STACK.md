# Technology Stack

## Frontend

The project includes a browser-based frontend.

Current repository assets include:

```text
frontend/
index.html
script.js
style.css
```

The frontend is responsible for:

- Selecting a document
- Requesting the upload flow
- Starting processing
- Polling/requesting the result
- Displaying the generated action-oriented information

## Backend

The backend is Python-based.

Main handlers:

```text
app.get_upload_url
app.start_document_processing
app.get_document_result
```

## AWS services

| Service | Responsibility |
|---|---|
| Amazon API Gateway | Public application API |
| AWS Lambda | Serverless backend execution |
| Amazon S3 | Private document storage |
| Amazon DynamoDB | Document/application state |
| Amazon Textract | PDF text detection |
| Amazon Bedrock | Generative AI processing |
| Amazon Nova Lite | Default configured Bedrock model |
| AWS IAM | Service permissions |
| AWS SAM / CloudFormation | Infrastructure as code |

## Infrastructure

The infrastructure is defined in:

```text
template.yaml
```

The SAM template configures:

- Python 3.13 Lambda runtime
- S3 bucket
- DynamoDB table
- API Gateway routes
- Lambda permissions
- Bedrock model parameter
- CloudFormation outputs

## Runtime configuration

The template defines:

```text
TABLE_NAME
BUCKET_NAME
BEDROCK_MODEL_ID
ALLOWED_ORIGIN
```

The default Bedrock model is:

```text
amazon.nova-lite-v1:0
```

## Security model

The document bucket is intended to remain private.

The upload flow uses short-lived S3 upload URLs rather than making the
bucket public.

IAM permissions are attached to the Lambda functions according to their
required operations.

## Why this stack?

The architecture uses managed AWS services so that document extraction,
storage, API routing, serverless execution, database state, and AI
processing can be composed without maintaining a traditional server.
