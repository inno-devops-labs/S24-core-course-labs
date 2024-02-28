output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.dev-ops-labs.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.dev-ops-labs.id
}