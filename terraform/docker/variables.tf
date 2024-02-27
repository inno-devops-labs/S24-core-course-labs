variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "moscow-time-app"
}

variable "image_name" {
  description = "Value of the name for the Docker image"
  type        = string
  default     = "damirafliatonov/moscow-time-app:latest"
}

variable "internal_port" {
  description = "Value of the internal port"
  type        = number
  default     = 8000
}

variable "external_port" {
  description = "Value of the external port"
  type        = number
  default     = 8000
}
