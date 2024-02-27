variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "app_python"
}

variable "image_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "vladdan16/app_python"
}

variable "auth_token" {
  description = "Yandex cloud auth token"
  type        = string
  default     = "token"
}

variable "cloud_id" {
  description = "Yandex Cloud ID"
  type        = string
  default     = "id"
}

variable "folder_id" {
  description = "Yandex Cloud Folder ID"
  type        = string
  default     = "id"
}

variable "compute_zone" {
  description = "Yandex Copute zone"
  type        = string
  default     = "ru-central1-a"
}

