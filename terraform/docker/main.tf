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

variable "container_name" {
  description = "Name for the app container"
  type        = string
  default     = "app"
}

resource "docker_image" "nginx" {
  name         = "nginx"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = var.container_name

  ports {
    internal = 80
    external = 8000
  }
}
