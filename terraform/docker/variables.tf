variable "image" {
  description = "Value of image name"
  type    = string
  default = "arinazaza/app_python.py"
}

variable "container_name" {
  description = "Value of container name"
  type    = string
  default = "app_python"
}


variable "internal_port" {
  description = "Value of internal port"
  type    = number
  default = 8000
}

variable "external_port" {
  description = "Value of external port"
  type    = number
  default = 8000
}