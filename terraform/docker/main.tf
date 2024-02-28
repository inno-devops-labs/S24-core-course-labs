terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "dev-ops-labs" {
  name         = "glebuben/dev-ops-labs:latest"
  keep_locally = false
}

resource "docker_container" "dev-ops-labs" {
  image = docker_image.dev-ops-labs.image_id
  name  = var.container_name
  ports {
    internal = 5000
    external = 5000
  }
}
