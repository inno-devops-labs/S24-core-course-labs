# Terraform...

## Docker

### `terraform apply`

```

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx-server will be created
  + resource "docker_container" "nginx-server" {
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
      + name                                        = "nginx-server"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = true
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
          + external = 4321
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = true
      + name         = "nginx:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Creation complete after 23s [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx-server: Creating...
docker_container.nginx-server: Creation complete after 1s [id=c04d5c9a4d7a54ee42ad5f32731390678d0a450783d727012733dcdfc2ba9410]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "c04d5c9a4d7a54ee42ad5f32731390678d0a450783d727012733dcdfc2ba9410"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

### Terraform state

```
$ terraform state list
docker_container.nginx-server
docker_image.nginx
$ terraform state show docker_image.nginx
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = true
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
$ terraform state show docker_container.nginx-server
# docker_container.nginx-server:
resource "docker_container" "nginx-server" {
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
    hostname                                    = "c04d5c9a4d7a"
    id                                          = "c04d5c9a4d7a54ee42ad5f32731390678d0a450783d727012733dcdfc2ba9410"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "unnamed-nginx-server"
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
    rm                                          = true
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
        external = 4321
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
$
```

### Outputs

```
container_id = "c04d5c9a4d7a54ee42ad5f32731390678d0a450783d727012733dcdfc2ba9410"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## Yandex cloud

### `terraform apply`

```

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8t8vqitgjou20saanq"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
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
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDM+C0veMuYJXT/OFbsXGdk6QJ4r7387SB6pwygthE0wnbvZUElqrM46fRF+rhksDxpZGUpLsz46HNagvjv0bTOkH2cgrtaD99ydfhnYjtydFuZRSiLaXVRArYcNuPbkT8gsTi9SV8P7hCz838dUPMxLFR9VsxIw3pIaZkIJGdrbqa4zrGU+CVivEvpHsJ2ltGGuXCKAzCi1qd7qCqHJqutgzwGP6a9feowiUX538VqvW41gz9ZtJfFyVqEe4JNKt2quQgvCvjRgeJyjmfZE+ThgygTjWolcFG5HAcqODsMbatrc3VRCqQPoKealfVphr/p6Cw7PUqEbJllO50XcNIHsdH/kbZPk6U9cClAc0RB5mGQ1U9fwfkJHoQUu2CuUAlvAoMMiF+QGOOsSfC32WY586KfLjkaq+5AlG/pI4IBadeNfTXy/E7TKH7bwgDKTtOTMqX0pmE0pvY2ytkvMTo0+iNnhl7sol/2i2ocMVXp1s1zFfXdbAvRhBSdxqPT+aE= nikolay@KoLin
            EOT
        }
      + name                      = "terraform1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

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
          + subnet_id          = (known after apply)
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm1 = (known after apply)
  + internal_ip_address_vm1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 2s [id=enpfqqoatq37nf8lnf5l]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9b3q31rt7bqgbcc89f3]
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=fhm58en2t7q6hcdmk2fs]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 32s [id=fhmho4p68ns0k2rst5bs]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm1 = "158.160.100.16"
internal_ip_address_vm1 = "192.168.10.6"
```

### Terraform state

```
$ terraform state list
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
$ terraform state show yandex_compute_disk.boot-disk-1
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-25T15:05:46Z"
    folder_id   = "b1gnuk87u8l89tqt75hn"
    id          = "fhm58en2t7q6hcdmk2fs"
    image_id    = "fd8t8vqitgjou20saanq"
    labels      = {}
    name        = "boot-disk-1"
    product_ids = [
        "f2ectu5pkit47tfmaev0",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
$ terraform state show yandex_vpc_network.network-1
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-25T15:05:46Z"
    default_security_group_id = "enpo95g6hp1gg9rrv4b4"
    folder_id                 = "b1gnuk87u8l89tqt75hn"
    id                        = "enpfqqoatq37nf8lnf5l"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9b3q31rt7bqgbcc89f3",
    ]
}
$ terraform state show yandex_vpc_subnet.subnet-1
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-25T15:05:48Z"
    folder_id      = "b1gnuk87u8l89tqt75hn"
    id             = "e9b3q31rt7bqgbcc89f3"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpfqqoatq37nf8lnf5l"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
$ terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-25T15:05:56Z"
    folder_id                 = "b1gnuk87u8l89tqt75hn"
    fqdn                      = "fhmho4p68ns0k2rst5bs.auto.internal"
    id                        = "fhmho4p68ns0k2rst5bs"
    labels                    = {}
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDM+C0veMuYJXT/OFbsXGdk6QJ4r7387SB6pwygthE0wnbvZUElqrM46fRF+rhksDxpZGUpLsz46HNagvjv0bTOkH2cgrtaD99ydfhnYjtydFuZRSiLaXVRArYcNuPbkT8gsTi9SV8P7hCz838dUPMxLFR9VsxIw3pIaZkIJGdrbqa4zrGU+CVivEvpHsJ2ltGGuXCKAzCi1qd7qCqHJqutgzwGP6a9feowiUX538VqvW41gz9ZtJfFyVqEe4JNKt2quQgvCvjRgeJyjmfZE+ThgygTjWolcFG5HAcqODsMbatrc3VRCqQPoKealfVphr/p6Cw7PUqEbJllO50XcNIHsdH/kbZPk6U9cClAc0RB5mGQ1U9fwfkJHoQUu2CuUAlvAoMMiF+QGOOsSfC32WY586KfLjkaq+5AlG/pI4IBadeNfTXy/E7TKH7bwgDKTtOTMqX0pmE0pvY2ytkvMTo0+iNnhl7sol/2i2ocMVXp1s1zFfXdbAvRhBSdxqPT+aE= nikolay@KoLin
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "deleting"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm58en2t7q6hcdmk2fs"
        disk_id     = "fhm58en2t7q6hcdmk2fs"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8t8vqitgjou20saanq"
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
        ip_address         = "192.168.10.6"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:11:c1:32:64"
        nat                = true
        nat_ip_address     = "158.160.100.16"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b3q31rt7bqgbcc89f3"
    }

    placement_policy {
        host_affinity_rules = []
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
$
```

### Terraform output

```
external_ip_address_vm1 = "158.160.100.16"
internal_ip_address_vm1 = "192.168.10.6"
```

## Best practices

-   Using separate files to define variables or logically independent resources.

-   Using terraform variables to specify API tokens or reousrce ids.

-   Using environment variables to specify sensitive terraform variables.
