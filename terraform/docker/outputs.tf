output "image_id" {
  description = "id of the docker image"
  value       = docker_image.nginx.id
}

output "container_id" {
  description = "id of the docker container"
  value       = docker_container.nginx.id
}
