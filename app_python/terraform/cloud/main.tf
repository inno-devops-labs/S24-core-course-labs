terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone = var.zone
  token = var.yandex_token
}

resource "yandex_vpc_network" "default" {
  name = "network1"
  folder_id = var.yandex_folder_id
}

resource "yandex_vpc_subnet" "default" {
  network_id     = yandex_vpc_network.default.id
  name           = "subnet1"
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = var.zone
  folder_id = var.yandex_folder_id
}

resource "yandex_compute_image" "default" {
  source_family  = "ubuntu-1804-lts"
  folder_id = var.yandex_folder_id
}

resource "yandex_compute_disk" "boot-disk" {
  name     = "boot-disk"
  type     = "network-nvme"
  zone     = var.zone
  size     = 50
  image_id = yandex_compute_image.default.id
  folder_id = var.yandex_folder_id
}

resource "yandex_compute_instance" "default" {
  zone     = var.zone

  resources {
    cores  = 2
    memory = 4
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat       = true
  }


  timeouts {
    create = "10m"
    delete = "10m"
  }
  folder_id = var.yandex_folder_id
}

output "name" {
  value = yandex_compute_instance.default.name
}

output "address" {
  value = yandex_compute_instance.default.network_interface.0.nat_ip_address
}