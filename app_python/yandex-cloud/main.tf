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
  token = "t1.9euelZrOk5XLyJXJkMadjpycnY2ak-3rnpWamJLNjZaKns6YkZmbkc_MlM3l8_cxOnpN-e9CbAtt_t3z93Fod03570JsC23-zef1656Vms6ajYnMj4-VlJiOx4mcmZXJ7_zN5_XrnpWajJvIzZWbx5bKicyTkY3Ji8rv_cXrnpWazpqNicyPj5WUmI7HiZyZlck.TwDzkVfKjLBGa2-DSBM8iuC4nBorPT4MparSbRA5wYROvU8Ad4ihrQcVnvDjLJecrvbUhsQ_EFLw5060tYXQBw"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = "fd8nhi2soipihuked9rf"
  folder_id = "b1gekjovb8e9ovoqiofd"
}

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
    ssh-keys = "ubuntu:${file("/home/yan/.ssh/id_ed25519.pub")}"
  }

  folder_id = "b1gekjovb8e9ovoqiofd"
}


resource "yandex_vpc_network" "network-1" {
  name = "network1"
  folder_id = "b1gekjovb8e9ovoqiofd"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
  folder_id = "b1gekjovb8e9ovoqiofd"
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}
