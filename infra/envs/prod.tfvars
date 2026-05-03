# General Environment Settings
environment = "production"
env         = "prod"

# DynamoDB Configuration
# Results in: agentic-ai-data-prod [4]
app_table_name = "agentic-ai-data-prod"

# AWS Provider Settings
aws_region = "us-east-1"

# IAM Security Roles
# Verified Account ID: 639679388423 [1]
# "arn:aws:iam::639679388423:role/ecsTaskExecutionRole"
ecs_execution_role_arn = aws_iam_role.ecs_task_execution_role.arn

# NOTE: google_api_key is omitted here and injected via 
# GitHub Actions Secrets for enterprise-grade security.