output "python-container-id" {
  value = docker_container.app_python.id
}

output "bun-container-id" {
  value = docker_container.app_bun.id
}

output "aws-1-public-ip" {
  value = aws_instance.server_python.public_ip
}

output "aws-2-public-ip" {
  value = aws_instance.server_bun.public_ip
}