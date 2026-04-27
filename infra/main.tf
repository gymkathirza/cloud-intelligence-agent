module "dynamodb_table" {
  source     = "./modules/dynamodb"
  table_name = var.app_table_name
  env        = var.environment
}