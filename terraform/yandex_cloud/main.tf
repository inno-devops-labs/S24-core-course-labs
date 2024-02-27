terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone  = "ru-central1-a"
  token = var.token
}

resource "yandex_compute_disk" "boot-disk-1" {
  folder_id = var.folder_id
  image_id  = var.image_id
  name      = "boot-disk-1"
  type      = "network-hdd"
  zone      = "ru-central1-a"
  size      = "20"
}

resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"
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
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}

resource "yandex_vpc_network" "network-1" {
  folder_id = var.folder_id
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  folder_id      = var.folder_id
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}