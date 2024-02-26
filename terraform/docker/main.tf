terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "img" {
  name         = var.image
  keep_locally = false
}

resource "docker_container" "python_app" {
  image = docker_image.img.image_id
  name  = var.container_name
  rm    = true
  
  ports {
    internal = var.internal_port
    external = var.external_port
  }
}