# Terraform lab

## Command outputs and logs

### Docker
* Applied changes:
```
Terraform will perform the following actions:

  # docker_container.moscow_time_python will be created
  + resource "docker_container" "moscow_time_python" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "moscow_time_python"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + ports {
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.moscow_time_python will be created
  + resource "docker_image" "moscow_time_python" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = true
      + name         = "n0m1nd/moscow_time_python:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.
```

* Output of `terraform state list`:
```
docker_container.moscow_time_python
docker_image.moscow_time_python
```

* Output of `terraform state list | xargs -L 1 terraform state show`:
```
# docker_container.moscow_time_python:
resource "docker_container" "moscow_time_python" {
    attach                                      = false
    command                                     = [
        "python3",
        "-m",
        "server",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "e0fe355bece8"
    id                                          = "e0fe355bece8bb7e0d64ad328c6a05b1dfe315fac1ee5d8c890b893d62a3943f"
    image                                       = "sha256:6083be1f4fb0c7528ea25108cd93064f796892ec7353cda42175517ece92fe08"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow_time_python"
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
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/src"

    healthcheck {
        interval     = "1s"
        retries      = 0
        start_period = "0s"
        test         = [
            "CMD-SHELL",
            "curl -f http://localhost:8080/ || exit 1",
        ]
        timeout      = "0s"
    }

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
# docker_image.moscow_time_python:
resource "docker_image" "moscow_time_python" {
    id           = "sha256:6083be1f4fb0c7528ea25108cd93064f796892ec7353cda42175517ece92fe08n0m1nd/moscow_time_python:latest"
    image_id     = "sha256:6083be1f4fb0c7528ea25108cd93064f796892ec7353cda42175517ece92fe08"
    keep_locally = true
    name         = "n0m1nd/moscow_time_python:latest"
    repo_digest  = "n0m1nd/moscow_time_python@sha256:41147a728ac0ebc9b4510564e1c558989aad2d3f8f45cc03b03ba35f4f963fb2"
}
```

* After running `terraform apply -var "container_name=moscow_time_python2"`:
```
# docker_container.moscow_time_python:
resource "docker_container" "moscow_time_python" {
. . .
    name                                        = "moscow_time_python2"
    network_data                                = [
        {
. . .
```

* Output of `terraform output`:
```
container_id = "61bbbef518ff6f08c7b15ad372e879d13c5716d6ffcf5c6110c255c90f431f85"
image_id = "sha256:6083be1f4fb0c7528ea25108cd93064f796892ec7353cda42175517ece92fe08n0m1nd/moscow_time_python:latest"
```

### Yandex Cloud

* Applied changes:
```
Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd80bm0rh4rkepi5ksdi"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 10
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + name                      = "vm-1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = false
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

  # yandex_vpc_network.default will be created
  + resource "yandex_vpc_network" "default" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network-1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.default will be created
  + resource "yandex_vpc_subnet" "default" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "network-1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }
```

* Output of `terraform state list`:
```
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.default
yandex_vpc_subnet.default
```

* Output of `terraform state list | xargs -L 1 terraform state show`:
```
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-27T00:50:07Z"
    folder_id   = "b1g8tkp68th1h6ofkdfq"
    id          = "fhmlvj3ug11ab6vvouoj"
    image_id    = "fd80bm0rh4rkepi5ksdi"
    name        = "boot-disk-1"
    product_ids = [
        "f2e3vsap4cmi4pqk05lg",
    ]
    size        = 10
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T00:50:21Z"
    folder_id                 = "b1g8tkp68th1h6ofkdfq"
    fqdn                      = "fhmdtr5volvsu5b6bkq1.auto.internal"
    id                        = "fhmdtr5volvsu5b6bkq1"
    name                      = "vm-1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmlvj3ug11ab6vvouoj"
        disk_id     = "fhmlvj3ug11ab6vvouoj"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd80bm0rh4rkepi5ksdi"
            name       = "boot-disk-1"
            size       = 10
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
        ip_address         = "192.168.10.13"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:de:ec:bf:c5"
        nat                = false
        security_group_ids = []
        subnet_id          = "e9bpgt9lq4mijvp5d1k0"
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
# yandex_vpc_network.default:
resource "yandex_vpc_network" "default" {
    created_at                = "2024-02-27T00:50:07Z"
    default_security_group_id = "enplkmeqk1jabr6kplmt"
    folder_id                 = "b1g8tkp68th1h6ofkdfq"
    id                        = "enpfhg9afgq15utuep2v"
    labels                    = {}
    name                      = "network-1"
    subnet_ids                = []
}
# yandex_vpc_subnet.default:
resource "yandex_vpc_subnet" "default" {
    created_at     = "2024-02-27T00:50:09Z"
    folder_id      = "b1g8tkp68th1h6ofkdfq"
    id             = "e9bpgt9lq4mijvp5d1k0"
    labels         = {}
    name           = "network-1"
    network_id     = "enpfhg9afgq15utuep2v"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

* `terraform output`:
```
external_ip_address = ""
internal_ip_address = "192.168.10.13"
```
