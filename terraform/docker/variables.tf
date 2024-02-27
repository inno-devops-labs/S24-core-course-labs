variable "image_name" {
  description = "Image name"
  type        = string
  default     = "dzendos/app_python"
}

variable "image_tag" {
  description = "Image tag"
  type        = string
  default     = "latest"
}

variable "container_name" {
  description = "Container name"
  type        = string
  default     = "app_python"
}

variable "port" {
  description = "Container port"
  type        = number
  default     = 8000
}