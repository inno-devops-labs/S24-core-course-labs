variable "internal_port" {
  description = "Internal port of the Docker containre"
  type        = number
  default     = 8000
}

variable "external_port" {
  description = "External port of the Docker container"
  type        = number
  default     = 8080
}
variable "container_name" {
  description = "Name of the Docker container"
  type        = string
  default     = "lab4"
}

variable "image_name" {
  description = "Name of the Docker image"
  type        = string
  default     = "smasiner2/python_time_app"
}