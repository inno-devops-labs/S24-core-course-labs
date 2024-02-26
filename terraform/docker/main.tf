terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "moscow-app" {
  name  = var.container_name
  image = var.container_image

  ports {
    internal = var.int_port
    external = var.ext_port
  }
}