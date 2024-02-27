variable "container_name" {
  description = "Container name"
  type        = string
  # you can use terraform.tfvars for the initialization
  default = "app_python"
}

variable "image_name" {
  description = "Image name"
  type        = string
  default     = "y4cerr/app_python"
}

variable "ports" {
  type = object({
    internal = number
    external = number
  })

  default = {
    internal = 8080
    external = 80
  }

}
