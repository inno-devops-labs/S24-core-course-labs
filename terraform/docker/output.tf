output "container_id" {
  description = "Docker container ID"
  value       = docker_container.app_python.id
}

output "image_id" {
  description = "Docker image ID"
  value       = docker_image.app_python.id
}