resource "docker_image" "app_python" {
  name         = "wesamnaseer/mtz:v1.0"
  keep_locally = true
}

resource "docker_image" "app_javascript" {
  name         = "wesamnaseer/mtz_js:latest"
  keep_locally = true
}

resource "docker_container" "app_python" {
  name  = var.python_container_name
  image = docker_image.app_python.image_id
  ports {
    internal = 5000
    external = 8001
  }
}

resource "docker_container" "app_javascript" {
  name  = var.javascript_container_name
  image = docker_image.app_javascript.image_id
  ports {
    internal = 3000
    external = 8081
  }
}