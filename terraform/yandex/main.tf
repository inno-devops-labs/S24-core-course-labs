terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone = var.zone
}

resource "yandex_compute_instance" "vm-1" {
  name = var.vm_name

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat       = var.nat
  }
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = var.zone
  size     = "10"
  image_id = var.image_id
}

resource "yandex_vpc_network" "default" {
  name = var.network_name
}

resource "yandex_vpc_subnet" "default" {
  name           = var.subnet_name
  zone           = var.zone
  network_id     = yandex_vpc_network.default.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}
