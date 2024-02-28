variable "container_name" {
  description = "Container name variable"
  type        = string
  default     = "python-app"
}

variable "container_image" {
  description = "Container image variable"
  type        = string
  default     = "ghadeero/python-web-app:latest"
}

variable "internal_port" {
  description = "Internal port"
  type        = number
  default     = 5000
}

variable "external_port" {
  description = "External port"
  type        = number
  default     = 5000
}
