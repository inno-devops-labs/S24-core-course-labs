variable "docker_username" {
  description = "Username for DockerHub"
  type        = string
}

variable "docker_password" {
  description = "Password for DockerHub"
  type        = string
}

variable "docker_container_name" {
  description = "Name of the container"
  type        = string
  default     = "devops-flask-app"
}

variable "docker_maintainer" {
  description = "Maintainer of the container"
  type        = string
}