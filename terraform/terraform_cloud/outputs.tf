output "os_id" {
  description = "ID of the OS"
  value       = data.twc_os.os.id
}

output "config_id" {
  description = "ID of the configuration"
  value       = data.twc_configurator.configurator.id
}
