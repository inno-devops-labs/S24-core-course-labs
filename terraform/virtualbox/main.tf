terraform {
  required_providers {
    virtualbox = {
      source  = "shekeriev/virtualbox"
      version = "0.0.4"
    }
  }
}

provider "virtualbox" {
  delay      = 60
  mintimeout = 5
}

resource "virtualbox_vm" "vm1" {
  name      = var.vm_name
  image     = "https://app.vagrantup.com/shekeriev/boxes/ubuntu-20-04-server/versions/0.2/providers/virtualbox/unknown/vagrant.box"
  cpus      = 1
  memory    = "512 mib"
  user_data = file("${path.module}/test_file")

  network_adapter {
    type           = "hostonly"
    device         = "IntelPro1000MTDesktop"
    host_interface = "vboxnet0"
  }
}
