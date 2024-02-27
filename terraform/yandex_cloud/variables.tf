variable "metadata_ssh_keys_path" {
  description = "ssh path"
  type        = string
  default     = "C:\\Users\\Дамир\\.ssh\\id_rsa.pub"
}

variable "zone" {
  description = "Availability zone"
  type        = string
  default     = "ru-central1-a"
}

variable "disk_name" {
  description = "Disk name"
  type        = string
  default     = "boot-disk-1"
}

variable "disk_type" {
  description = "Disk type"
  type        = string
  default     = "network-hdd"
}

variable "disk_size" {
  description = "Disk size"
  type        = string
  default     = "20"
}

variable "image_id" {
  description = "Image id"
  type        = string
  default     = "fd8b1uvm6a48q040kcus"
}

variable "folder_id" {
  description = "Folder id"
  type        = string
}

variable "network_name" {
  description = "Network name"
  type        = string
  default     = "network1"
}

variable "subnet_name" {
  description = "Subnet name"
  type        = string
  default     = "subnet1"
}

variable "vm_name" {
  description = "VM name"
  type        = string
  default     = "terraform1"
}
