# Doc2Action

## AI Document to Action Assistant

Doc2Action is an AI-powered document processing application that converts important PDF documents into clear, action-oriented information.

Instead of providing only a general summary, the application focuses on identifying information that users may need to act on, such as deadlines, eligibility requirements, required documents, next steps, and warnings.

Built by **team CloudSmiths** for **Bharat Builds: First Commit**, a WeMakeDevs × AWS hackathon.
Team members
- Aditi Samadhan Jadhav
- Arya Ajit Jadhav
- Akshara Rajendra Gunjal

Repository: https://github.com/AditiJadhav21/Doc2Action
---

## Problem

Important information in notices, scholarship documents, event circulars, forms, and other PDFs is often buried inside long documents.

Users may need to manually search through the document to find:

* Important deadlines
* Eligibility requirements
* Required documents
* Instructions
* Next steps
* Important warnings

This makes it easy to miss information or misunderstand what needs to be done.

---

## Solution

Doc2Action processes a PDF document and converts its contents into an action-oriented response.

The basic workflow is:

```text
PDF
 ↓
Secure Upload
 ↓
Amazon Textract
 ↓
Amazon Bedrock
 ↓
Action-Oriented Result
 ↓
Frontend
```

The goal is to help users understand not only what a document says, but also what they may need to do next.

---

## Key Features

* PDF document upload
* Private document storage using Amazon S3
* Temporary upload URLs
* Text extraction using Amazon Textract
* AI-based document analysis using Amazon Bedrock
* Action-oriented document results
* Storage of document-related information using Amazon DynamoDB
* Serverless backend using AWS Lambda
* API-based communication using Amazon API Gateway
* Infrastructure deployment using AWS SAM

---

## Architecture

```text
User
  |
  v
Frontend
  |
  v
API Gateway
  |
  +--------------------+
  |                    |
  v                    v
Upload URL Lambda    Process Lambda
  |                    |
  v                    v
Private S3         Amazon Textract
                       |
                       v
                 Result Lambda
                       |
              +--------+--------+
              |                 |
              v                 v
         DynamoDB        Amazon Bedrock
              |                 |
              +--------+--------+
                       |
                       v
                   Frontend
```

---

## AWS Services

| Service         | Purpose                                           |
| --------------- | ------------------------------------------------- |
| Amazon S3       | Stores uploaded documents privately               |
| API Gateway     | Provides backend API endpoints                    |
| AWS Lambda      | Handles upload, processing, and result operations |
| Amazon Textract | Extracts text from PDF documents                  |
| Amazon Bedrock  | Analyzes extracted document content               |
| Amazon DynamoDB | Stores document-related information               |
| AWS IAM         | Controls access to AWS resources                  |
| AWS SAM         | Builds and deploys the application                |

The default Bedrock model configured in the project is:

```text
amazon.nova-lite-v1:0
```

The model can be changed using the `BedrockModelId` deployment parameter if required.

---

## Security

The application is designed to keep uploaded documents private.

The S3 bucket should not be made publicly accessible. Instead, the browser receives a temporary upload URL that is valid for five minutes.

The main application endpoints are exposed through API Gateway, while AWS services are accessed through Lambda functions with the required permissions.

---

## Project Structure

```text
Doc2Action/
│
├── Backend/
├── demo/
├── docs/
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── app.py
├── requirements.txt
├── template.yaml
│
├── AWS_SETUP.md
├── DEPLOYMENT_CHECKLIST.md
├── PRESENTATION.md
├── RUN_FIRST.txt
└── README.md
```

---

## Requirements

Before running the project, install:

* AWS CLI
* AWS SAM CLI
* Python
* An AWS account
* IAM credentials with permissions to create the resources defined in `template.yaml`

Configure AWS CLI:

```bash
aws configure
```

Verify the credentials:

```bash
aws sts get-caller-identity
```

---

## Amazon Bedrock Setup

Enable access to a compatible Amazon Bedrock model in the AWS Region being used for deployment.

The default model is:

```text
amazon.nova-lite-v1:0
```

If required, the model can be changed during:

```bash
sam deploy --guided
```

All AWS services should be deployed in the same Region.

---

## Deployment

From the project root, run:

```bash
sam build
```

Then deploy:

```bash
sam deploy --guided
```

After deployment, AWS provides an `ApiUrl` output.

Copy this URL into:

```text
frontend/script.js
```

and update the `API_URL` value.

---

## Frontend

The frontend consists of:

```text
frontend/index.html
frontend/style.css
frontend/script.js
```

For local testing, open:

```text
frontend/index.html
```

in a browser.

The frontend can also be hosted using Amazon S3 and CloudFront.

---

## Application Flow

1. User selects a PDF document.
2. Frontend requests a temporary upload URL.
3. The document is uploaded to the private S3 bucket.
4. The processing API starts document analysis.
5. Amazon Textract extracts text from the document.
6. Amazon Bedrock analyzes the extracted information.
7. The result is stored/retrieved using DynamoDB.
8. The frontend displays the action-oriented result.

---

## Example

A scholarship notice may contain several pages of information.

Doc2Action is designed to identify information such as:

```text
Deadline
Eligibility
Required Documents
Next Steps
Warnings
```

This allows the user to focus on the actions associated with the document instead of manually searching through every page.

---

## Demo

For a demonstration:

1. Deploy the AWS infrastructure.
2. Configure the `API_URL` in `frontend/script.js`.
3. Open the frontend.
4. Upload a small, readable PDF.
5. Wait for document processing.
6. Display the generated action-oriented result.

For public demonstrations, use only non-sensitive documents.

---

## Cost Considerations

Amazon Textract and Amazon Bedrock can incur AWS usage charges.

It is recommended to create an AWS Budget alert before testing the application.

Use small test documents during development and demonstrations.

---

## Troubleshooting

### Bedrock 403 Error

Check that:

* Bedrock model access is enabled.
* The selected Region is correct.
* The configured `BedrockModelId` is available in that Region.

### CORS Error

Make sure the `API_URL` in:

```text
frontend/script.js
```

exactly matches the `ApiUrl` generated during deployment.

Redeploy after making infrastructure changes.

### Textract Failure

Use a readable PDF.

Password-protected and corrupt PDF files are not supported by the documented workflow.

---

## Removing AWS Resources

After testing, deployed resources can be removed using:

```bash
sam delete --stack-name YOUR_STACK_NAME
```

Replace `YOUR_STACK_NAME` with the deployed SAM/CloudFormation stack name.

---

## Documentation

Additional documentation is available in:

* `AWS_SETUP.md` — AWS setup and deployment
* `DEPLOYMENT_CHECKLIST.md` — deployment checklist
* `PRESENTATION.md` — presentation outline
* `RUN_FIRST.txt` — quick-start instructions
* `template.yaml` — AWS infrastructure configuration

---

## Future Scope

Possible future improvements include:

* Support for additional document formats
* Deadline reminders
* Calendar integration
* Multi-language document processing
* Document history
* Improved accessibility
* More structured action categories
* Enhanced document analysis

---

## Hackathon

**Bharat Builds: First Commit**

A WeMakeDevs × AWS hackathon project focused on building a practical solution using AWS cloud technologies and AI.

---

## Team

Built by Team CloudSmiths for Bharat Builds: First Commit.
