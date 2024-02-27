terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}


provider "yandex" {
  zone      = "ru-central1-a"
  token     = var.token
  folder_id = var.folder-id
}

resource "yandex_vpc_network" "default" {
}

data "yandex_compute_image" "ubuntu-2204-lts" {
  family = "ubuntu-2204-lts"
}

resource "yandex_vpc_subnet" "subnet1" {
  name           = "subnet1"
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = "ru-central1-a"
  network_id     = "${yandex_vpc_network.default.id}"
}

resource "yandex_vpc_address" "vm1" {
  name = "terraform1"

  external_ipv4_address {
    zone_id = "ru-central1-a"
  }
}

resource "yandex_compute_instance" "moscow-time" {
  name = "moscow-time"
  zone = "ru-central1-a"

  resources {
    cores         = 2
    memory        = 4
    core_fraction = 100
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.ubuntu-2204-lts.image_id
    }
  }


  network_interface {
    subnet_id      = yandex_vpc_subnet.subnet1.id
    nat_ip_address = yandex_vpc_address.vm1.external_ipv4_address[0].address
    nat            = true
  }

}