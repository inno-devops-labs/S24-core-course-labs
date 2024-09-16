output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.devops-lab-python-app.id
}

output "container_name" {
  description = "Name of the Docker container"
  value       = docker_container.devops-lab-python-app.name
}