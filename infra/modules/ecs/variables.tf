variable "env" {
  type = string
}

variable "cluster_name" {
  type = string
}

variable "repository_url" {
  type = string
}

variable "execution_role_arn" {
  type = string
}

variable "google_api_key" {
  type = string
}

variable "aws_region" {
  type = string
}

variable "subnets" {
  type = list(string)
}

variable "security_group_id" {
  type = string
}
