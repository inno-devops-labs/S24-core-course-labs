output "python_container_id" {
  description = "Container ID"
  value       = docker_container.python-app.id
}

output "python_container_name" {
  description = "Container name"
  value       = docker_container.python-app.name
}

output "rust_container_id" {
  description = "Container ID"
  value       = docker_container.rust-app.id
}

output "rust_container_name" {
  description = "Container name"
  value       = docker_container.rust-app.name
}
