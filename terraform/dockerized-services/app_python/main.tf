resource "docker_image" "app_python" {
  name         = "legolass322/devops:app_python"
  keep_locally = false
}

resource "docker_container" "app_python" {
  image = docker_image.app_python.image_id
  name  = var.container_name
  ports {
    internal = 8080
    external = var.external_port
  }
}