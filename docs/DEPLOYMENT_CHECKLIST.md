# Deployment checklist

## AWS account

- [ ] AWS CLI credentials work:
  `aws sts get-caller-identity`
- [ ] Correct AWS Region selected
- [ ] Bedrock model access is enabled
- [ ] AWS Budget alert is enabled

## Build and deployment

- [ ] `sam build` succeeds
- [ ] `sam deploy --guided` succeeds
- [ ] CloudFormation stack reaches a successful state
- [ ] `ApiUrl` output is available
- [ ] `DocumentsBucketName` output is available

## Frontend

- [ ] Deployed API URL is copied into the frontend configuration
- [ ] Frontend loads without console errors
- [ ] Upload URL request succeeds

## End-to-end test

- [ ] Small readable PDF uploads successfully
- [ ] `/process` starts document processing
- [ ] Textract completes
- [ ] `/result/{documentId}` returns the result
- [ ] Bedrock analysis succeeds
- [ ] Summary is displayed
- [ ] Deadlines are displayed
- [ ] Actionable tasks are displayed

## Cleanup

When the deployment is no longer needed:

```bash
sam delete --stack-name YOUR_STACK_NAME
```
