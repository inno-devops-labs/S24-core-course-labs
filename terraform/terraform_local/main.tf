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

resource "docker_image" "app-flask" {
  name         = "app-flask:latest"
  keep_locally = false
}

resource "docker_container" "flask" {
  image = docker_image.app-flask.image_id
  name  = var.container_name
  ports {
    internal = 5000
    external = 8000
  }
}
