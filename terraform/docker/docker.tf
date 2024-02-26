terraform {
  required_version = ">= 0.13"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "app_python" {
  name         = "cogbonna/app_python_image:latest"
  keep_locally = true
}

resource "docker_image" "app_javascript" {
  name         = "cogbonna/app_javascript_image:latest"
  keep_locally = true
}

resource "docker_container" "app_python" {
  name  = var.python_container_name
  image = docker_image.app_python.image_id
  ports {
    internal = 5000
    external = 5000
  }
}

resource "docker_container" "app_javascript" {
  name  = var.javascript_container_name
  image = docker_image.app_javascript.image_id
  ports {
    internal = 3000
    external = 3000
  }
}