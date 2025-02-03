## Overview
This project demonstrates deploying a containerized web application using AWS ECS Fargate with CloudFormation and CI/CD.

## 📌 Deployment Steps
1. **Set up AWS CLI:** Ensure AWS CLI is installed and configured.
2. **Deploy Infrastructure:**
   ```sh
   aws cloudformation deploy --stack-name zayzoon-infra --template-file infra/cloudformation.yaml
   ```
3. **Push Docker Image to ECR:**
   ```sh
   docker build -t zayzoon-app .
   docker tag zayzoon-app 123456789012.dkr.ecr.us-west-1.amazonaws.com/zayzoon-app:latest
   docker push 123456789012.dkr.ecr.us-west-1.amazonaws.com/zayzoon-app:latest
   ```
4. **Update ECS Service:**
   ```sh
   aws ecs update-service --cluster ZayzoonCluster --service ZayzoonService --force-new-deployment
   ```

## Cleanup
To delete the resources:
```sh
aws cloudformation delete-stack --stack-name zayzoon-infra
```# ZayZoon-SRE-Exercise
