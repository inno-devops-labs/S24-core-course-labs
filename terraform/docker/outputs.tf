output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.app_python_container.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.app_python_image.id
}

output "container_name" {
  description = "Name of the Docker container"
  value       = docker_container.app_python_container.name
}

output "image_name" {
  description = "Name of the Docker image"
  value       = docker_image.app_python_image.name
}