terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}


provider "docker" {}

resource "docker_image" "app_python_image" {
  name         = var.image
  keep_locally = false
}

resource "docker_container" "app_python_container" {
  image = docker_image.app_python_image.name
  name  = var.container_name

  ports {
    internal = var.internal_port
    external = var.external_port
  }
}