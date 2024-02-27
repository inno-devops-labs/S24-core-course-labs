output "compute_public_ips" {
  description = "Compute nat ipv4"
  value = flatten([for compute in yandex_compute_instance.compute[*] : 
    [for k, s in compute : {name = s.name, ip = s.network_interface.0.nat_ip_address} ]  
  ])
}