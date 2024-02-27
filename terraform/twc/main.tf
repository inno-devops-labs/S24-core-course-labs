terraform {
  required_providers {
    twc = {
      source = "tf.timeweb.cloud/timeweb-cloud/timeweb-cloud"
    }
  }
}

data "twc_configurator" "configurator" {
  location  = "ru-1"
  disk_type = "nvme"
}

data "twc_os" "os" {
  name    = "ubuntu"
  version = "22.04"
}
resource "twc_server" "lab-4-serv" {
  name  = var.server_name
  os_id = data.twc_os.os.id

  configuration {
    configurator_id = data.twc_configurator.configurator.id
    disk            = 1024 * 10
    cpu             = 1
    ram             = 1024
  }
}