resource "aws_dynamodb_table" "this" {
  name           = "${var.table_name}-${var.env}"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Environment = var.env
    Name        = var.table_name
  }
}resource "aws_dynamodb_table" "this" {
  name           = "${var.table_name}-${var.env}"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"

  attribute {
    name = "id"
    type = "S"
  }

  tags = {
    Environment = var.env
    Name        = var.table_name
  }
}