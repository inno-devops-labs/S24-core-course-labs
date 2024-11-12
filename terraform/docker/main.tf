terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "flask-time-server" {
  name         = var.image_name
  keep_locally = false
}

resource "docker_container" "time-server" {
  image = docker_image.flask-time-server.image_id
  name  = var.container_name
  ports {
    internal = var.ports.internal
    external = var.ports.external
  }
}

output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.time-server
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.flask-time-server
}
