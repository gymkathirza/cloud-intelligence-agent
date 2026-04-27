provider "aws" {
  region = "us-east-1"
}

# 1. The S3 Bucket for Terraform State
resource "aws_s3_bucket" "terraform_state" {
  bucket        = "github-cia-unique-tf-state-bucket" # MUST BE GLOBALLY UNIQUE! Add random numbers.
  force_destroy = true # Ensures easy cleanup when the workshop is over
}

# Enable Versioning (Crucial for state history)
resource "aws_s3_bucket_versioning" "state_versioning" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}

# Enable Server-Side Encryption (Enterprise Standard)
resource "aws_s3_bucket_server_side_encryption_configuration" "state_encryption" {
  bucket = aws_s3_bucket.terraform_state.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# 2. The DynamoDB Table for State Locking
resource "aws_dynamodb_table" "terraform_locks" {
  name         = "github-cia-unique-terraform-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}