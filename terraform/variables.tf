variable "docker_image" {
  description = "Docker image for the Flask app"
  default     = "almetovkamil/app_python:v1"
}

variable "container_name" {
  description = "Docker container name"
  default     = "app_python"
}
