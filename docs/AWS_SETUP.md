# AWS setup

## Prerequisites

Install:

- AWS CLI
- AWS SAM CLI
- Python 3.13

Configure AWS credentials:

```bash
aws configure
```

Verify:

```bash
aws sts get-caller-identity
```

## Bedrock

Enable access to a Converse-compatible model in the selected AWS Region.

The current template defaults to:

```text
amazon.nova-lite-v1:0
```

You can change `BedrockModelId` during guided deployment if required.

## Deploy

From the project root:

```bash
sam build
sam deploy --guided
```

Keep the resources in one AWS Region.

## Frontend configuration

After deployment, copy the `ApiUrl` CloudFormation output into the
frontend API configuration used by the application.

## Security and cost

- Keep the S3 bucket private.
- Do not commit AWS credentials.
- Upload URLs are intended to be short-lived.
- Textract and Bedrock can incur usage charges.
- Set an AWS Budget before testing.

## Troubleshooting

### Bedrock 403

Check:

- Model access
- AWS Region
- `BedrockModelId`

### CORS error

Confirm that the frontend API URL exactly matches the deployed API URL.

### Textract failure

Use a readable PDF. Password-protected or corrupt files are not supported
by the current documented flow.
