# AWS setup

1. Install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html), then run `aws configure` with an IAM user or role allowed to create the resources in `template.yaml`.
2. In Amazon Bedrock, request access to a Converse-compatible model in your selected Region. The template defaults to `amazon.nova-lite-v1:0`; change `BedrockModelId` during guided deployment if needed.
3. In a terminal at the project root run `sam build`, followed by `sam deploy --guided`. Choose a unique stack name and keep all services in one Region (for example `ap-south-1`).
4. When deployment completes, copy the `ApiUrl` output to the `API_URL` constant in `frontend/script.js`.
5. Open `frontend/index.html` locally for testing, or host the three frontend files using S3 + CloudFront.

## Required account considerations

Textract and Bedrock incur usage charges. Set an AWS Budget before testing. Do not make the generated S3 bucket public. The app creates private, five-minute upload URLs instead.

## Troubleshooting

- **403 from Bedrock:** model access is missing, the region is wrong, or `BedrockModelId` is unavailable there.
- **CORS error:** confirm that `API_URL` exactly matches the CloudFormation output; redeploy after changing the template.
- **Textract FAILED:** use a readable PDF. Password-protected or corrupt files are not supported.
