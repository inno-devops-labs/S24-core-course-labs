resource "docker_registry_image" "app_registry_image" {
  name = "${var.docker_registry_username}/${var.docker_container_name}"
  keep_remotely = true
}

resource "docker_image" "app_image" {
  name         = "${var.docker_registry_username}/${var.docker_container_name}"
  keep_locally = false
  build {
    context    = "../../"
  }
}

resource "docker_container" "app_container" {
  name  = var.docker_container_name
  image = docker_image.app_image.name
  labels {
    label = "version"
    value = "1.0"
  }
  labels {
    label = "maintainer"
    value = var.docker_maintainer
  }
  labels {
    label = "description"
    value = "WebApp showing current Moscow time"
  }

  working_dir = "/app_python"

  ports {
    internal = 8080
    external = 8080
  }

  command = [
    "python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8080"
  ]

  start = true
}

resource "docker_tag" "app_tag" {
  source_image = docker_image.app_image.name
  target_image = "${var.docker_registry_username}/${var.docker_container_name}:latest"
}
