terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "devops-lab" {
  name  = var.container
  image = var.image

  ports {
    internal = var.internal
    external = var.external
  }
}