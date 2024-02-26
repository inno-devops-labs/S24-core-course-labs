# Docker
`terraform state show docker_container.nginx` output:
```
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "037087f4a9d0"
    id                                          = "037087f4a9d0817b5995f4c7bfd2b9994696964d30cd471a288778fdf17b3f50"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:03"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

`terraform state list` output:
```
docker_container.nginx
docker_image.nginx
```
### Applied changes
`terraform apply` (for the first time):
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
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
      + name                                        = "tutorial"
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
          + external = 8000
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "nginx"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.
```

`terraform apply` after changing nginx image to time web-app image:
```
docker_image.webapp_image: Refreshing state... [id=sha256:99a1602f74a9280294c0dc6142e1618a775ae4f66b8ceff7a729c338f8a64101soralin/moscow-time-webapp]
docker_container.webapp_container: Refreshing state... [id=a7c8ad8775a38925e4598526370a0956a5063abed1f23752395a9f95c1c10a8b]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.webapp_container must be replaced
-/+ resource "docker_container" "webapp_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "python",
          - "-m",
          - "flask",
          - "--app",
          - "app",
          - "run",
          - "--host=0.0.0.0",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "a7c8ad8775a3" -> (known after apply)
      ~ id                                          = "a7c8ad8775a38925e4598526370a0956a5063abed1f23752395a9f95c1c10a8b" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "lab4"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.3"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:03"
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode                                = "default" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "puppet" -> null
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ internal = 80 -> 5000 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.
```
Finally, `terraform output`:
```
container_id = "fec18179b03914959e3e86b6035ac8a3767ed29fb93dc4728b0ef118ac8eb625"
container_name = "lab4"
image_id = "sha256:99a1602f74a9280294c0dc6142e1618a775ae4f66b8ceff7a729c338f8a64101soralin/moscow-time-webapp"
image_name = "soralin/moscow-time-webapp"
```

# Yandex Cloud
`terraform state list`:
```
yandex_compute_disk.boot-disk-1
yandex_compute_disk.boot-disk-2
yandex_compute_instance.vm-1
yandex_compute_instance.vm-2
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

`terraform state show yandex_compute_disk.boot-disk-1`:
```
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-26T18:15:56Z"
    folder_id   = "b1gv7lr8tdld8u014u17"
    id          = "fhmv5q78l0kjq2drhmai"
    image_id    = "fd8autg36kchufhej85b"
    name        = "boot-disk-1"
    product_ids = [
        "f2e454d6jm9tftcpj6g4",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

`terraform state show yandex_compute_disk.boot-disk-2`:

```
# yandex_compute_disk.boot-disk-2:
resource "yandex_compute_disk" "boot-disk-2" {
    block_size  = 4096
    created_at  = "2024-02-26T18:15:56Z"
    folder_id   = "b1gv7lr8tdld8u014u17"
    id          = "fhmdtupjnsj21m3mcik0"
    image_id    = "fd8autg36kchufhej85b"
    name        = "boot-disk-2"
    product_ids = [
        "f2e454d6jm9tftcpj6g4",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

`terraform state show yandex_compute_instance.vm-1`:

```
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-26T18:16:13Z"
    folder_id                 = "b1gv7lr8tdld8u014u17"
    fqdn                      = "fhm6masii9896tm49j98.auto.internal"
    id                        = "fhm6masii9896tm49j98"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDrAL4ZjIJ3A/a1sJvf683mwro7rRdU3uDj66CMemVpL kurisu@LAPTOP-R4SS6E6D
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmv5q78l0kjq2drhmai"
        disk_id     = "fhmv5q78l0kjq2drhmai"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8autg36kchufhej85b"
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
        ip_address         = "192.168.10.16"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:6b:2b:92:92"
        nat                = true
        nat_ip_address     = "158.160.50.88"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b016qv9uol5c18rs2n"
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
```

`terraform state show yandex_compute_instance.vm-2`:

```
# yandex_compute_instance.vm-2:
resource "yandex_compute_instance" "vm-2" {
    created_at                = "2024-02-26T18:16:13Z"
    folder_id                 = "b1gv7lr8tdld8u014u17"
    fqdn                      = "fhma7h9rhp3lqc829u9v.auto.internal"
    id                        = "fhma7h9rhp3lqc829u9v"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDrAL4ZjIJ3A/a1sJvf683mwro7rRdU3uDj66CMemVpL kurisu@LAPTOP-R4SS6E6D
        EOT
    }
    name                      = "terraform2"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmdtupjnsj21m3mcik0"
        disk_id     = "fhmdtupjnsj21m3mcik0"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8autg36kchufhej85b"
            name       = "boot-disk-2"
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
        ip_address         = "192.168.10.19"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:a3:c5:3b:8e"
        nat                = true
        nat_ip_address     = "158.160.49.163"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b016qv9uol5c18rs2n"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 4
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }
}
```

`terraform state show yandex_vpc_network.network-1`:
```
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-26T18:12:24Z"
    default_security_group_id = "enpujuntv4fe53ee1du1"
    folder_id                 = "b1gv7lr8tdld8u014u17"
    id                        = "enpjuulojvv1bod3q5mk"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9b016qv9uol5c18rs2n",
    ]
}
```

`terraform state show yandex_vpc_subnet.subnet-1`:

```
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-26T18:12:29Z"
    folder_id      = "b1gv7lr8tdld8u014u17"
    id             = "e9b016qv9uol5c18rs2n"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpjuulojvv1bod3q5mk"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

