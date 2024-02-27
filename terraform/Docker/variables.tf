variable "container_name" {
  description = "Name for the Docker container"
  type        = string
  default     = "my_container"
}

variable "image_name_and_tag" {
  description = "Name and tag for the Docker image"
  type        = string
  default     = "nginx:latest"
}


variable "internal_port" {
  description = "Internal port for the Docker container"
  type        = number
  default     = 80
}

variable "external_port" {
  description = "External port for the Docker container"
  type        = number
  default     = 8000
}