output "instance_ip" {
  description = "The public IP address of the devops-lab-machine instance"
  value       = yandex_compute_instance.devops-lab-machine.network_interface.0.ip_address
}

output "subnet_id" {
  description = "The ID of the subnet created for the devops-lab-machine instance"
  value       = yandex_vpc_subnet.subnet-devops-lab.id
}

output "instance_ssh_key" {
  description = "SSH key configured for accessing the devops-lab-machine instance"
  value       = yandex_compute_instance.devops-lab-machine.metadata["ssh-keys"]
}