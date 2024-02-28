variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "ExampleNginxContainer"
}

variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "image_id" {
  type    = string
  default = "fd87va5cc00gaq2f5qfb"
}

variable "folder_id" {
  type    = string
  default = "b1gnnf3j8bv1kfirnuq4"
}
