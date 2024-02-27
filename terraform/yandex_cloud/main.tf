terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone = var.zone
  token = var.token
}

resource "yandex_vpc_network" "default" {
  name = var.network
  folder_id = var.folder_id
}

resource "yandex_vpc_subnet" "default" {
  network_id = yandex_vpc_network.default.id
  name = var.subnet
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone = var.zone
  folder_id = var.folder_id
}

resource "yandex_compute_image" "default" {
  source_family = var.image_family
  folder_id = var.folder_id
}

resource "yandex_compute_disk" "boot-disk" {
  name = "boot-disk"
  type = var.disk_type
  zone = var.zone
  size = var.disk_size
  image_id = yandex_compute_image.default.id
  folder_id = var.folder_id
}

resource "yandex_compute_instance" "vm-1" {
  zone = var.zone

  resources {
    cores = var.cores
    memory = var.memory
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/yandex_cloud.pub")}"
  }


  #metadata = {
  #  user-data = data.template_file.default.rendered
  #}

  timeouts {
    create = var.timeout_create
    delete = var.timeout_delete
  }
  
  folder_id = var.folder_id
}

