variable "python_container_name" {
  description = "Name of the container"
  type        = string
  default     = "python-app"
}

variable "python_container_image" {
  description = "Image from which the container is built"
  type        = string
  default     = "ejedavid/app_python:latest"
}

variable "python_internal_port" {
  description = "Container internal port"
  type        = number
  default     = 8000
}

variable "python_external_port" {
  description = "External port"
  type        = number
  default     = 8080
}

variable "rust_container_name" {
  description = "Name of the container"
  type        = string
  default     = "rust-app"
}

variable "rust_container_image" {
  description = "Image from which the container is built"
  type        = string
  default     = "ejedavid/app_rust:latest"
}

variable "rust_internal_port" {
  description = "Container internal port"
  type        = number
  default     = 8000
}

variable "rust_external_port" {
  description = "Container External port"
  type        = number
  default     = 8081
}
