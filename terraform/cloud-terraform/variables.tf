variable "yandex_token" {
  description = "Yandex Cloud token"
  type        = string
}

variable "yandex_cloud_id" {
  description = "Yandex Cloud cloud id"
  type    = string
}

variable "yandex_folder_id" {
  description = "Yandex Cloud folder id"
  type        = string
}

variable "yandex_image_id" {
  description = "Yandex Cloud image id"
  type        = string
  default     = "fd8b24tqvq7t2f8a1o1s"
}

variable "yandex_compute_zone" {
  description = "Yandex Cloud compute zone"
  type    = string
  default = "ru-central1-a"
}
