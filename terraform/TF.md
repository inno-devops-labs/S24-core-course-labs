# Terraform 

## Best practises

1. Version Control: Store your Terraform configurations in version control (e.g., Git) to track changes, collaborate with others, and rollback changes if needed.
2. Variables and Outputs: Define variables to parameterize your configurations and outputs to expose important information for other resources or users.
3. Naming resources. Follow a consistent naming convention for resources to make them easier to identify and manage.


## Outputs
### Docker:
#### terraform state show
docker_container.time_web:
resource "docker_container" "time_web" {
    attach                                      = false
    command                                     = [
        "python",
        "time_web.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "731c55478a8b"
    id                                          = "731c55478a8bb2177639f6e6d9081f93d22b5dad53c31f53a96349a6c39f0ff1"
    image                                       = "sha256:32128b35f55df3a3345e7f617ad5bc8725660d2c612aab17b91b68ca1d54d9ec"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "time_web.py"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "default"
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = false
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "myuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

#### terraform output
container_id = "731c55478a8bb2177639f6e6d9081f93d22b5dad53c31f53a96349a6c39f0ff1"
container_name = "time_web.py"


### Yandex Cloud
#### terraform show 
yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-27T19:09:51Z"
    folder_id   = "b1gq9ocnbbosarjqbt4l"
    id          = "fhm7fok9l3s0ta7mj84n"
    name        = "boot-disk-1"
    product_ids = []
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}

yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T19:10:01Z"
    folder_id                 = "b1gq9ocnbbosarjqbt4l"
    fqdn                      = "fhmkcg7qbfjkmot8g2aj.auto.internal"
    id                        = "fhmkcg7qbfjkmot8g2aj"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB7I7xUJwaDEFVJM7baoCMO1J/n/5yizOYH9vJwetX7P renathajrullin@MacBook-Pro-Renat.local
        EOT
    }
    name                      = "time-web-cloud"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm7fok9l3s0ta7mj84n"
        disk_id     = "fhm7fok9l3s0ta7mj84n"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            name       = "boot-disk-1"
            size       = 20
            type       = "network-hdd"
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
        mac_address        = "d0:0d:14:64:0f:a5"
        nat                = true
        nat_ip_address     = "158.160.45.120"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bptfm2sjdq0lu04ume"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}

yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-27T19:09:51Z"
    default_security_group_id = "enppfukaqh3ttmekmji5"
    folder_id                 = "b1gq9ocnbbosarjqbt4l"
    id                        = "enpfj1ovmginololsvq2"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}

yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-27T19:09:54Z"
    folder_id      = "b1gq9ocnbbosarjqbt4l"
    id             = "e9bptfm2sjdq0lu04ume"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpfj1ovmginololsvq2"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}


Outputs:

external_ip_address_vm_1 = "158.160.45.120"
internal_ip_address_vm_1 = "192.168.10.10"

#### terraform output
external_ip_address_vm_1 = "158.160.45.120"
internal_ip_address_vm_1 = "192.168.10.10"




