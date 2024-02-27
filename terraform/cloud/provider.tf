terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  cloud_id                 = file("${path.root}/data/cloud_id")
  folder_id                = file("${path.root}/data/folder_id")
  zone                     = "ru-central1-b"
  service_account_key_file = file("${path.root}/data/sa-terraform.secret.json")
}