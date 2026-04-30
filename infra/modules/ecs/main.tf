resource "aws_ecs_cluster" "this" {
  name = "${var.cluster_name}-${var.env}"
}

resource "aws_ecs_task_definition" "app" {
  family                   = "agentic-ai-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256" # Minimal for cost savings
  memory                   = "512"
  execution_role_arn       = var.execution_role_arn

  container_definitions = jsonencode([{
    name      = "agentic-ai-container"
    image     = "${var.repository_url}:latest"
    essential = true
    portMappings = [{
      containerPort = 8501 # Streamlit default port [7, 8]
      hostPort      = 8501
    }]
    environment = [
      { name = "GOOGLE_API_KEY", value = var.google_api_key },
      { name = "AWS_REGION", value = var.aws_region }
    ]
  }])
}

resource "aws_ecs_service" "this" {
  name            = "agentic-ai-service"
  cluster         = aws_ecs_cluster.this.id
  task_definition = aws_ecs_task_definition.app.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    subnets          = var.subnets
    assign_public_ip = true
    security_groups  = [var.security_group_id]
  }
}

resource "aws_iam_service_linked_role" "ecs" {
  aws_service_name = "ecs.amazonaws.com"
}