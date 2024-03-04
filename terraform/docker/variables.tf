variable "image_name" {
  type    = string
  default = "guzelzakirova/moscow-time-app:1.0.0"
}

variable "container_name" {
  type    = string
  default = "moscow-time-app"
}

variable "internal_port" {
  type    = number
  default = 8000
}

variable "external_port" {
  type    = number
  default = 8000
}