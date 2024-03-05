terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone  = var.zone
  folder_id = var.folder_id
}

resource "yandex_compute_disk" "disk" {
  name     = "disk"
  type     = var.disk_type
  zone     = var.zone
  size     = var.disk_hdd_size
  image_id = var.disk_image_id
}

resource "yandex_compute_instance" "vm" {
  name        = "vm"
  platform_id = var.vm_platfom_id

  resources {
    cores         = 2
    core_fraction = 5
    memory        = 1
  }

  boot_disk {
    disk_id = yandex_compute_disk.disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
}

resource "yandex_vpc_network" "network" {
  name = "network"
}

resource "yandex_vpc_subnet" "subnet" {
  name           = "subnet"
  zone           = var.zone
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = var.subnet_v4_cidr_blocks
}
