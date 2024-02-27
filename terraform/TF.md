# Terraform
## Docker
```bash
PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\docker> terraform state show docker_container.moscow-time
# docker_container.moscow-time:
resource "docker_container" "moscow-time" {
    attach                                      = false
    command                                     = [
        "python",
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "ca9be13f38af"
    id                                          = "ca9be13f38af505c9734743cdc3a156de537e239c4a5dbcf8e6abef32a513313"
    image                                       = "sha256:4024a4e13260fae6d930b76ad29a9fc14c2c9b7b60507d9745228deabb6e56a3"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow-time"
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
    user                                        = "user"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\docker> terraform state list docker_container.moscow-time
docker_container.moscow-time
PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\docker> terraform output
container_id = "ca9be13f38af505c9734743cdc3a156de537e239c4a5dbcf8e6abef32a513313"
container_name = "moscow-time"
```

## Yandex Cloud
```bash
Nastya Palashkina, [27.02.2024 21:00]
PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\yandex_cloud> terraform state list
data.yandex_compute_image.ubuntu-2204-lts
yandex_compute_instance.moscow-time
yandex_vpc_address.vm1
yandex_vpc_network.default
yandex_vpc_subnet.subnet1
PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\yandex_cloud> terraform state show yandex_compute_instance.moscow-time
# yandex_compute_instance.moscow-time:
resource "yandex_compute_instance" "moscow-time" {
    created_at                = "2024-02-27T17:55:20Z"
    folder_id                 = "b1gbto4dhqlehd2sftq7"
    fqdn                      = "fhm5caocfuh9pic7bt2v.auto.internal"
    id                        = "fhm5caocfuh9pic7bt2v"
    name                      = "moscow-time"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm6s828egtg8sa6nq12"
        disk_id     = "fhm6s828egtg8sa6nq12"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8hnnsnfn3v88bk0k1o"
            size       = 8
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
        ip_address         = "192.168.10.26"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:56:2b:0c:7f"
        nat                = true
        nat_ip_address     = "158.160.59.152"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bk10p6ihb4msu1plv9"
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
}

PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\yandex_cloud> terraform state show yandex_vpc_address.vm1
# yandex_vpc_address.vm1:
resource "yandex_vpc_address" "vm1" {
    created_at          = "2024-02-27T16:49:33Z"
    deletion_protection = false
    folder_id           = "b1gbto4dhqlehd2sftq7"
    id                  = "e9bvgc9bjoh73518812g"
    labels              = {}
    name                = "terraform1"
    reserved            = true
    used                = false

external_ipv4_address {
        address = "158.160.59.152"
        zone_id = "ru-central1-a"
    }
}
PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\yandex_cloud> terraform state show yandex_vpc_network.default
# yandex_vpc_network.default:
resource "yandex_vpc_network" "default" {
    created_at                = "2024-02-27T17:50:29Z"
    default_security_group_id = "enpoj7htd0018e9teu9h"
    folder_id                 = "b1gbto4dhqlehd2sftq7"
    id                        = "enpabqph9hhckaogqfk5"
    labels                    = {}
    subnet_ids                = []
}
PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\yandex_cloud> terraform state show yandex_vpc_subnet.subnet1
# yandex_vpc_subnet.subnet1:
resource "yandex_vpc_subnet" "subnet1" {
    created_at     = "2024-02-27T17:55:19Z"
    folder_id      = "b1gbto4dhqlehd2sftq7"
    id             = "e9bk10p6ihb4msu1plv9"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpabqph9hhckaogqfk5"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Github
```bash
PS C:\Users\Анастасия\OneDrive\Документы\GitHub\S24-DevOps-labs\terraform\github> terraform import "github_repository.devops-repo" "DevOpslabs"
github_repository.devops-repo: Importing from ID "DevOpslabs"...
github_repository.devops-repo: Import prepared!
  Prepared github_repository for import
github_repository.devops-repo: Refreshing state... [id=DevOpslabs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

## Best Practices
- Using `terraform plan` and `terraform validate` for checking before applying
- Using variables.tf for parametrization
- Using outputs.tf for easy access to significant values
- Do not use access tokens as an environment variable
- Creating directories for different modules that helps with keeping structure clear
