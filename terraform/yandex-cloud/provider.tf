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
  token     = var.secret-token
  cloud_id  = var.yandex-cloud-id
  folder_id = var.yandex-folder-id
}