output "aws_instance_IP" {
  value = aws_instance.app_server.public_ip
}