variable "python_container_name" {
  description = "Name for the Python Docker container"
  type        = string
  default     = "app_python"
}

variable "javascript_container_name" {
  description = "Name for the JavaScript Docker container"
  type        = string
  default     = "app_javascript"
}
