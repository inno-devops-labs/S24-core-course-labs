
output "public-ip-for-aws_instance" {
  value = aws_instance.application_server.public_ip
}
