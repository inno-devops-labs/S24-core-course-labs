output "python-container-id" {
  value = docker_container.app_python.id
}

output "bun-container-id" {
  value = docker_container.app_bun.id
}

output "aws-public-ip" {
  value = aws_instance.app_server.public_ip
}