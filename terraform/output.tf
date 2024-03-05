output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.my-python-app.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.my-python-app.id
}
