resource "yandex_compute_disk" "boot-disk-1" {
  zone     = "ru-central1-a"
  name     = "boot-disk-1"
  type     = "network-hdd"
  size     = "20"
  image_id = "fd8t8vqitgjou20saanq"
}

resource "yandex_compute_instance" "devops-vm" {
  name = "devops-moscow-app"
  zone = "ru-central1-a"

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
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "moscow-app"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.50.0/24"]
}