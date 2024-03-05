terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone                     = var.zone
  service_account_key_file = file("key.json")
  folder_id                = "b1gjtumbnfshl713ms12"
}

resource "yandex_vpc_network" "network" {}

resource "yandex_vpc_subnet" "subnetwork" {
  zone           = var.zone
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = ["10.228.0.0/24"]
}

resource "yandex_compute_instance" "default" {
  name        = "default"
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
      image_id = "fd80bm0rh4rkepi5ksdi" # ubuntu-2204-lts
    }
  }

  scheduling_policy {
    preemptible = true
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnetwork.id
    nat       = true
  }

  metadata = {
    user-data = file("user_data.yaml")
  }
}