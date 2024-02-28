output "container_id" {
  value       = docker_container.container.id
  description = "Container ID of the nginx container"
}

output "image_id" {
  value       = docker_image.image.id
  description = "Image ID of the nginx image"
}