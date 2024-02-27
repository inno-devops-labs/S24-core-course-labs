terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone  = var.zone
  token = var.service_token
}

resource "yandex_vpc_network" "default" {
  name      = var.network
  folder_id = "b1g8aian1v2o5fmf9tsh"
}

resource "yandex_vpc_subnet" "subnet-1" {
  network_id     = yandex_vpc_network.default.id
  name           = var.subnet
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = var.zone
  folder_id      = "b1g8aian1v2o5fmf9tsh"
}

resource "yandex_compute_image" "default" {
  source_family    = var.image_family
  folder_id = "b1g8aian1v2o5fmf9tsh"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name      = "boot-disk-1"
  type      = "network-hdd"
  size      = 8
  image_id  = "fd83s8u085j3mq231ago"
  folder_id = "b1g8aian1v2o5fmf9tsh"
}

data "template_file" "default" {
  template = file("${path.module}/init.ps1")
  vars = {
    user_name  = var.user_name
    user_pass  = var.user_pass
    admin_pass = var.admin_pass
  }
}

resource "yandex_compute_instance" "default" {
  name                      = var.vm_name
  platform_id               = "standard-v2"
  allow_stopping_for_update = true

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
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/inno_rsa.pub")}"
  }

  folder_id = "b1g8aian1v2o5fmf9tsh"
}

output "name" {
  value = yandex_compute_instance.default.name
}

output "address" {
  value = yandex_compute_instance.default.network_interface.0.nat_ip_address
}
