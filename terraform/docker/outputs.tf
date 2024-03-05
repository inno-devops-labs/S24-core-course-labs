output "container_id" {
  description = "Container ID"
  value       = docker_container.moscow-time.id
}

output "container_name" {
  description = "Container name"
  value       = docker_container.moscow-time.name
}