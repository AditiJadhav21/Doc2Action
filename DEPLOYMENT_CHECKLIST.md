# Deployment checklist

- [ ] AWS CLI credentials work (`aws sts get-caller-identity`)
- [ ] Bedrock model access is enabled in the deployment Region
- [ ] `sam build` succeeds
- [ ] `sam deploy --guided` succeeds
- [ ] `ApiUrl` is copied into `frontend/script.js`
- [ ] A small PDF upload completes and displays an action plan
- [ ] AWS Budget alert is enabled

To remove all deployed AWS resources when finished, run `sam delete --stack-name YOUR_STACK_NAME`.
