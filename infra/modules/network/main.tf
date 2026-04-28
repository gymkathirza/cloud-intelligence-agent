resource "aws_security_group" "app" {
  name        = "agentic-ai-sg-${var.env}"
  description = "Security group for agentic AI ECS service"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 8501
    to_port     = 8501
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
