terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
    twc = {
      source = "tf.timeweb.cloud/timeweb-cloud/timeweb-cloud"
    }
  }
}

provider "docker" {}

resource "docker_image" "moscow-time-app" {
  name         = "zaqbez39me/moscow-time-app:latest"
  keep_locally = true
}

resource "docker_container" "moscow-time-app" {
  image = docker_image.moscow-time-app.image_id
  name  = var.container_name
  ports {
    internal = 80
    external = 8000
  }
}

output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.moscow-time-app.id
}

variable "container_name" {
  description = "Name for the deployed Docker container"
  type        = string
  default     = "moscow-time-app"
}