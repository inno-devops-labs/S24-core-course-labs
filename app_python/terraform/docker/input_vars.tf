variable "docker_username" {
  description = "Username for docker hub"
  type        = string
}

variable "docker_password" {
  description = "Password for docker hub"
  type        = string
}

variable "docker_container_name" {
  description = "Name of the container"
  type        = string
  default     = "sapushha_flask_app"
}

variable "docker_maintainer" {
  description = "Maintainer of the container"
  type        = string
}