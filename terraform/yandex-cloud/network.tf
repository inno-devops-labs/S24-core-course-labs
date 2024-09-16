resource "yandex_vpc_network" "network-devops-lab" {
  name = "network-devops-lab"
}

resource "yandex_vpc_subnet" "subnet-devops-lab" {
  name           = "subnet-devops-lab"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-devops-lab.id
  v4_cidr_blocks = ["192.168.40.0/24"]
}