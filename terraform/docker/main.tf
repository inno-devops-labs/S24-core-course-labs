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
  name         = "zaqbez39me/moscow-time-app:latest"
  keep_locally = true
}

resource "docker_container" "moscow-time-app" {
  image = docker_image.moscow-time-app.image_id
  name  = var.container_name
  ports {
    internal = 80
    external = 8000
  }
}