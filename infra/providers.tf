terraform {
  backend "s3" {
    bucket         = "my-unique-tf-state-bucket"
    key            = "dev/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock" # Prevents two people from running it at once
  }
}

provider "aws" {
  region = "us-east-1"
}