terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }

  }
}

provider "docker" {}

variable "container_name" {
  description = "Name for the app container"
  type        = string
  default     = "app_python"
}

resource "docker_image" "app_python" {
  name         = "mostafakira/app_python:latest"
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python.image_id
  name  = var.container_name

  ports {
    internal = 5000
    external = 5000
  }
}

output "container-id" {
  value = docker_container.app_python.id
}
