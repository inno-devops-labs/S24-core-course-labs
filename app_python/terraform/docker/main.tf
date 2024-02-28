terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////./pipe/docker_engine"
}

resource "docker_image" "app_image" {
  name         = "${var.docker_username}/${var.docker_container_name}"
  keep_locally = false
  build {
    context = "..\\..\\"
  }
}

resource "docker_container" "app_container" {
  name  = var.docker_container_name
  image = docker_image.app_image.name
  labels {
    label = "maintainer"
    value = var.docker_maintainer
  }
  labels {
    label = "description"
    value = "Web Application that displays the current Moscow time"
  }

  working_dir = "/app_python"

  ports {
    internal = 8080
    external = 8080
  }

  command = [
    "python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8080"
  ]

  start = true
}

resource "docker_tag" "app_tag" {
  source_image = docker_image.app_image.name
  target_image = "${var.docker_username}/${var.docker_container_name}:latest"
}