terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host    = "npipe:////.//pipe//docker_engine"
}

resource "docker_container" "moscow-time" {
  name  = var.container_name
  image = var.container_image

  ports {
    internal = var.internal_port
    external = var.external_port
  }
}