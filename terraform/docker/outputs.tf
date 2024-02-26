output "python-container-id" {
  value = docker_container.app_python.id
}

output "javascript-container-id" {
  value = docker_container.app_javascript.id
}
