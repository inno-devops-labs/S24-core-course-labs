output "container_id" {
  description = "Docker container"
  value = docker_container.nginx.id
}

output "image_id" {
  description = "Docker image"
  value = docker_image.nginx.id
}