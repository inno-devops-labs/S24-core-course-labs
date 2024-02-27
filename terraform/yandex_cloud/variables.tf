
variable "auth_token" {
  description = "Yandex Cloud identity token"
  type        = string
  default     = "TOKEN"
}

variable "compute_zone" {
  type    = string
  default = "ru-central1-a"
}

variable "cloud_id" {
  type    = string
  default = "CLOUD_ID"
}

variable "folder_id" {
  type    = string
  default = "FOLDER_ID"
}

# variable "key_file" {
#   type    = string
#   default = "key.json"
# }
