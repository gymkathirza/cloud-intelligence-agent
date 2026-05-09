# cloud-intelligence-agent
Python-based CrewAI framework for autonomous cloud provisioning and optimization.

# 🤖 Agentic AI: Cloud Intelligence Assistant

This repository contains an enterprise-grade **Multi-Agent System** designed to act as a "Digital Employee" for autonomous cloud infrastructure audits [1, 2]. Utilizing **CrewAI** and **Gemini 1.5 Flash**, the assistant proactively scans cloud inventory, researches AWS best practices, and generates strategic cost-optimization reports [2-5].

---

## 🚀 Key Features
*   **Multi-Agent Reasoning:** Orchestrates a **Senior Data Researcher** to scan DynamoDB and a **Cloud Solutions Architect** to search the web for optimization strategies [3-5].
*   **Enterprise IaC:** Modular **Terraform** structure for fully automated, reproducible infrastructure [6-9].
*   **Secure CI/CD:** **GitHub Actions** integration using **OIDC (OpenID Connect)** for passwordless authentication to AWS [10, 11].
*   **Dual Deployment:** Accessible via **Streamlit Community Cloud** for public demoing and containerized on **AWS ECS Fargate** for production-grade serverless hosting [2, 9, 12, 13].

---

## 📂 Repository Structure
The project follows an enterprise separation of concerns between application and infrastructure logic [6, 8].

```text
├── .github/workflows/       # CI/CD pipelines (OIDC, Terraform, Docker) [8]
├── src/                     # APPLICATION LOGIC [8]
│   ├── crew_logic.py        # Multi-agent definitions and tasks [4, 5]
│   ├── tools.py             # DynamoDB and Web Search tool integrations [14, 15]
│   ├── ui.py                # Streamlit web interface [16-18]
│   └── Dockerfile           # Multi-stage build for Python and Terraform [17, 19]
├── infra/                   # INFRASTRUCTURE (IaC) [8]
│   ├── bootstrap/           # Remote state S3 & DynamoDB Lock setup [20, 21]
│   ├── envs/                # Environment-specific .tfvars (Dev/Prod) [8, 22, 23]
│   ├── modules/             # Reusable modules (ECR, ECS, DynamoDB) [8, 9]
│   └── main.tf              # Root orchestration "Glue" [8, 24]
└── README.md
```
--------------------------------------------------------------------------------
## 🛠️ Setup & Local Development
1. Environment Configuration
This project is optimized for GitHub Codespaces.
Add the following secrets to your repository settings:
GOOGLE_API_KEY: For Gemini 1.5 Flash.
AWS_REGION: e.g., us-east-1.
AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY: For local AWS connectivity.
AWS_ROLE_TO_ASSUME: The OIDC Role ARN for GitHub Actions.

3. Infrastructure Bootstrap
To maintain enterprise standards, you must first create a remote backend for Terraform state management.

cd infra/bootstrap
terraform init
terraform apply
Capture the S3 bucket name from the outputs and update your infra/providers.tf.

4. Local App Run
Install dependencies and trigger the agent reasoning loop manually:
pip install -r app/requirements.txt
python app/main.py

--------------------------------------------------------------------------------
## ☁️ Hosting & Deployment
AWS ECS Fargate (Manual/Professional)
The AWS deployment is managed via a Manual Workflow Dispatch to control costs while demonstrating serverless container orchestration.
Terraform: Builds a VPC across two AZs, a private ECR repository, and an ECS Fargate cluster.
GitHub Action: Builds the Docker image, pushes it to ECR, and forces a new deployment.
Access: The UI is available at http://<ECS_PUBLIC_IP>:8501.
Streamlit Community Cloud (Automated CI/CD)
Ideal for public portfolio demonstration with automated updates on every push to main.
Connect your GitHub repository to Streamlit Cloud.
Configure Secrets in TOML format within the Streamlit dashboard.
Live Link: https://cloud-intelligence-agent-xcitasoft.streamlit.app/.

--------------------------------------------------------------------------------
## 📊 Data Layer
Database: DynamoDB (Table: agentic-ai-data-prod).
Schema: Partition Key: ResourceId (S), Sort Key: ResourceType (S).
Data Seeding: The pipeline automatically populates mock data (EC2, RDS, S3 instances) using the AWS CLI for the agents to analyze.

--------------------------------------------------------------------------------
## 🛡️ Security Standards
OIDC: No long-lived AWS credentials stored in GitHub.
Least Privilege: Scoped IAM roles for ECS Task Execution and GitHub Actions.
State Encryption: Terraform remote state is encrypted at rest in S3 with DynamoDB-based state locking.
