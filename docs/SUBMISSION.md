# Submission Checklist

Use this checklist before the final hackathon submission.

## Project

- [ ] Project name is consistent everywhere: Doc2Action
- [ ] GitHub repository is public
- [ ] README is complete
- [ ] Repository contains no credentials or secrets
- [ ] Repository structure is clean

## AWS

- [ ] AWS account/credentials are configured
- [ ] `sam build` succeeds
- [ ] `sam deploy --guided` succeeds
- [ ] Bedrock model access is enabled
- [ ] API Gateway URL is verified
- [ ] S3 bucket remains private
- [ ] DynamoDB table is created
- [ ] Textract processing works
- [ ] Bedrock invocation works
- [ ] AWS Budget alert is enabled

## Application

- [ ] PDF upload works
- [ ] Processing starts successfully
- [ ] Result endpoint returns data
- [ ] Summary is displayed
- [ ] Important deadlines are displayed
- [ ] Actionable tasks are displayed
- [ ] Error states are understandable
- [ ] Frontend uses the correct deployed API URL

## Demo

- [ ] Demo PDF is fictional/public/non-sensitive
- [ ] Complete upload-to-result flow is rehearsed
- [ ] AWS architecture is explained
- [ ] AI role is explained
- [ ] Demo video is recorded
- [ ] Final screenshots are added
- [ ] Presentation is ready

## Final evidence

Add the following before submission:

- Public repository URL
- Live application URL, if available
- API URL, if appropriate for the submission
- Demo video URL
- Team members and contributions
- AWS architecture screenshot
- Application screenshots
