terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "webapp_image" {
  name         = var.image_name
  keep_locally = false
}

resource "docker_container" "webapp_container" {
  image = docker_image.webapp_image.image_id
  name  = var.container_name

  ports {
    internal = 5000
    external = 8000
  }
}
