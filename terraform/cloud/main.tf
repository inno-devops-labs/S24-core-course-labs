data "vkcs_compute_flavor" "compute" {
  name = var.compute_flavor
}

data "vkcs_images_image" "compute" {
  name = var.image_flavor
}

resource "vkcs_compute_instance" "compute" {
  name              = "compute-instance"
  flavor_id         = data.vkcs_compute_flavor.compute.id
  key_pair          = var.key_pair_name
  security_groups   = ["default", "security_group"]
  availability_zone = var.availability_zone_name

  block_device {
    uuid                  = data.vkcs_images_image.compute.id
    source_type           = "image"
    destination_type      = "volume"
    volume_type           = "ceph-ssd"
    volume_size           = 8
    boot_index            = 0
    delete_on_termination = true
  }

  network {
    uuid = vkcs_networking_network.network.id
  }

  depends_on = [
    vkcs_networking_network.network,
    vkcs_networking_subnet.subnetwork
  ]
}

resource "vkcs_networking_floatingip" "fip" {
  pool = data.vkcs_networking_network.extnet.name
}

resource "vkcs_compute_floatingip_associate" "fip" {
  floating_ip = vkcs_networking_floatingip.fip.address
  instance_id = vkcs_compute_instance.compute.id
}

output "instance_fip" {
  value = vkcs_networking_floatingip.fip.address
}