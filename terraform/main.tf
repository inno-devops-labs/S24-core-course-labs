terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone  = var.zone
  token = "t1.9euelZqTzYubmsnMnsecmZXOlYuUiu3rnpWaipCclJSQjpTGzoqOjZeVjorl8_cxdQtR-e9hYi8N_d3z93EjCVH572FiLw39zef1656VmpiMm87HycqVmovMypnNlpeY7_zN5_XrnpWancqSlY_Pz8qMyceel5eLnY3v_cXrnpWamIybzsfJypWai8zKmc2Wl5g.vLzObm5vzgy6BBnFxtqqlmWIsjr1VkwBh2KszO49Qhvh9RirJQsQj--Dg7wOOvwjbIhrk9UDlHGJsbao9w8LBA"
}

resource "yandex_vpc_network" "default" {
  name      = var.network
  folder_id = "b1gf7fuch5b775aih5hj"
}

resource "yandex_vpc_subnet" "default" {
  network_id     = yandex_vpc_network.default.id
  name           = var.subnet
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = var.zone
  folder_id      = "b1gf7fuch5b775aih5hj"
}

resource "yandex_compute_image" "default" {
  family    = var.image_family
  folder_id = "b1gf7fuch5b775aih5hj"
}

resource "yandex_compute_disk" "boot-disk" {
  name      = "boot-disk"
  type      = var.disk_type
  zone      = "ru-central1-a"
  size      = var.disk_size
  image_id  = yandex_compute_image.default.id
  folder_id = "b1gf7fuch5b775aih5hj"
}

data "template_file" "default" {
  template = file("${path.module}/init.ps1")
  vars     = {
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
  folder_id = "b1gf7fuch5b775aih5hj"
}

output "name" {
  value = yandex_compute_instance.default.name
}

output "address" {
  value = yandex_compute_instance.default.network_interface.0.nat_ip_address
}
