variable "token" {
  description = "YC token"
  type        = string
}

variable "folder_id" {
  description = "YC folder_id"
  type        = string
}

variable "zone" {
  type    = string
  default = "ru-central1-a"
}

variable "cores" {
  type    = number
  default = 2
}

variable "memory" {
  type    = number
  default = 2
}

variable "disk_size" {
  type    = number
  default = 8
}

variable "disk_type" {
  type    = string
  default = "network-hdd"
}

