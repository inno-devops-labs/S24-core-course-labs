output "container_name" {
  description = "Container name:"
  value       = docker_container.app_python_container.name
}

output "container_id" {
  description = "Container ID:"
  value       = docker_container.app_python_container.id
}

output "image_id" {
  description = "Image ID:"
  value       = docker_image.app_python_image.id
}

output "image_name" {
  description = "Image name:"
  value       = docker_image.app_python_image.name
}