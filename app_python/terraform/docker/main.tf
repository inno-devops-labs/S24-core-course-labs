terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
    host ="unix:///Users/ykozyrenko/.docker/run/docker.sock"
}

resource "docker_image" "nginx" {
  name         = "${var.name_image}:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = var.tf_name

  ports {
    internal = 5000
    external = var.port
  }
}