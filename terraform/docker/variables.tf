variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "lab4"
}

variable "image_name" {
  description = "Value of the name for the Docker image"
  type        = string
  default     = "soralin/moscow-time-webapp"
}

