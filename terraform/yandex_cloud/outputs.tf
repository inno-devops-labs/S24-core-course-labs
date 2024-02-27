output "network_id" {
  description = "The ID of the created Yandex VPC Network"
  value       = yandex_vpc_network.network-1.id
}

output "subnet_id" {
  description = "The ID of the created Yandex VPC Subnet"
  value       = yandex_vpc_subnet.subnet-1.id
}