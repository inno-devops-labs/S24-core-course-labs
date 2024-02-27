terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token     = var.cloud_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
}

#Yandex vm config
resource "yandex_compute_instance" "vm-1" {
  name = "tarraform1"
  zone = "ru-central1-a"

  resources {
    cores  = 2
    memory = 2
  }
  
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }
  
  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  metadata = {
    ssh-keys = "ubuntu:${file("/root/.ssh/id_ed25519.pub")}"
  }
}

#Yandex disk for vm config
resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  zone     = "ru-central1-a"
  image_id = "fd8t8vqitgjou20saanq"
  size     = "20"
  type     = "network-hdd"
}

#Yandex subnet config
resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.0.0/24"]
}

#Yandex network config
resource "yandex_vpc_network" "network-1" {
  name = "network1"
}