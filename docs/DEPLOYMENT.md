# AWS Deployment Guide

## Prerequisites

Install:

- AWS CLI
- AWS SAM CLI
- Python 3.13
- An AWS account with permission to create the resources in `template.yaml`

Verify AWS credentials:

```bash
aws sts get-caller-identity
```

## 1. Configure Bedrock access

In the selected AWS Region, enable access to a Converse-compatible
Amazon Bedrock model.

The current template defaults to:

```text
amazon.nova-lite-v1:0
```

The model can be changed through the `BedrockModelId` SAM parameter.

## 2. Build

From the project root:

```bash
sam build
```

## 3. Deploy

Run:

```bash
sam deploy --guided
```

Choose a unique CloudFormation stack name and keep the application
resources in one AWS Region.

## 4. Configure the frontend

After deployment, copy the `ApiUrl` CloudFormation output into the
frontend API configuration used by the application.

The current setup documentation places the API URL in:

```text
frontend/script.js
```

## 5. Test

Use a small, readable PDF and verify:

1. Upload URL is generated.
2. Upload reaches S3.
3. Processing starts.
4. Textract completes.
5. Result endpoint returns the document result.
6. Bedrock analysis succeeds.
7. The browser displays the action-oriented result.

## 6. Cleanup

When the deployment is no longer needed:

```bash
sam delete --stack-name YOUR_STACK_NAME
```

## Cost and security notes

Textract and Bedrock can incur AWS usage charges. Set an AWS Budget before
testing.

Do not make the document bucket public. The intended design uses private
S3 storage and short-lived upload URLs.
