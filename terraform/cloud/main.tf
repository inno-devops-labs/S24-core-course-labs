resource "yandex_compute_instance" "compute" {
  for_each = {
    for instance in local.instances : instance.name => instance
  }

  name = each.key
  resources {
    cores         = each.value.resources.core
    memory        = each.value.resources.memory
    core_fraction = each.value.resources.core_fraction
    gpus          = each.value.resources.gpus
  }
  boot_disk {
    device_name = each.value.boot_disk.device_name
    auto_delete = each.value.boot_disk.auto_delete
    mode        = each.value.boot_disk.mode
    disk_id     = each.value.boot_disk.disk_id
    initialize_params {
      image_id    = each.value.boot_disk.disk_id == null ? each.value.boot_disk.initialize_params.image_id != null ? each.value.boot_disk.initialize_params.image_id : var.default_disk_initialize_params.image_id : null
      size        = each.value.boot_disk.disk_id == null ? each.value.boot_disk.initialize_params.size != null ? each.value.boot_disk.initialize_params.size : var.default_disk_initialize_params.size : null
      name        = each.value.boot_disk.disk_id == null ? each.value.boot_disk.initialize_params.name != null ? each.value.boot_disk.initialize_params.name : var.default_disk_initialize_params.name : null
      description = each.value.boot_disk.disk_id == null ? each.value.boot_disk.initialize_params.description != null ? each.value.boot_disk.initialize_params.description : var.default_disk_initialize_params.description : null
      block_size  = each.value.boot_disk.disk_id == null ? each.value.boot_disk.initialize_params.block_size != null ? each.value.boot_disk.initialize_params.block_size : var.default_disk_initialize_params.block_size : null
      # type        = each.value.boot_disk.disk_id == null ? each.value.boot_disk.initialize_params.type != null ? each.value.boot_disk.initialize_params.type : var.default_disk_initialize_params.type : null
      type        = each.value.boot_disk.initialize_params.type != null ? each.value.boot_disk.initialize_params.type : var.default_disk_initialize_params.type
      snapshot_id = each.value.boot_disk.disk_id == null ? each.value.boot_disk.initialize_params.snapshot_id != null ? each.value.boot_disk.initialize_params.snapshot_id : var.default_disk_initialize_params.snapshot_id : null
    }
  }
  network_interface {
    subnet_id          = can(each.value.network_interface.subnet_id) ? each.value.network_interface.subnet_id : var.default_subnet_id
    ipv4               = each.value.network_interface.ipv4
    ip_address         = each.value.network_interface.ip_address
    ipv6               = each.value.network_interface.ipv6
    ipv6_address       = each.value.network_interface.ipv6_address
    nat                = each.value.network_interface.nat
    nat_ip_address     = each.value.network_interface.nat_ip_address
    security_group_ids = each.value.network_interface.security_group_ids
  }
  scheduling_policy {
    preemptible = each.value.scheduling_policy.preemptible
  }
  description               = each.value.description
  zone                      = each.value.zone
  platform_id               = each.value.platform_id
  metadata                  = each.value.metadata
  allow_stopping_for_update = each.value.allow_stopping_for_update
}
