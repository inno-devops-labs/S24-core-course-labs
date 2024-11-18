# Configure required providers and version
terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

# Define the Yandex Cloud provider with necessary authentication and configuration
provider "yandex" {
  zone                     = var.time_zone
  cloud_id                 = var.cloud_id
  folder_id                = var.folder_id
  service_account_key_file = "/Users/smasiner/Documents/GitHub/Iwanttodie/Untitled/S24-core-course-labs/terraform/yandex_cloud/key.json"
}

# Create a boot disk for the virtual machine (VM)
resource "yandex_compute_disk" "vm_boot_disk" {
  name     = "vm-boot-disk"
  type     = "network-hdd"
  size     = "8" # Size in GB
  image_id = "fd800c7s2p483i648ifv"
}

# Create a Virtual Private Cloud (VPC) network
resource "yandex_vpc_network" "vpc_network" {
  name = "main-vpc-network"
}

# Create a subnet within the VPC network
resource "yandex_vpc_subnet" "main_subnet" {
  name           = "main-subnet"
  zone           = var.time_zone
  network_id     = yandex_vpc_network.vpc_network.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

# Provision a virtual machine instance
resource "yandex_compute_instance" "time_app_instance" {
  name                      = "time-app-instance"
  allow_stopping_for_update = true
  folder_id                 = var.folder_id

  # Configure VM resources (CPU and memory)
  resources {
    cores  = 2
    memory = 2 # Memory in GB
  }

  # Attach the previously created boot disk to the instance
  boot_disk {
    disk_id = yandex_compute_disk.vm_boot_disk.id
  }

  # Configure networking for the VM, with NAT for internet access
  network_interface {
    subnet_id = yandex_vpc_subnet.main_subnet.id
    nat       = true
  }

  # Set up SSH access with a public key for the 'ubuntu' user
  metadata = {
    ssh-keys = "ubuntu:${file("~/.ssh/id_rsa.pub")}"
  }
}
