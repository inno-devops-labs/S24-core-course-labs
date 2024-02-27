variable "name_image" {
  description = "The image name"
  type        = string
  default     = "orillion1/lab2"
}

variable "tf_name" {
  description = "Name of container"
  type        = string
  default     = "webapp"
}

variable "port" {
  description = "The port of the container"
  type        = number
  default     = 8000
}