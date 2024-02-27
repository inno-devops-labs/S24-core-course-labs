output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.time_web.id
}

output "container_name" {
  description = "Name of the Docker container"
  value       = docker_container.time_web.name
}
