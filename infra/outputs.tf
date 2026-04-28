output "database_name" {
  value = module.dynamodb_table.table_id
}

output "ecr_repository_url" {
  value = module.ecr.repository_url
}

output "security_group_id" {
  value = module.network.security_group_id
}

output "ecs_cluster_id" {
  value = module.ecs.cluster_id
}

output "ecs_service_name" {
  value = module.ecs.service_name
}

output "ecs_service_arn" {
  value = module.ecs.service_arn
}

output "ecs_task_definition_arn" {
  value = module.ecs.task_definition_arn
}
