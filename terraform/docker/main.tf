terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "python-app" {
  name  = var.python_container_name
  image = var.python_container_image

  ports {
    internal = var.python_internal_port
    external = var.python_external_port
  }
}

resource "docker_container" "rust-app" {
  name  = var.rust_container_name
  image = var.rust_container_image

  ports {
    internal = var.rust_internal_port
    external = var.rust_external_port
  }
}
