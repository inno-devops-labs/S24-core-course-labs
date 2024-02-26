variable "image_name" {
  description = "The name of the image"
  type        = string
  default     = "nabuki/moscowtime-web"
}

variable "image_tag" {
  description = "The tag of the image"
  type        = string
  default     = "latest"
}

variable "container_name" {
  description = "The name of the cumtainer"
  type        = string
  default     = "moscowtime-web-app"
}

variable "container_port" {
  description = "The port of the container"
  type        = number
  default     = 8080
}

variable "host_port" {
  description = "The port to be occupied on the host"
  type        = number
  default     = 8000
}