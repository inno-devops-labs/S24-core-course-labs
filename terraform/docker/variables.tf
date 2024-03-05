variable "container_name" {
  description = "Docker container name"
  type        = string
  default     = "time_web.py"
}

variable "docker_image" {
  description = "Docker image"
  type        = string
  default     = "snapman/time_web.py"
}

variable "internal_port" {
  description = "Internal port"
  type        = number
  default     = 80
}

variable "external_port" {
  description = "External port"
  type        = number
  default     = 8080
}