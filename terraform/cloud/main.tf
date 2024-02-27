terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone = var.zone
  token = var.token
  folder_id = var.folder_id
}

resource "yandex_compute_disk" "boot-disk" {
  name     = "boot-disk"
  type     = var.disk_type
  zone     = var.zone
  size     = var.disk_size
  image_id = yandex_compute_image.default.id
}

resource "yandex_compute_image" "default" {
  source_family = "ubuntu-2204-lts"
}

resource "yandex_compute_instance" "vm" {
  name = "terraform1"
  zone = var.zone
  
  resources {
    cores  = var.cores
    memory = var.memory
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

resource "yandex_vpc_network" "yc-network" {
  name = "yc-network"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.yc-network.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}
