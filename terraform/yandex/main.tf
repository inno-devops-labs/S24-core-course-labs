terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}


provider "yandex" {
  zone  = var.zone
  folder_id = "b1g4gl2n8lipgh1t6sjh"
}

resource "yandex_compute_disk" "disk-1" {
  name     = "disk-1"
  type     = "network-hdd"
  zone     = var.zone
  size     = var.hdd_size
  image_id = var.image_id
}

resource "yandex_compute_instance" "vm-1" {
  name        = "vmvm"
  platform_id = "standard-v2"

  resources {
    cores         = 2
    core_fraction = 50
    memory        = 1
  }

  boot_disk {
    disk_id = yandex_compute_disk.disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = var.zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}