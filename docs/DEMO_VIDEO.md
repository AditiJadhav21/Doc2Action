# Demo Video Script

## Recommended length

Keep the demonstration short and focused on one complete document journey.

## Scene 1 — Problem

Show a long scholarship, event, academic, or notice PDF.

Narration:

> Important information in long documents is easy to miss. Deadlines,
> eligibility requirements, required documents, and next steps can be
> buried across several pages.

## Scene 2 — Solution

Open Doc2Action.

Narration:

> Doc2Action converts a complex document into an action-oriented result.
> Instead of only summarizing the document, it helps the user understand
> what matters and what needs to happen next.

## Scene 3 — Upload

Select a small, readable PDF.

Show the upload flow.

Explain:

- The browser requests a short-lived upload URL.
- The document is uploaded to a private S3 bucket.
- The public application endpoint is API Gateway.

## Scene 4 — AWS processing

Explain the pipeline:

```text
API Gateway
    ↓
Lambda
    ↓
Private S3
    ↓
Amazon Textract
    ↓
Amazon Bedrock / Nova Lite
    ↓
DynamoDB
```

## Scene 5 — Result

Show:

- Summary
- Deadlines
- Eligibility / required information
- Required documents
- Next steps
- Warnings, where available

## Scene 6 — Why it matters

Narration:

> The goal is not to replace the original document. The goal is to reduce
> the time needed to find the information that requires attention.

## Demo safety

Use a fictional or public document. Do not demonstrate with passwords,
API keys, private notices, personal identification numbers, or confidential
business documents.
