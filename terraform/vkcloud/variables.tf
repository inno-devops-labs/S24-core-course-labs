variable "image_flavor" {
  type = string
  default = "Ubuntu-22.04-202208"
}

variable "compute_flavor" {
  type = string
  default = "Basic-1-1-10"
}

variable "key_pair_name" {
  type = string
  default = "Ubuntu-STD2-1-1-10GB-XFvi0K0I"
}

variable "availability_zone_name" {
  type = string
  default = "MS1"
}

variable "instance_name" {
  description = "Value of the Name tag for the VK Cloud instance"
  type        = string
  default     = "devops-vm"
}
