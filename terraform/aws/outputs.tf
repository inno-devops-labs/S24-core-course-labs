output "ip-address" {
  value = aws_instance.instance.public_ip
}