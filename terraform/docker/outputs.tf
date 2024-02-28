output "nginx_container_id" {
  value = docker_container.nginx.id
}

output "nginx_image_id" {
  value = docker_image.nginx.id
}

output "nginx_container_name" {
  value = var.container_name
}
