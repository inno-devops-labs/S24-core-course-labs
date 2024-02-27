
output "container_id" {
  description = "Docker container ID"
  value       = docker_container.dev-ops-course-app-python.id
}

output "container_name" {
  description = "Docker container name"
  value       = docker_container.dev-ops-course-app-python.name
}
