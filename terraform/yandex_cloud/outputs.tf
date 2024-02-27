output "external_ip" {
  value = yandex_compute_instance.moscow-time.network_interface[0].nat_ip_address
}