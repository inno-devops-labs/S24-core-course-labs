terraform {
  required_providers {
    twc = {
      source = "tf.timeweb.cloud/timeweb-cloud/timeweb-cloud"
    }
  }
  required_version = ">= 1.4.4"
}

provider "twc" {
  token = var.TOKEN
}

data "twc_configurator" "configurator" {
  location = "ru-1"
  disk_type = "nvme"
}

data "twc_os" "os" {
  name = "ubuntu"
  version = "20.04"
}

resource "twc_ssh_key" "your-key" {
  name = "Your key"
  body = file("./.ssh/public.pub")
}

resource "twc_server" "my-timeweb-server" {
  name = "DevOps Course Server"
  os_id = data.twc_os.os.id

  configuration {
    configurator_id = data.twc_configurator.configurator.id
    disk = 10240
    cpu = 1
    ram = 1024
  }

  ssh_keys_ids = [twc_ssh_key.your-key.id]
}
