provider "docker" {
  registry_auth {
    address  = "registry-1.docker.io"
    username = var.docker_registry_username
    password = var.docker_registry_password
  }

  registry_auth {
    address  = "https://registry.hub.docker.com/v2/"
    username = var.docker_registry_username
    password = var.docker_registry_password
  }
}