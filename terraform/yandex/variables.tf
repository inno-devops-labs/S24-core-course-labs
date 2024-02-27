variable "zone" {
  description = "Yandex Cloud Compute zone to be used"
  type        = string
  default     = "ru-central1-a"
}

variable "vm_name" {
  description = "Yandex Cloud Compute vm name"
  type        = string
  default     = "vm-1"
}

variable "network_name" {
  description = "Yandex Cloud Compute network name"
  type        = string
  default     = "network-1"
}

variable "subnet_name" {
  description = "Yandex Cloud Compute subnet name"
  type        = string
  default     = "network-1"
}

variable "nat" {
  description = "Use nat"
  type        = bool
  default     = false
}

variable "image_id" {
  description = "Image id to use with the vm (default: ubuntu-22-04-lts-v20230925)"
  type        = string
  default     = "fd80bm0rh4rkepi5ksdi"
}
