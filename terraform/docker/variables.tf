variable "image_name" {
  description = "The name of the image"
  type        = string
  default     = "nad777/anton_nekhaev_flask"
}

variable "container_name" {
  description = "The name of the container"
  type        = string
  default     = "anton_nekhaev_flask"
}

variable "port" {
  description = "The port of the container"
  type        = number
  default     = 5001
}