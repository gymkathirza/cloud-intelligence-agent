resource "aws_dynamodb_table" "this" {
  name         = "${var.table_name}-${var.env}"
  billing_mode = "PAY_PER_REQUEST"

  hash_key = "ResourceId"
  # Range_key (Sort Key)
  range_key = "ResourceType"

  attribute {
    name = "ResourceId"
    type = "S"
  }

  attribute {
    name = "ResourceType"
    type = "S"
  }

  tags = {
    Environment = var.env
    Name        = var.table_name
  }
}