# Presentation outline

## Problem
Important information in notices is easy to miss: deadlines, eligibility requirements, attachments, and actions are buried in long PDFs.

## Solution
DocAction AI accepts a private PDF upload and returns an action-oriented summary rather than a generic document summary.

## Architecture
Browser → API Gateway → short-lived S3 upload URL → private S3 bucket → Textract → Bedrock → DynamoDB → Browser.

## Security
The bucket is private. The browser receives a URL valid for only five minutes and for one upload object. API Gateway is the only public application endpoint.

## Demo
Upload a scholarship or event notice, wait for analysis, and show the deadlines, eligibility, required documents, next steps, and warnings cards.
