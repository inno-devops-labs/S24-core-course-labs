terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "moscow-time-app" {
  name         = var.image_name
  keep_locally = false
}

resource "docker_container" "moscow-time-app" {
  image = docker_image.moscow-time-app.image_id
  name  = var.container_name

  ports {
    internal = var.internal_port
    external = var.external_port
  }
}
