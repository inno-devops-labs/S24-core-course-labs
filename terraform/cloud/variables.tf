variable "vk_login" {
  description = "Login for the vk cloud account"
  type        = string
}

variable "vk_password" {
  description = "Password for the vk cloud account"
  type        = string
}

variable "image_flavor" {
  type    = string
  default = "Ubuntu-22.04-202208"
}

variable "compute_flavor" {
  type    = string
  default = "Basic-1-2-20"
}

variable "key_pair_name" {
  type    = string
  default = "keypair-terraform"
}

variable "availability_zone_name" {
  type    = string
  default = "MS1"
}