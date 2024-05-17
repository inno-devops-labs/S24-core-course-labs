variable "container_name" {
  description = "Container's name"
  type        = string
  default     = "application-weather"
}

variable "container_image" {
  description = "Image name"
  type        = string
  default     = "sharmatanmay617/devops-lab-2:latest"
}

variable "int_port" {
  description = "Internal Port"
  type        = number
  default     = 5000
}

variable "ext_port" {
  description = "External port"
  type        = number
  default     = 5000
}