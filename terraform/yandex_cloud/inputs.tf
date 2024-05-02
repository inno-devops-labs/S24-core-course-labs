variable "yandex_cloud_id" {
  type = string
}

variable "yandex_folder_id" {
  type = string
}

variable "yandex_token" {
  type        = string
  description = "Obtain at https://oauth.yandex.com/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb"
  sensitive   = true
}
