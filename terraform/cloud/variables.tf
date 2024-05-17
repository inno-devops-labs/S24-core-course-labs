variable "instances" {
  description = "List of instances"
  type = list(object({
    name = string
    resources = object({
      core          = number
      memory        = number
      core_fraction = optional(number)
      gpus          = optional(number)
    })
    boot_disk = object({
      device_name = optional(string)
      auto_delete = optional(bool)
      mode        = optional(string)
      disk_id     = optional(string)
      initialize_params = optional(object({
        name        = optional(string)
        description = optional(string)
        size        = optional(number)
        block_size  = optional(number)
        type        = optional(string)
        image_id    = optional(string)
        snapshot_id = optional(string)
        }), {
        name        = null
        description = null
        size        = null
        block_size  = null
        type        = null
        image_id    = null
        snapshot_id = null
      })
    })
    network_interface = object({
      subnet_id          = optional(string)
      ipv4               = optional(bool)
      ip_address         = optional(string)
      ipv6               = optional(bool)
      ipv6_address       = optional(string)
      nat                = optional(bool)
      nat_ip_address     = optional(string)
      security_group_ids = optional(list(string))
    })
    secondary_disk = optional(object({
      disk_id     = string
      device_name = optional(string)
      auto_delete = optional(bool)
      mode        = optional(string)
    }))
    scheduling_policy = optional(object({
      preemptible = optional(bool)
    }))
    metadata                  = optional(map(string))
    description               = optional(string)
    zone                      = optional(string)
    platform_id               = optional(string)
    allow_stopping_for_update = optional(bool)
  }))
}

variable "default_disk_initialize_params" {
  type = object({
    image_id    = string
    size        = number
    name        = optional(string)
    description = optional(string)
    block_size  = optional(number)
    type        = optional(string)
    snapshot_id = optional(string)
  })
  default = {
    size     = 64
    image_id = "fd80bm0rh4rkepi5ksdi" // ubunut 22.04 lts
  }
}

variable "default_subnet_id" {
  type    = string
  default = ""
}

variable "default_user-data" {
  type      = string
  sensitive = true
}
