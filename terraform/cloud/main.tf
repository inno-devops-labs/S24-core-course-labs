terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

variable "token" {
  description = "oath token"
  type        = string
}

variable "cloud_id" {
  description = "cloud id"
  type        = string
}

variable "folder_id" {
  description = "folder id"
  type        = string
}

provider "yandex" {
  token     = var.token
  cloud_id  = var.cloud_id
  folder_id = var.folder_id
}

resource "yandex_vpc_network" "network-1" {
  name = "network1"
}

resource "yandex_vpc_subnet" "subnet-1" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network-1.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

output "network_id" {
  description = "ID of the cloud vpc network"
  value       = yandex_vpc_network.network-1.id
}

output "subnet_id" {
  description = "ID of the cloud vpc subnet"
  value       = yandex_vpc_subnet.subnet-1.id
}
