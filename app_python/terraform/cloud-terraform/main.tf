terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone  = var.zone
  token = "t1.9euelZqWmJ2ckJ3Ozp3OyouUmY2Sk-3rnpWaysacnc_Gy5Ccy56Vz8qLkpLl8_cSfwZR-e8iRVVX_d3z91ItBFH57yJFVVf9zef1656Vmo2Rlp2Vl4uXzo3Hx5Gej5qe7_zN5_XrnpWajZaWkM2VkZ3KzpKTmMiMz53v_cXrnpWajZGWnZWXi5fOjcfHkZ6Pmp4.fbNs23LOIOFGJreDXVU7K7hfRVPGtw3TJHujlzd1bttUW9u2zECGO2zOsEA9EIt1YmU-abrOpt1vcTxsZvrfCA"
}

resource "yandex_vpc_network" "default" {
  name      = var.network
  folder_id = "b1grh1oiajrordvcn1c6"
}

resource "yandex_vpc_subnet" "default" {
  network_id     = yandex_vpc_network.default.id
  name           = var.subnet
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = var.zone
  folder_id      = "b1grh1oiajrordvcn1c6"
}

resource "yandex_compute_image" "default" {
  source_family = var.image_family
  folder_id     = "b1grh1oiajrordvcn1c6"
}



resource "yandex_compute_disk" "boot-disk" {
  name      = "boot-disk"
  type      = var.disk_type
  zone      = "ru-central1-a"
  size      = var.disk_size
  image_id  = yandex_compute_image.default.id
  folder_id = "b1grh1oiajrordvcn1c6"
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
  zone = var.zone

  resources {
    cores  = var.cores
    memory = var.memory
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat       = var.nat
  }

  metadata = {
    user-data = data.template_file.default.rendered
  }

  timeouts {
    create = var.timeout_create
    delete = var.timeout_delete
  }
  folder_id = "b1grh1oiajrordvcn1c6"
}

output "name" {
  value = yandex_compute_instance.default.name
}

output "address" {
  value = yandex_compute_instance.default.network_interface.0.nat_ip_address
}