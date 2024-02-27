output "container_id" {
  description = "Docker container's ID"
  value       = docker_container.app_python.id
}

output "image_id" {
  description = "Docker image's ID"
  value       = docker_image.app_python.id
}

