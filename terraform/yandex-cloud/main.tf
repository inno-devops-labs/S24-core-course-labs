resource "yandex_compute_disk" "boot-drive-1" {
  zone     = "ru-central1-a"
  name     = "boot-drive-1"
  type     = "network-hdd"
  size     = "20"
  image_id = "fd8t8vqitgjou20saanq"
}

resource "yandex_compute_instance" "devops-lab-machine" {
  name = "devops-lab-machine"
  zone = "ru-central1-a"
  platform_id = "standard-v3"


  resources {
    cores  = 2
    memory = 1
    core_fraction = 20
  }

  scheduling_policy {
    preemptible = true
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-drive-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-devops-lab.id
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}