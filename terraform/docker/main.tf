terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "devops-lab-python-app" {
  name  = var.container_name
  image = var.docker_image

  ports {
    internal = var.internal_port
    external = var.external_port
  }
}
