terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = var.zone
}

resource "yandex_compute_disk" "boot-disk-1" {
  name      = var.disk_name
  type      = var.disk_type
  zone      = var.zone
  size      = var.disk_size
  image_id  = var.image_id
  folder_id = var.folder_id
}

resource "yandex_compute_instance" "vm-1" {
  name = var.vm_name
  folder_id = var.folder_id

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = "windows_user:${file(var.metadata_ssh_keys_path)}"
  }
}

resource "yandex_vpc_network" "network-1" {
  name      = var.network_name
  folder_id = var.folder_id
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = var.subnet_name
  zone           = var.zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
  folder_id      = var.folder_id
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}
