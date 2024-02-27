variable "provider_socket" {
  type = string
  description = "Socket for docker daemon"
}

variable "container_name" {
  type = string
  description = "Name for app_python container"
  default = "app_python"
}

variable "external_port" {
  type = number
  description = "Port for container to forward"
  default = 8080
}