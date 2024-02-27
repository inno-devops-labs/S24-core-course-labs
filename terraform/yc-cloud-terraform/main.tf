terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
    zone = var.zone
    token = "t1.9euelZqenMjMz8bJy52dy53HjcfKme3rnpWax46UzZWTyceLjImcnZ3NmZrl8_dZKgZR-e8mPhJC_t3z9xlZA1H57yY-EkL-zef1656VmsiMypXLxsyakp7NiZ6QjY_M7_zN5_XrnpWayJWJnJaTmpybzZPGkcqSkcfv_cXrnpWayIzKlcvGzJqSns2JnpCNj8w.zULp_RmBpEF0C7CacuBaU_NphnAd5t1eGSe_7zHCiSmtE2tgZ4g4VgETzkmhY6ztdgTJ2wCf69cMMADYrdSiBQ"
}

resource "yandex_vpc_network" "default" {
    name = var.network
    folder_id = "b1g1g3o13qjhhu3gptpj"
}

resource "yandex_vpc_subnet" "default" {
    network_id = yandex_vpc_network.default.id
    name = var.subnet
    v4_cidr_blocks = ["192.168.10.0/24"]
    zone = var.zone
    folder_id = "b1g1g3o13qjhhu3gptpj"
}

resource "yandex_compute_image" "default" {
    source_family = var.image_family
    folder_id = "b1g1g3o13qjhhu3gptpj"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  size     = 8
  image_id = "fd83s8u085j3mq231ago"
  folder_id = "b1g1g3o13qjhhu3gptpj"
}

data "template_file" "default" {
    template = file("${path.module}/init.ps1")
    vars = {
        user_name = var.user_name
        user_pass = var.user_pass
        admin_pass = var.admin_pass
    }
}

resource "yandex_compute_instance" "vm-1" {
  name                      = "terraform1"
  platform_id               = "standard-v2"
  allow_stopping_for_update = true
  folder_id = "b1g1g3o13qjhhu3gptpj"
  resources {
    cores         = 2
    memory        = 1
    core_fraction = 5
  }

  scheduling_policy {
    preemptible = true
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat = var.nat
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}