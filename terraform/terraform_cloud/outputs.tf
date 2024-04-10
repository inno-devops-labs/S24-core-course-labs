output "twc_os_id" {
  description = "ID of OS"
  value       = twc_server.my-timeweb-server.os_id
}

output "twc_configuration_id" {
  description = "Server provider"
  value       = twc_server.my-timeweb-server.configuration[0]
}