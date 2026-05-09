# General Environment Settings
environment = "production"
env         = "prod"

# DynamoDB Configuration
# Results in: agentic-ai-data-prod [4]
app_table_name = "agentic-ai-data-prod"

# AWS Provider Settings
aws_region = "us-east-1"

# NOTE: google_api_key is omitted here and injected via 
# GitHub Actions Secrets for enterprise-grade security.