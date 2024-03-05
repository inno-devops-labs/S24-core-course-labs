variable "docker_image_name" {
  description = "The name of the Docker image"
  type        = string
  default     = "esadmazi/my-python-app:latest"
  sensitive   = true
}

variable "container_name" {
  description = "The name of the Docker container"
  type        = string
  default     = "my-python-app-container"
  sensitive   = true
}

variable "internal_port" {
  description = "The internal port your application listens on"
  type        = number
  default     = 5000
  sensitive   = true
}

variable "external_port" {
  description = "The external port to expose"
  type        = number
  default     = 8000
  sensitive   = true
}
