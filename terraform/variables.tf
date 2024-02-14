variable "python_container_name" {
  description = "Name for the python app container"
  type        = string
  default     = "python-app"
}

variable "bun_container_name" {
  description = ""
  type        = string
  default     = "bun-app"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-central-1"
}