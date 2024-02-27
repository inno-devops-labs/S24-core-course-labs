variable "zone" {
  type = string
  default = "ru-central1-a"
}

variable "token" {
  type = string
}

variable "image_family" {
  type = string
  default = "ubuntu-2204-lts"
}

variable "disk_type" {
  type = string
  default = "network-nvme"
}

variable "disk_size" {
  type = number
  default = 50
}

variable "folder_id" {
  type = string
  default = "b1gv4t2t9ahap1g9phga"
}

variable "network" {
  type = string
  default = "ya-network"
}

variable "subnet" {
  type = string
  default = "ya-network"
}

variable "timeout_create" {
  type = string
  default = "10m"
}

variable "timeout_delete" {
  type = string
  default = "10m"
}

variable "cores" {
  type = number
  default = 2
}

variable "memory" {
  type = number
  default = 4
}
