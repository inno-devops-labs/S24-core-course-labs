variable "folder_id" {
  description = "ID for the folder"
  default = "b1glo8kv2qknqu2lbm9a"
}

variable "zone" {
    default = "ru-central1-a"
}

variable "network" {
  default = "vpc_network"
}

variable "subnet" {
  default = "vpc_subnet"
}

variable "image_family" {
  default = "ubuntu-1804-lts"
}

variable "disk_type" {
  default = "network-nvme"
}

variable "token" {
  type = string
}