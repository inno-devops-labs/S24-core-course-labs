variable "folder_id" {
  description = "Folder ID of the Yandex.Cloud"
  type        = string
  sensitive   = true
}

variable "cloud_id" {
  description = "ID of the Yandex.Cloud"
  type        = string
  sensitive   = true
}

terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      version = "0.90.0"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  service_account_key_file = "authorized_key.json"
  cloud_id                 = var.cloud_id
  folder_id                = var.folder_id
  zone                     = "ru-central1-a"
}

resource "yandex_iam_service_account" "sa" {
  name = "tf-test-sa"
}


resource "yandex_resourcemanager_folder_iam_member" "sa-editor" {
  folder_id = var.folder_id
  role      = "storage.admin"
  member    = "serviceAccount:${yandex_iam_service_account.sa.id}"
}

resource "yandex_iam_service_account_static_access_key" "sa-stat" {
  service_account_id = yandex_iam_service_account.sa.id
  description        = "static access key for object storage"
}

resource "yandex_storage_bucket" "test" {
  access_key = yandex_iam_service_account_static_access_key.sa-stat.access_key
  secret_key = yandex_iam_service_account_static_access_key.sa-stat.secret_key
  bucket     = "my-test-terraform-bucket-devops"
  acl        = "public-read"
  website {
    index_document = "index.html"
  }
}

resource "yandex_storage_object" "index" {
  access_key = yandex_iam_service_account_static_access_key.sa-stat.access_key
  secret_key = yandex_iam_service_account_static_access_key.sa-stat.secret_key
  bucket     = yandex_storage_bucket.test.id
  key        = "index.html"
  source     = "index.html"
}

output "website_endpoint" {
  value       = yandex_storage_bucket.test.website_endpoint
  description = "Website endpoint"
}
