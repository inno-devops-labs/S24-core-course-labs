resource "yandex_compute_disk" "boot-disk-1" {
  name = "boot-disk-1"
  type = "network-hdd"
  zone = var.yandex_compute_zone
  size = "10"
  # ubuntu 18.04 lts
  image_id = "fd8b1k66ee99rmt7p9ac"
}

// Create a new instance
resource "yandex_compute_instance" "vm1" {
  name        = "terraform-test"
  platform_id = "standard-v1"
  zone        = var.yandex_compute_zone

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-1.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.test_subnet.id
  }

  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_ed25519.pub")}"
  }
}

resource "yandex_vpc_network" "test_net" {
  name = "test_network"
}

resource "yandex_vpc_subnet" "test_subnet" {
  zone           = var.yandex_compute_zone
  network_id     = yandex_vpc_network.test_net.id
  v4_cidr_blocks = ["10.130.0.0/24"]
}
