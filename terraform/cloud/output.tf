output "availability_zone" {
  description = "Availability zone of server"
  value       = twc_server.example-server.availability_zone
}

output "location" {
  description = "Location of server"
  value       = twc_server.example-server.location
}