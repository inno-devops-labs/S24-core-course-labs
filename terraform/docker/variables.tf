variable "image_name" {
  type = string
  default = "nginx:latest"
}

variable "container_name" {
  type = string
  default = "timur_harin_lab4"
}

variable "container_port" {
  type    = number
  default = 8000
}

variable "host_port" {
  type    = number
  default = 8080
}
