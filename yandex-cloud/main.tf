terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone  = "ru-central1-a"
  token = "t1.9euelZrMmMvPipTHnYnOl5fNipCNze3rnpWamJLNjZaKns6YkZmbkc_MlM3l8_dkTnVN-e9PHEBZ_d3z9yR9ck35708cQFn9zef1656VmsmUlc_Li4yRkZCakI-eyo-a7_zN5_XrnpWakcuelp6dnp7Micaans6expjv_cXrnpWayZSVz8uLjJGRkJqQj57Kj5o.MlmwLJJ1uHhavhItqYFf1LVPF9Ot5S52VSaQetzsI020i8ScEBI8zPmy4cxaJ3VWvJfudkm_U1kG3w614UCTAQ"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name      = "boot-disk-1"
  type      = "network-hdd"
  zone      = "ru-central1-a"
  size      = "15"
  image_id  = "fd8idq8k33m9hlj0huli"
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
  name      = "network1"
  folder_id = "b1gekjovb8e9ovoqiofd"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
  folder_id      = "b1gekjovb8e9ovoqiofd"
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}
