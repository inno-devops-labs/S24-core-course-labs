terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
}

provider "docker" {}

resource "docker_image" "devops" {
  name         = "ramprin/devops_py"
  keep_locally = false
}

resource "docker_container" "devops" {
  image = docker_image.devops.image_id
  name  = var.container_name

  ports {
    internal = 8080
    external = 80
  }
}

output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.devops.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.devops.id
}