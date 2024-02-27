output "IPAddress" {
  value = element(virtualbox_vm.vm1.*.network_adapter.0.ipv4_address, 1)
}