terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host    = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "app_python_image" {
  name         = "sokolofff/app_python"
  keep_locally = false
}

resource "docker_container" "app_python_container" {
  image = docker_image.app_python_image.name
  name  = "app_python"

  ports {
    internal = 8080
    external = 8080
  }
}
