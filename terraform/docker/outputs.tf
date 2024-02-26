output "container_id" {
  description = "Container ID"
  value       = docker_container.python_app.id
}

output "image_id" {
  description = "Container image"
  value       = docker_image.img.id
}