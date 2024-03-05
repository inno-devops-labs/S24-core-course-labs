terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  zone      = "ru-central1-a"
  token     = "t1.9euelZqakI2Qm4nHlcvIlpWQlc6Qzu3rnpWancqVnoyRzYnLls3JzJSKnsnl8_ctT35Q-e8DIRkH_t3z9219e1D57wMhGQf-zef1656VmseUzZiKnZeNi5aJmJ6dnpXH7_zN5_XrnpWaisaRmcvMkYmWjJHOycfHxsnv_cXrnpWax5TNmIqdl42LlomYnp2elcc.ThREL8XoJeInD42dBS8Qs_KtJRwC7zKKeHQ3G2wbkrpLm4nX0HcGW9zd4W7QXzg-47L-Q15L2RP7Wvf4u0GOBA"
  cloud_id  = "b1gn9uf42257qorpmcho"
  folder_id = "b1gndq8hffhg542i3tkr"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = "fd8hnnsnfn3v88bk0k1o"
}

resource "yandex_vpc_network" "network-1" {
  name = "network-1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "Subnet 1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.20.0/24"]
}

resource "yandex_compute_instance" "vm-1" {
  name = "terraform-vm"

  resources {
    memory = 2
    cores  = 2
  }

  boot_disk {
    initialize_params {
      image_id = "fd83s8u085j3mq231ago"
    }
  }

  metadata = {
    ssh-keys = format("%s:%s", "ubuntu", file("~/.ssh/id_ed25519.pub"))
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }
}