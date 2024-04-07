terraform {
  required_providers {
    twc = {
      source = "tf.timeweb.cloud/timeweb-cloud/timeweb-cloud"
    }
  }
  required_version = ">= 1.4.4"
}

provider "twc" {
  token = var.TIMEWEB_TOKEN
}

data "twc_configurator" "configurator" {
  location = "ru-1"
  disk_type = "nvme"
}

data "twc_os" "os" {
  name = "ubuntu"
  version = "20.04"
}

resource "twc_ssh_key" "timeweb-ssh-key" {
  name = "TimeWeb SSH key"
  body = file("~/.ssh/timeweb_rsa.pub")
}

resource "twc_server" "my-timeweb-server" {
  name = var.server_name
  os_id = data.twc_os.os.id

  ssh_keys_ids = [twc_ssh_key.timeweb-ssh-key.id]

  configuration {
    configurator_id = data.twc_configurator.configurator.id
    disk = 1024 * 15
    cpu = 1
    ram = 1024
  }
}