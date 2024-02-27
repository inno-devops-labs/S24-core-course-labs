output "instance_id" {
  description = "ID of the Compute instance"
  value       = yandex_compute_instance.vm-1.id
}

output "instance_public_ip" {
  description = "Public IP address of the Compute instance"
  value       = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}
