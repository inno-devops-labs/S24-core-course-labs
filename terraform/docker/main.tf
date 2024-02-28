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

variable "container_name" {
  description = "New name for the Docker container"
  default     = "new_container_name"
}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
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

output "nginx_container_id" {
  value = docker_container.nginx.id
}

output "nginx_image_id" {
  value = docker_image.nginx.id
}

output "nginx_container_name" {
  value = var.container_name
}
