output "container_name_python" {
  value = docker_container.custom_container_python.name
}

output "container_id_python" {
  value = docker_container.custom_container_python.id
}

output "container_image_python" {
  value = docker_container.custom_container_python.image
}

output "container_port_python" {
  value = docker_container.custom_container_python.ports
}

output "container_name_java" {
  value = docker_container.custom_container_java.name
}

output "container_id_java" {
  value = docker_container.custom_container_java.id
}

output "container_image_java" {
  value = docker_container.custom_container_java.image
}

output "container_port_java" {
  value = docker_container.custom_container_java.ports
}
