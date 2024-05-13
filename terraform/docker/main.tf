terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "moscow_time" {
  name         = var.container_name
  keep_locally = true
}

resource "docker_container" "my_container" {
  image = docker_image.moscow_time.image_id
  name  = var.container_name
  ports {
    internal = 8080
    external = 80
  }
}