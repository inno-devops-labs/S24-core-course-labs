terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {}

resource "docker_container" "custom_container_python" {
  image = var.docker_image_python
  name  = var.container_name_python
  ports {
    internal = var.internal_port_python
    external = var.external_port_python
  }
}

resource "docker_container" "custom_container_java" {
  image = var.docker_image_java
  name  = var.container_name_java
  ports {
    internal = var.internal_port_java
    external = var.external_port_java
  }
}
