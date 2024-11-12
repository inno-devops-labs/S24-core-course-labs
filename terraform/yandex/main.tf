terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone = "ru-central1-a"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name = "boot-disk-1"
  type = "network-hdd"
  size = "10"
  image_id = "fd84kd8dcu6tmnhbeebv"
}

resource "yandex_compute_instance" "vm1" {
  name        = "terraform-time-server"
  platform_id = "standard-v1"
  resources {
    cores  = 2
    memory = 2
  }
  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.test_subnet.id
  }
  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

resource "yandex_vpc_network" "test_net" {
  name = "test_network"
}

resource "yandex_vpc_subnet" "test_subnet" {
  network_id     = yandex_vpc_network.test_net.id
  v4_cidr_blocks = ["10.130.0.0/24"]
}

