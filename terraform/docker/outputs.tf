output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.webapp_container.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.webapp_image.id
}

output "container_name" {
  description = "Name of the Docker container"
  value       = docker_container.webapp_container.name
}

output "image_name" {
  description = "Name of the Docker image"
  value       = docker_image.webapp_image.name
}
