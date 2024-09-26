# Best Practices

- Use terraform validate
- Use terraform variables
- Use terrafom fmt

# Docker

## Commands outputs:

### terraform.apply

```bash
terraform apply

Terraform used the selected providers to generate the following
execution plan. Resource actions are indicated with the following
symbols:
  + create

Terraform will perform the following actions:

  # docker_container.moscow-time-app will be created
  + resource "docker_container" "moscow-time-app" {
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
      + name                                        = "moscow-time-app"
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
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.moscow-time-app will be created
  + resource "docker_image" "moscow-time-app" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "guzelzakirova/moscow-time-app:1.0.0"
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

docker_image.moscow-time-app: Creating...
docker_image.moscow-time-app: Still creating... [10s elapsed]
docker_image.moscow-time-app: Creation complete after 18s [id=sha256:96e3884a621bc212a1594ef2e9399b47aa5e0f8bb40a3eb16a351ae77ab3a46fguzelzakirova/moscow-time-app:1.0.0]
docker_container.moscow-time-app: Creating...
docker_container.moscow-time-app: Creation complete after 0s [id=f374cd63fa07cc2943af2bab7f98a84ba048af8c6b7835cbb90cbebdbc41f461]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "f374cd63fa07cc2943af2bab7f98a84ba048af8c6b7835cbb90cbebdbc41f461"
image_id = "sha256:96e3884a621bc212a1594ef2e9399b47aa5e0f8bb40a3eb16a351ae77ab3a46fguzelzakirova/moscow-time-app:1.0.0"
```

### terraform state show (container)

```bash
# docker_container.moscow-time-app:
resource "docker_container" "moscow-time-app" {
    attach                                      = false
    command                                     = [
        "python",
        "src/main.py",
        "0.0.0.0",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "e3077ec54473"
    id                                          = "e3077ec54473f8656975e4d0b9bb28ab15107b44edd5d8685b281d6f785efb6f"
    image                                       = "sha256:96e3884a621bc212a1594ef2e9399b47aa5e0f8bb40a3eb16a351ae77ab3a46f"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow-time-app"
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
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### terraform state show (image)

```bash
# docker_image.moscow-time-app:
resource "docker_image" "moscow-time-app" {
    id           = "sha256:96e3884a621bc212a1594ef2e9399b47aa5e0f8bb40a3eb16a351ae77ab3a46fguzelzakirova/moscow-time-app:1.0.0"
    image_id     = "sha256:96e3884a621bc212a1594ef2e9399b47aa5e0f8bb40a3eb16a351ae77ab3a46f"
    keep_locally = false
    name         = "guzelzakirova/moscow-time-app:1.0.0"
    repo_digest  = "guzelzakirova/moscow-time-app@sha256:5242765245a643ad42b20a8e8296e504e94278bfce4d15310cdde33cc0d54a2d"
}
```

### terraform state list

```bash
docker_container.moscow-time-app
docker_image.moscow-time-app
```

### terraform output

```bash
container_id = "f374cd63fa07cc2943af2bab7f98a84ba048af8c6b7835cbb90cbebdbc41f461"
image_id = "sha256:96e3884a621bc212a1594ef2e9399b47aa5e0f8bb40a3eb16a351ae77ab3a46fguzelzakirova/moscow-time-app:1.0.0"
PS C:\Users\guzel\OneDrive\Рабочий стол\pr\devops-course\app_python\terraform\docker>
```


# Yandex Cloud

## Commands outputs:

### terraform.apply
```bash
yandex_vpc_network.default: Refreshing state... [id=enp77j67vei37onk6r5k]
yandex_compute_image.default: Refreshing state... [id=fd8ri5b5gubq3ggpuop4]
yandex_compute_disk.boot-disk: Refreshing state... [id=fhmou7ljpub6so2oldlj]
yandex_vpc_subnet.default: Refreshing state... [id=e9btkdc4u2gprf6hiqsj]
yandex_compute_instance.default: Refreshing state... [id=fhmiahf06dpu6dfcsjaf]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk must be replaced
-/+ resource "yandex_compute_disk" "boot-disk" {
      ~ created_at  = "2024-03-04T06:46:50Z" -> (known after apply)
      ~ id          = "fhmou7ljpub6so2oldlj" -> (known after apply)
      - labels      = {} -> null
        name        = "boot-disk"
      ~ product_ids = [
          - "f2ejqncm1j4oqo7g92da",
        ] -> (known after apply)
      ~ status      = "ready" -> (known after apply)
      ~ type        = "network-ssd" -> "network-nvme" # forces replacement
        # (5 unchanged attributes hidden)

      - disk_placement_policy {}
    }

  # yandex_compute_instance.default must be replaced
