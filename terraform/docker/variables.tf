variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "app_python_container"
}

variable "image_name" {
  description = "Value of the name for the Docker image"
  type        = string
  default     = "bulatok4/app_python"
}

variable "image_tag" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "latest"
}

variable "internal_port" {
  description = "Value of the internal port for the Docker container"
  type        = number
  default     = 8080
}

variable "external_port" {
  description = "Value of the external port for the Docker container"
  type        = number
  default     = 8080
}