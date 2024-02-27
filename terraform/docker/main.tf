terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host ="unix:///Users/nikitagrigorenko/.docker/run/docker.sock"
}

resource "docker_image" "app_python" {
  name         = "${var.image_name}:${var.image_tag}"
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python.image_id
  name  = var.container_name

  ports {
    internal = 5000
    external = var.port
  }
}