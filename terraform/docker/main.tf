terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "image" {
  name         = var.image_name
  keep_locally = false
}

resource "docker_container" "container" {
  image = docker_image.image.image_id
  name  = var.container_name
  ports {
    internal = var.container_port
    external = var.host_port
  }
}
