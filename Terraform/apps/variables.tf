variable "javascript_container_name" {
  description = "Name for the Docker container"
  type        = string
  default     = "moscow_tz_js"
}

variable "python_container_name" {
  description = "Name for the Python Docker container"
  type        = string
  default     = "moscow_tz"
}