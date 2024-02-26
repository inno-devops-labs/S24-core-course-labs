output "container_id" {
  description = "Docker container ID"
  value       = docker_container.devops-app.id
}

output "container_name" {
  description = "Docker container name"
  value       = docker_container.devops-app.name
}