
terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.109.0"
    }
  }
}
// Configure the Yandex.Cloud provider
provider "yandex" {
  token     = var.auth_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = var.compute_zone
}

resource "yandex_compute_disk" "boot-disk-1" {
  name = "boot-disk-1"
  type = "network-hdd"
  zone = var.compute_zone
  size = "60"
  # ubuntu 18.04 lts
  image_id = "fd8b1k66ee99rmt7p9ac"
}

// Create a new instance
resource "yandex_compute_instance" "vm1" {
  name        = "terraform-test"
  platform_id = "standard-v1"
  zone        = var.compute_zone

  resources {
    cores  = 4
    memory = 4
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.test_subnet.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

resource "yandex_vpc_network" "test_net" {
  name = "test_network"
}

resource "yandex_vpc_subnet" "test_subnet" {
  zone           = var.compute_zone
  network_id     = yandex_vpc_network.test_net.id
  v4_cidr_blocks = ["10.130.0.0/24"]
}
