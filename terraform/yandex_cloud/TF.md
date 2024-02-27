yandex_compute_disk.boot-disk
yandex_compute_image.default
yandex_compute_instance.vm-1
yandex_vpc_network.default
yandex_vpc_subnet.default

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T21:17:37Z"
    folder_id                 = "b1gv4t2t9ahap1g9phga"
    fqdn                      = "fhmjr8b2p0rk3k8o18u4.auto.internal"
    id                        = "fhmjr8b2p0rk3k8o18u4"
    metadata                  = {
        "ssh-keys" = <<-EOT
            yc-user:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIeOUHRHOhVxVtupqO/jlZ72eYpe2VmWF11RQGTg6wcm yaroslav@xiaomao
        EOT
    }
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmue0uulgordfnct909"
        disk_id     = "fhmue0uulgordfnct909"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd84p55lgujrfj1t5qcv"
            name       = "boot-disk"
            size       = 50
            type       = "network-ssd"
        }
    }

    metadata_options {
        aws_v1_http_endpoint = 1
        aws_v1_http_token    = 2
        gce_http_endpoint    = 1
        gce_http_token       = 1
    }

    network_interface {
        index              = 0
        ip_address         = "192.168.10.10"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:13:da:16:2c"
        nat                = true
        nat_ip_address     = "84.201.133.126"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b90c5dgk6geivt2lg5"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }

    timeouts {
        create = "10m"
        delete = "10m"
    }
}
