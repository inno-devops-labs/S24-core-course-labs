variable "container_name_python" {
  description = "Docker container name"
  type        = string
  default     = "app_python"
}

variable "docker_image_python" {
  description = "Docker image"
  type        = string
  default     = "dmfrpro/app_python"
}

variable "internal_port_python" {
  description = "Internal port"
  type        = number
  default     = 8080
}

variable "external_port_python" {
  description = "External port"
  type        = number
  default     = 8080
}

variable "container_name_java" {
  description = "Docker container name"
  type        = string
  default     = "app_java"
}

variable "docker_image_java" {
  description = "Docker image"
  type        = string
  default     = "dmfrpro/app_java"
}

variable "internal_port_java" {
  description = "Internal port"
  type        = number
  default     = 8000
}

variable "external_port_java" {
  description = "External port"
  type        = number
  default     = 8000
}
