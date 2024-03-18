terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}
variable "folder_id" {
  description = "The ID of the Yandex.Cloud folder"
  type        = string
}

variable "token" {
  description = "The Token of the Yandex.Cloud"
  type        = string
}

// Configure the Yandex.Cloud provider
provider "yandex" {
  zone                     = "ru-central1-b"
  folder_id = var.folder_id
  token = var.token
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  size     = 8
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
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = "ru-central1-b"
}