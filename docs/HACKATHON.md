# Hackathon Criteria

## Problem and impact

Doc2Action addresses a common information-overload problem: important
deadlines, eligibility requirements, required documents, and actions can
be difficult to find in long PDF notices.

## Built on AWS

The application uses AWS managed services including:

- Amazon API Gateway
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon Textract
- Amazon Bedrock
- AWS IAM
- AWS SAM / CloudFormation

## AI integration

Amazon Textract provides document text extraction, while Amazon Bedrock
provides the generative AI layer used to turn extracted information into
an action-oriented result.

The configured default Bedrock model is `amazon.nova-lite-v1:0`.

## Technical execution

The project implements an end-to-end flow:

```text
PDF
 ↓
Short-lived upload URL
 ↓
Private S3
 ↓
Textract
 ↓
Bedrock
 ↓
Action-oriented result
```

## User value

The output is organized around practical questions:

- What is this document about?
- Which dates matter?
- What information or documents are required?
- What should I do next?
- Are there warnings or conditions I should notice?

## Evidence to include before submission

- Working application screenshot
- AWS architecture diagram
- Successful deployment evidence
- Example processed document
- Before/after or input/output screenshots
- Demo video link
- Team member names and contributions