`terraform output`:
```
external_ip_address_vm_1 = "158.160.50.88"
external_ip_address_vm_2 = "158.160.49.163"
internal_ip_address_vm_1 = "192.168.10.16"
internal_ip_address_vm_2 = "192.168.10.19"
```
### Applied changes
`terraform apply`:
```
yandex_vpc_network.network-1: Refreshing state... [id=enpjuulojvv1bod3q5mk]
yandex_vpc_subnet.subnet-1: Refreshing state... [id=e9b016qv9uol5c18rs2n]

Terraform used the selected providers to generate the following execution plan. Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = "b1gv7lr8tdld8u014u17"
      + id          = (known after apply)
      + image_id    = "fd8autg36kchufhej85b"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_disk.boot-disk-2 will be created
  + resource "yandex_compute_disk" "boot-disk-2" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = "b1gv7lr8tdld8u014u17"
      + id          = (known after apply)
      + image_id    = "fd8autg36kchufhej85b"
      + name        = "boot-disk-2"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = "b1gv7lr8tdld8u014u17"
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDrAL4ZjIJ3A/a1sJvf683mwro7rRdU3uDj66CMemVpL kurisu@LAPTOP-R4SS6E6D
            EOT
        }
      + name                      = "terraform1"
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
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = "e9b016qv9uol5c18rs2n"
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

  # yandex_compute_instance.vm-2 will be created
  + resource "yandex_compute_instance" "vm-2" {
      + created_at                = (known after apply)
      + folder_id                 = "b1gv7lr8tdld8u014u17"
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDrAL4ZjIJ3A/a1sJvf683mwro7rRdU3uDj66CMemVpL kurisu@LAPTOP-R4SS6E6D
            EOT
        }
      + name                      = "terraform2"
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
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = "e9b016qv9uol5c18rs2n"
        }

      + resources {
          + core_fraction = 100
          + cores         = 4
          + memory        = 4
        }
    }

Plan: 4 to add, 0 to change, 0 to destroy.
```
# Best Practices

1. Use of `variables.tf`: all repeated variables or sensitive information is stored separately in variables file
(in this case HashiCorp Vault might also come handy)
2. Use of `outputs.tf`: all outputs are declared in separate file and are easy to view with `terraform output`
3. Use of GitHub branch protection and configuration: to enhance the security and offer consistency.
4. Use of `terraform plan` and `terraform validate`: to validate and view changes before applying them (or that will be stored and used later while applying)
