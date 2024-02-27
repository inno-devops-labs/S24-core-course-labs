variable "container_name" {
  description = "Docker container name"
  type        = string
  default     = "dev-ops-course-app-python"
}

variable "docker_image" {
  description = "Docker image"
  type        = string
  default     = "catdog905/dev-ops-course-app-python"
}

variable "internal_port" {
  description = "Internal port"
  type        = number
  default     = 80
}

variable "external_port" {
  description = "External port"
  type        = number
  default     = 80
} 
