variable "container_name" {
  description = "Container name"
  type        = string
  default = "time-server"
}

variable "image_name" {
  description = "Image name"
  type        = string
  default     = "qexik1/flask-time-server"
}

variable "ports" {
  type = object({
    internal = number
    external = number
  })
  default = {
    internal = 5000
    external = 5000
  }
}
