output "terraform_state_bucket" {
  description = "The name of the S3 bucket to use in your prod.config"
  value       = aws_s3_bucket.terraform_state.bucket
}

output "terraform_lock_table" {
  description = "The name of the DynamoDB table to use in your prod.config"
  value       = aws_dynamodb_table.terraform_locks.name
}