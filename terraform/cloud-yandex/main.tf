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
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id="e9b9ag2o6frld99chit6"
    nat       = true
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}