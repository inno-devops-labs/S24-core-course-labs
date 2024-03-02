terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone = var.zone
  token = "t1.9euelZqcnpbPx56ak5CQm52Rx8yYk-3rnpWamJWTlszJl4vHnczIipCQiovl9PdiQzxR-e9odDTV3fT3InI5UfnvaHQ01c3n9euelZrNiceKkMbKy5rLioqPxpuaj-_8zef1656VmseNy4zPlJvLiZWenZTJzo2X7_3F656Vms2Jx4qQxsrLmsuKio_Gm5qP.Lsn2JP3SF47YEjPcIrNQyUDHeUieTlSgoXKl7DhzGjD8SZZGx0Y9Bl4lETsydHR6xXnwMW_rfWSnbhFSedbWDw"
}

resource "yandex_vpc_network" "default" {
  name = var.network
  folder_id = "b1gvup3s47j516kd9hdh"
}

resource "yandex_vpc_subnet" "default" {
  network_id     = yandex_vpc_network.default.id
  name           = var.subnet
  v4_cidr_blocks = ["192.168.10.0/24"]
  zone           = var.zone
  folder_id = "b1gvup3s47j516kd9hdh"
}

resource "yandex_compute_image" "default" {
  source_family  = var.image_family
  folder_id = "b1gvup3s47j516kd9hdh"
}



resource "yandex_compute_disk" "boot-disk" {
  name     = "boot-disk"
  type     = var.disk_type
  zone     = "ru-central1-a"
  size     = var.disk_size
  image_id = yandex_compute_image.default.id
  folder_id = "b1gvup3s47j516kd9hdh"
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
  zone     = var.zone

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
  folder_id = "b1gvup3s47j516kd9hdh"
}

output "name" {
  value = yandex_compute_instance.default.name
}

output "address" {
  value = yandex_compute_instance.default.network_interface.0.nat_ip_address
}

