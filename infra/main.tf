module "dynamodb_table" {
  source     = "./modules/dynamodb"
  table_name = var.app_table_name
  env        = var.environment
}

module "ecr" {
  source          = "./modules/ecr"
  repository_name = "agentic-ai-app"
}

module "network" {
  source     = "./modules/network"
  env        = var.env
  aws_region = var.aws_region
}

module "ecs" {
  source             = "./modules/ecs"
  env                = var.env
  cluster_name       = "agentic-ai-cluster"
  repository_url     = module.ecr.repository_url
  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn
  google_api_key     = var.google_api_key
  aws_region         = var.aws_region
  subnets            = [module.network.public_subnet_1_id, module.network.public_subnet_2_id]
  security_group_id  = module.network.security_group_id
}