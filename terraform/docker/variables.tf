variable "container_name" {
  description = "Container Name"
  type        = string
  default     = "moscow-time"
}

variable "container_image" {
  description = "Container image"
  type        = string
  default     = "skylemn07/app"
}

variable "internal_port" {
  description = "Container internal port"
  type        = number
  default     = 5000
}

variable "external_port" {
  description = "External port"
  type        = number
  default     = 8000
}