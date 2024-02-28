resource "docker_image" "default" {
  name         = "${var.docker_username}/${var.docker_container_name}"
  keep_locally = false

  build {
    context = "../../"
  }
}

resource "docker_container" "default" {
  name  = var.docker_container_name
  image = docker_image.default.name

  labels {
    label = "maintainer"
    value = var.docker_maintainer
  }

  labels {
    label = "description"
    value = "Flask Web Application displaying current time in Moscow"

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

resource "docker_tag" "default" {
  source_image = docker_image.default.name
  target_image = "${var.docker_username}/${var.docker_container_name}:latest"
}