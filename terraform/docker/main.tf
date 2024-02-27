terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "dev-ops-course-app-python" {
  name  = var.container_name
  image = var.docker_image

  ports {
    internal = var.internal_port
    external = var.external_port
  }
}
