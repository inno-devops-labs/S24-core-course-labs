terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone      = var.zone
  token     = var.service_token
  folder_id = "b1gig8rbrvamd4b31tul"
}

resource "yandex_vpc_network" "networklab" {}

resource "yandex_vpc_subnet" "networklab" {
  zone           = var.zone
  network_id     = yandex_vpc_network.networklab.id
  v4_cidr_blocks = ["10.228.0.0/24"]
}

resource "yandex_vpc_address" "vm1" {
  name = "terraform1"

  external_ipv4_address {
    zone_id = var.zone
  }
}

data "yandex_compute_image" "ubuntu-2204-lts" {
  family = "ubuntu-2204-lts"
}

resource "yandex_compute_instance" "default" {
  name        = var.vm_name
  platform_id = "standard-v1"
  zone        = var.zone

  allow_stopping_for_update = true

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

  scheduling_policy {
    preemptible = true
  }

  network_interface {
    subnet_id      = yandex_vpc_subnet.networklab.id
    nat_ip_address = yandex_vpc_address.vm1.external_ipv4_address[0].address
    nat            = true
  }
}