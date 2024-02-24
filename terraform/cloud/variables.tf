variable "zone" {
  type = string
  default = "ru-central1-a"
}

variable "vm_name" {
  type = string
  default = "terraform_vm"
}

variable "image_id" {
  type = string
  default = "fd8svvs3unvqn83thrdk"
}

variable "hdd_size" {
  type = string
  default = "10"
}