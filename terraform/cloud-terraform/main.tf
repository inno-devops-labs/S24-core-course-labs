terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  zone  = "ru-central1-a"
  token = "t1.9euelZrImcaMz4yRx8-bycrLjJHPjO3rnpWajsebzpWQj5vPi57IxpORyZjl8_cYZWxQ-e9XM1JW_t3z91gTalD571czUlb-zef1656VmseZjJeLk8yenpeMyY-bmcnP7_zN5_XrnpWalIzPy83GypCcmYrPypzNno3v_cXrnpWax5mMl4uTzJ6el4zJj5uZyc8.IZkye1S06jtGU4n-3YMS-pZcmJm3UeLZmxniJBHlmaG9_V9Avrcc1zh17URTkm5Vu8X9myaH8wAPYpOCA-1ZCQ"
}

resource "yandex_compute_disk" "boot-disk-1" {
  name     = "boot-disk-1"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = "fd8hnnsnfn3v88bk0k1o"
  folder_id = "b1g5s23m0hvfb94fvpoq"
}

resource "yandex_compute_disk" "boot-disk-2" {
  name     = "boot-disk-2"
  type     = "network-hdd"
  zone     = "ru-central1-a"
  size     = "20"
  image_id = "fd8hnnsnfn3v88bk0k1o"
  folder_id = "b1g5s23m0hvfb94fvpoq"
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
    user-data = "${file("meta.txt")}"
  }
  folder_id = "b1g5s23m0hvfb94fvpoq"
}

resource "yandex_compute_instance" "vm-2" {
  name = "terraform2"

  resources {
    cores  = 4
    memory = 4
  }

  boot_disk {
    disk_id = yandex_compute_disk.boot-disk-2.id
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.subnet-1.id
    nat       = true
  }

  metadata = {
    user-data = "${file("meta.txt")}"
  }
  folder_id = "b1g5s23m0hvfb94fvpoq"
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
  folder_id = "b1g5s23m0hvfb94fvpoq"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
  folder_id = "b1g5s23m0hvfb94fvpoq"
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "internal_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}

output "external_ip_address_vm_2" {
  value = yandex_compute_instance.vm-2.network_interface.0.nat_ip_address
}
