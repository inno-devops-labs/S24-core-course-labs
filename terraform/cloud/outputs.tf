output "instance_public_ip" {
  description = "IP address for terraform"
  value       = aws_instance.app_server.public_ip
}

output "instance_id" {
  description = "ID of EC2"
  value       = aws_instance.app_server.id
}