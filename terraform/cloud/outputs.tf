output "instance_id" {
  description = "ID of the EC2 instance"
  value       = twc_server.my-timeweb-server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = twc_server.my-timeweb-server.main_ipv4
}
