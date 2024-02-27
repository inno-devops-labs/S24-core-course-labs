variable "zone" {
    type = string
    default = "ru-central1-a"
}

variable "network" {
    type = string
    default = "ya-network"
}

variable "subnet" {
    type = string
    default = "ya-network"
}

variable "subnet_v4_cidr_blocks" {
    type = list(string)
    default = ["192.168.10.0/24"]
}

variable "nat" {
    type = bool
    default = true
}

variable "image_family" {
    type = string
    default = "ubuntu-1804-lts"
}

variable "name" {
    type = string
    default = "your name"
}

variable "cores" {
    type = number
    default = 2
}

variable "memory" {
    type = number
    default = 1
}

variable "disk_size" {
    type = number
    default = 8
}

variable "disk_type" {
    type = string
    default = "network-nvme"
}

variable "user_name" {
    default = ""
    type = string
}

variable "user_pass" {
    default = ""
    type = string
}

variable "admin_pass" {
    default = ""
    type = string
}