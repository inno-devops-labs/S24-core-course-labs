variable "docker_registry_username" {
  description = "GitHub username for docker registry (docker hub)"
}

variable "docker_registry_password" {
  description = "GitHub password for docker registry (docker hub)"
}

variable "docker_container_name" {
  description = "Name of the container"
  default = "moscow_time_web_app"
}

variable "docker_maintainer" {
  description = "Maintainer of the container"
}