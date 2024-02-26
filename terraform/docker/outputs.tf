output "container_id" {
  description = "Container ID"
  value       = docker_container.moscow-app.id
}

output "container_name" {
  description = "Container name"
  value       = docker_container.moscow-app.name
}