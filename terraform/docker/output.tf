output "container_id" {
  value       = docker_container.app.id
}

output "image_id" {
  value       = docker_image.app.id
}