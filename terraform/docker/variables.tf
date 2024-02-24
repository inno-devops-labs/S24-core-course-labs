variable "image_name" {
  description = "The name of the image"
  type        = string
  default     = "fedorivn/simple-web-app"
}

variable "image_tag" {
  description = "The tag of the image"
  type        = string
  default     = "python-1.0.0"
}

variable "container_name" {
  description = "The name of the container"
  type        = string
  default     = "simple-web-app"
}

variable "port" {
  description = "The port of the container"
  type        = number
  default     = 8000
}
