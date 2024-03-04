output "js_app_external_port" {
  value = docker_container.app_javascript.ports.0.external
}

output "js_app_internal_port" {
  value = docker_container.app_javascript.ports.0.internal
}

output "python_app_external_port" {
  value = docker_container.app_python.ports.0.external
}

output "python_app_internal_port" {
  value = docker_container.app_python.ports.0.internal
}