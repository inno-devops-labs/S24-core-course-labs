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
  token     = var.secret_token
  cloud_id  = var.yandex_cloud_id
  folder_id = var.yandex_folder_id
}