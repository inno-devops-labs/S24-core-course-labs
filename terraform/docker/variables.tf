variable "container_name" {
  description = "Container Name"
  type        = string
  default     = "devops-moscow-app"
}

variable "container_image" {
  description = "Container image"
  type        = string
  default     = "exemplerie/devops-lab"
}

variable "int_port" {
  description = "Container internal port"
  type        = number
  default     = 5000
}

variable "ext_port" {
  description = "External port"
  type        = number
  default     = 8000
}