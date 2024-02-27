resource "docker_image" "app_python" {
  name         = "zeyadalagamy/moscow_tz:latest"
  keep_locally = true
}

resource "docker_image" "app_javascript" {
  name         = "zeyadalagamy/moscow_tz_js:latest"
  keep_locally = true
}

resource "docker_container" "app_python" {
  name  = var.python_container_name
  image = docker_image.app_python.image_id
  ports {
    internal = 8001
    external = 8001
  }
}

resource "docker_container" "app_javascript" {
  name  = var.javascript_container_name
  image = docker_image.app_javascript.image_id
  ports {
    internal = 8081
    external = 8081
  }
}