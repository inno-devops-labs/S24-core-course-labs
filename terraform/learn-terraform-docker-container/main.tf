terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

#
provider "docker" {}

# https://developer.hashicorp.com/terraform/tutorials/docker-get-started/docker-build#terraform-block
# docker_ — provider name
# _image — resource name for the provider
resource "docker_image" "nginx" {
  name         = "nginx"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = var.container_name

  ports {
    internal = 80
    external = 8080
  }
}
