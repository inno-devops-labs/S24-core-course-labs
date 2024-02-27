variable "container_name" {
  description = "Name of Docker container"
  type        = string
  default     = "app_python"
}

variable "image_name" {
  description = "Name of Docker image"
  type        = string
  default     = "pgrammer/app_python"
}

variable "image_tag" {
  description = "Docker Image tag"
  type        = string
  default     = "latest"
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
