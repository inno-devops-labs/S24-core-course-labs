terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "moscow_time_python" {
  name         = "n0m1nd/moscow_time_python:latest"
  keep_locally = true
}

resource "docker_container" "moscow_time_python" {
  name = var.container_name
  image = docker_image.moscow_time_python.image_id

  ports {
    external = 8080
    internal = 8080
  }
}
