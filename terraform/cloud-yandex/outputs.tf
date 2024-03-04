output "vm_ip" {
  description = "IP address of devops-moscow-app"
  value       = yandex_compute_instance.devops-vm.network_interface.0.ip_address
}

output "vm_ssh_key" {
  description = "SSH key for accessing the devops-moscow-app"
  value       = yandex_compute_instance.devops-vm.metadata["ssh-keys"]
}