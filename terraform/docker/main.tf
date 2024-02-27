terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "app_python" {
  name         = "yuszx/app_python:latest"
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python.name
  name  = var.container_name
  ports {
    internal = 5000
    external = 8080
  }
}
