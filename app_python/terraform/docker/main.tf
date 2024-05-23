terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "python-test-app_python" {
  name         = "rinri/python-test-app_python"
  keep_locally = false
}

resource "docker_container" "python-test-app_python" {
  image = docker_image.python-test-app_python.image_id
  name  = var.docker_container_name

  ports {
    internal = 8000
    external = 8000
  }
}
