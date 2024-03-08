terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "my-python-app" {
  name         = var.docker_image_name
  keep_locally = false
}

resource "docker_container" "my-python-app" {
  image = docker_image.my-python-app.image_id
  name  = var.container_name
  ports {
    internal = var.internal_port
    external = var.external_port
  }
}

