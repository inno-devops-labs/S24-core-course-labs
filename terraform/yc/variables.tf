# global

variable "zone" {
  type    = string
  default = "ru-central1-a"
}


# provider

variable "folder_id" {
  type    = string
  default = "b1g1h1m1femu1na18tl9"
}

# Boot disk

variable "disk_image_id" {
  type    = string
  default = "fd8svvs3unvqn83thrdk"
  description = "Id образа для зашрузачного диска. В данном случае это ubuntu-2204-lts"
}

variable "disk_hdd_size" {
  type    = string
  default = "10"
}

variable "disk_type"{
  type = string
  default = "network-hdd"
  description = "Network storage with HDD backend "
}

# VM

variable "vm_name" {
  type    = string
  default = "terraform_vm"
}

variable "vm_platfom_id" {
  type    = string
  default = "standard-v2"
}

# Subnet 

variable "subnet_v4_cidr_blocks" {
  type    = list(string)
  default = ["192.168.10.0/24"]
}
