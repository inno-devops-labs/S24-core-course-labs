provider "docker" {}

resource "docker_image" "app_python" {
  name         = "pptx704/app_python:latest"
  keep_locally = true
}

resource "docker_image" "app_bun" {
  name         = "pptx704/app_bun:latest"
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

resource "docker_container" "app_bun" {
  name  = var.bun_container_name
  image = docker_image.app_bun.image_id
  ports {
    internal = 3000
    external = 3000
  }
}