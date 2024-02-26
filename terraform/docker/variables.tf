variable "container_name" {
  description = "Docker container name"
  type        = string
  default     = "devops-app"
}

variable "docker_image" {
  description = "Docker image"
  type        = string
  default     = "blinikar/devops-app"
}

variable "internal_port" {
  description = "Internal port"
  type        = number
  default     = 5000
}

variable "external_port" {
  description = "External port"
  type        = number
  default     = 8080
}