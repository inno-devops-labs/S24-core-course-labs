terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_image" "flask_app" {
  name          = "custom_app:latest"
  build {
    context    = "${path.module}/../../"
    dockerfile = "${path.module}/../../Dockerfile"
  }
}

resource "docker_container" "flask_app" {
  image = docker_image.flask_app.image_id
  name  = var.container_name
  ports {
    internal = 5000
    external = 5000
  }
}
