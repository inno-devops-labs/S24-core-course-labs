terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_python" {
  name         = var.image_name
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python.image_id
  name  = var.container_name

  ports {
    internal = var.port
    external = var.port
  }
}

output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.app_python.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.app_python.id
}