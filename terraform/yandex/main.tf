terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.109.0"
    }
  }
  required_version = ">= 0.13"
}

// Configure the Yandex.Cloud provider
provider "yandex" {
  token = var.auth_token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
  zone      = var.compute_zone
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = var.compute_zone
  size     = "20"
  image_id = "fd8autg36kchufhej85b"
}


// Create a new instance
resource "yandex_compute_instance" "vm-1" {
  name = "terraform1"

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
  zone           = var.compute_zone
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["10.130.0.0/24"]
}
