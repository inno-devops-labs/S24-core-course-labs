# Terraform

## Best practices

- Usage of modules for `cloud`, `docker`, `github`
- Following naming conventions
- Declaration of variables and outputs in different files
- Including lock-file into VCS

## Docker

- `terraform state list`

```
docker_container.nginx
docker_image.nginx
```

- `terraform state show docker_container.nginx`

```terraform
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
    hostname                                    = "962813f6dec3"
    id                                          = "962813f6dec393b5e6edc4fda5aa7924572e4a0076e18487deb77ac626252262"
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

- `terraform state show docker_image.nginx`

```terraform
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

### Applied changes log

```terraform
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
      + name                                        = "tutorial_nginx_container"
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
      + name         = "nginx:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.
```

### Output

```terraform
container_id = "f2089a1262391ce7637729fdbb361020536552599b0b1b7f977f285301684acb"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## Yandex Cloud

- `terraform state list`

```
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

- `terraform state show yandex_compute_disk.boot-disk-1`

```terraform
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-24T13:55:08Z"
    folder_id   = "b1g5qj560obk3rtg0arp"
    id          = "fhm79unpt0ecl510mjfe"
    image_id    = "fd8svvs3unvqn83thrdk"
    labels      = {}
    name        = "boot-disk-1"
    product_ids = [
        "f2erca36agei1p5ml8ih",
    ]
    size        = 10
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

- `terraform state show yandex_compute_instance.vm-1`

```terraform
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-24T13:58:57Z"
    folder_id                 = "b1g5qj560obk3rtg0arp"
    fqdn                      = "fhmt6rmfcij9md3eg6dd.auto.internal"
    id                        = "fhmt6rmfcij9md3eg6dd"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEpMqnaLlaRp4LJS5yyM51OwlBUJNw3nFwHZ21C8XwAP under@DESKTOP-K87RABG
        EOT
    }
    name                      = "vmvm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v2"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm79unpt0ecl510mjfe"
        disk_id     = "fhm79unpt0ecl510mjfe"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8svvs3unvqn83thrdk"
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
        ip_address         = "192.168.10.26"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1d:36:ec:f6"
        nat                = true
        nat_ip_address     = "158.160.121.145"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b962ornqmemj7elsku"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 50
        cores         = 2
        gpus          = 0
        memory        = 1
    }

    scheduling_policy {
        preemptible = false
    }
}
```

- `terraform state show yandex_vpc_network.network-1`

```terraform
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-24T13:55:08Z"
    default_security_group_id = "enp03me8o16i2145av2t"
    folder_id                 = "b1g5qj560obk3rtg0arp"
    id                        = "enp4ia08dmk66c57h1er"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9b962ornqmemj7elsku",
    ]
}
```

- `terraform state show yandex_vpc_subnet.subnet-1`

```terraform
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-24T13:55:11Z"
    folder_id      = "b1g5qj560obk3rtg0arp"
    id             = "e9b962ornqmemj7elsku"
    labels         = {}
    name           = "subnet1"
    network_id     = "enp4ia08dmk66c57h1er"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

### Applied changes log

```terraform
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

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
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEpMqnaLlaRp4LJS5yyM51OwlBUJNw3nFwHZ21C8XwAP under@DESKTOP-K87RABG
            EOT
        }
      + name                      = "vmvm"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = "fhm79unpt0ecl510mjfe"
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
          + subnet_id          = "e9b962ornqmemj7elsku"
        }

      + resources {
          + core_fraction = 50
          + cores         = 2
          + memory        = 1
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)
```

### Output

```terraform
external_ip_address_vm_1 = "158.160.121.145"
internal_ip_address_vm_1 = "192.168.10.26"
```