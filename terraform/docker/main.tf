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

resource "docker_image" "my_image" {
  name = "batdockerivankornienko/app_python"
}

resource "docker_container" "my_container" {
  image = docker_image.my_image.name
  name  = var.container_name
  ports {
    internal = 5000
    external = 8000
  }
}



