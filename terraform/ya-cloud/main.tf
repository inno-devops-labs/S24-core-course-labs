resource "yandex_compute_disk" "drive" {
  zone     = "ru-central1-a"
  name     = "drive"
  type     = "network-hdd"
  size     = "21"
  image_id = "fd8t8vqitgjou20saanq"
}

resource "yandex_compute_instance" "virtual-machine" {
  name = "virtual-machine"
  zone = "ru-central1-a"

  boot_disk {
    disk_id = yandex_compute_disk.drive.id
  }

  resources {
    cores  = 2
    memory = 2
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.lab-subnet.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}

resource "yandex_vpc_network" "network-lab" {
  name = "network-lab"
}

resource "yandex_vpc_subnet" "lab-subnet" {
  name           = "lab-subnet"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-lab.id
  v4_cidr_blocks = ["192.168.50.0/24"]
}

terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone      = "ru-central1-a"
  token     = var.auth_token
  cloud_id  = var.ya-cloud-id
  folder_id = var.ya-folder-id
}