-/+ resource "yandex_compute_instance" "default" {
      ~ created_at                = "2024-03-04T06:47:06Z" -> (known after apply)
      ~ fqdn                      = "fhmiahf06dpu6dfcsjaf.auto.internal" -> (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      ~ id                        = "fhmiahf06dpu6dfcsjaf" -> (known after apply)
      - labels                    = {} -> null
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + service_account_id        = (known after apply)
      ~ status                    = "running" -> (known after apply)
        # (5 unchanged attributes hidden)

      ~ boot_disk {
          ~ device_name = "fhmou7ljpub6so2oldlj" -> (known after apply)
          ~ disk_id     = "fhmou7ljpub6so2oldlj" # forces replacement -> (known after apply) # forces replacement
          ~ mode        = "READ_WRITE" -> (known after apply)
            # (1 unchanged attribute hidden)

          - initialize_params {
              - block_size = 4096 -> null
              - image_id   = "fd8ri5b5gubq3ggpuop4" -> null
              - name       = "boot-disk" -> null
              - size       = 50 -> null
              - type       = "network-ssd" -> null
            }
        }

      - metadata_options {
          - aws_v1_http_endpoint = 1 -> null
          - aws_v1_http_token    = 2 -> null
          - gce_http_endpoint    = 1 -> null
          - gce_http_token       = 1 -> null
        }

      ~ network_interface {
          ~ index              = 0 -> (known after apply)
          ~ ip_address         = "192.168.10.12" -> (known after apply)
          ~ ipv6               = false -> (known after apply)
          + ipv6_address       = (known after apply)
          ~ mac_address        = "d0:0d:12:54:5e:03" -> (known after apply)
          ~ nat_ip_address     = "158.160.123.70" -> (known after apply)
          ~ nat_ip_version     = "IPV4" -> (known after apply)
          ~ security_group_ids = [] -> (known after apply)
            # (3 unchanged attributes hidden)
        }

      - placement_policy {
          - host_affinity_rules       = [] -> null
          - placement_group_partition = 0 -> null
        }

      ~ resources {
          - gpus          = 0 -> null
            # (3 unchanged attributes hidden)
        }

      - scheduling_policy {
          - preemptible = false -> null
        }

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ address = "158.160.123.70" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_compute_instance.default: Destroying... [id=fhmiahf06dpu6dfcsjaf]
yandex_compute_instance.default: Still destroying... [id=fhmiahf06dpu6dfcsjaf, 10s elapsed]
yandex_compute_instance.default: Still destroying... [id=fhmiahf06dpu6dfcsjaf, 20s elapsed]
yandex_compute_instance.default: Still destroying... [id=fhmiahf06dpu6dfcsjaf, 30s elapsed]
yandex_compute_instance.default: Still destroying... [id=fhmiahf06dpu6dfcsjaf, 40s elapsed]
yandex_compute_instance.default: Destruction complete after 43s
yandex_compute_disk.boot-disk: Destroying... [id=fhmou7ljpub6so2oldlj]
yandex_compute_disk.boot-disk: Destruction complete after 1s
yandex_compute_disk.boot-disk: Creating...
yandex_compute_disk.boot-disk: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk: Creation complete after 14s [id=fhmtct6nmcm46gcknddq]
yandex_compute_instance.default: Creating...
yandex_compute_instance.default: Still creating... [10s elapsed]
yandex_compute_instance.default: Still creating... [20s elapsed]
yandex_compute_instance.default: Creation complete after 25s [id=fhmt7vhdqnpciq20bbat]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.
```

### terraform state show (yandex_compute_disk.boot-disk)
```bash
# yandex_compute_disk.boot-disk:
resource "yandex_compute_disk" "boot-disk" {
    block_size  = 4096
    created_at  = "2024-03-04T07:22:49Z"
    folder_id   = "b1glo8kv2qknqu2lbm9a"
    id          = "fhmnadu2vn7uvogv74ot"
    image_id    = "fd8ri5b5gubq3ggpuop4"
    name        = "boot-disk"
    product_ids = [
        "f2ejqncm1j4oqo7g92da",
    ]
    size        = 50
    status      = "ready"
    type        = "network-ssd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

### terraform state show (yandex_compute_image.default)
```bash
# yandex_compute_image.default:
resource "yandex_compute_image" "default" {
    created_at    = "2024-03-04T06:46:44Z"
    folder_id     = "b1glo8kv2qknqu2lbm9a"
    id            = "fd8ri5b5gubq3ggpuop4"
    labels        = {}
    min_disk_size = 3
    pooled        = false
    product_ids   = [
        "f2ejqncm1j4oqo7g92da",
    ]
    size          = 2
    source_family = "ubuntu-1804-lts"
    status        = "ready"
}
```

### terraform state show (yandex_compute_instance.default)
```bash
# yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    created_at                = "2024-03-04T07:23:05Z"
    folder_id                 = "b1glo8kv2qknqu2lbm9a"
    fqdn                      = "fhmgjturmk2n1u7gbnpi.auto.internal"
    id                        = "fhmgjturmk2n1u7gbnpi"
    metadata                  = {
        "ssh-keys" = "ubuntu:~/.ssh/id_ed25519.pub"
    }
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmnadu2vn7uvogv74ot"
        disk_id     = "fhmnadu2vn7uvogv74ot"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8ri5b5gubq3ggpuop4"
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
        ip_address         = "192.168.10.18"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:10:9f:7d:bb"
        nat                = true
        nat_ip_address     = "130.193.51.105"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9btkdc4u2gprf6hiqsj"
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
```

### terraform state show (yandex_vpc_network.default)
```bash
# yandex_vpc_network.default:
resource "yandex_vpc_network" "default" {
    created_at                = "2024-03-04T06:46:44Z"
    default_security_group_id = "enpiq6e06q88ap85b1mg"
    folder_id                 = "b1glo8kv2qknqu2lbm9a"
    id                        = "enp77j67vei37onk6r5k"
    labels                    = {}
    name                      = "vpc_network"
    subnet_ids                = [
        "e9btkdc4u2gprf6hiqsj",
    ]
}
```

### terraform state show (yandex_vpc_subnet.default)
```bash
# yandex_vpc_subnet.default:
resource "yandex_vpc_subnet" "default" {
    created_at     = "2024-03-04T06:46:47Z"
    folder_id      = "b1glo8kv2qknqu2lbm9a"
    id             = "e9btkdc4u2gprf6hiqsj"
    labels         = {}
    name           = "vpc_subnet"
    network_id     = "enp77j67vei37onk6r5k"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```


### terraform state list

```bash
yandex_compute_disk.boot-disk
yandex_compute_image.default
yandex_compute_instance.default
yandex_vpc_network.default
yandex_vpc_subnet.default
```

### terraform output
```bash
address = "51.250.80.228"
```