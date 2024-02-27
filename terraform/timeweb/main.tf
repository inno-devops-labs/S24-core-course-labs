terraform {
  required_providers {
    twc = {
      source = "tf.timeweb.cloud/timeweb-cloud/timeweb-cloud"
    }
  }
  required_version = ">= 0.13"
}

variable "server_name" {
  description = "Value of the name for server"
  type        = string
  default     = "example-server"
}

data "twc_configurator" "configurator" {
  location = "ru-1"
  disk_type = "nvme"
}

data "twc_os" "os" {
  name = "ubuntu"
  version = "22.04"
}
resource "twc_server" "example-server" {
  name = var.server_name
  os_id = data.twc_os.os.id

  configuration {
    configurator_id = data.twc_configurator.configurator.id
    disk = 1024 * 10
    cpu = 1
    ram = 1024
  }
}

output "main_ipv4" {
  description = "TWC server ipv4"
  value       = twc_server.example-server.main_ipv4
}