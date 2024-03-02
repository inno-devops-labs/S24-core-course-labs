# For docker

<code>terraform state show docker_container.custom_container</code>
```
# docker_container.custom_container:
resource "docker_container" "custom_container" {
    attach                                      = false
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "f7a95d57eb51"
    id                                          = "f7a95d57eb51a4cda7414fe1025ec6e45492b67ccfef11e1800f106840f05d49"
    image                                       = "sha256:ce742cdc2cabfc920f587c004560300e5367a3585a4272225a31827bce0cf749"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "terraform-lab4"
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
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

<code>terraform state show docker_image.custom_image</code>
```
# docker_image.custom_image:
resource "docker_image" "custom_image" {
    id          = "sha256:ce742cdc2cabfc920f587c004560300e5367a3585a4272225a31827bce0cf749furryowolord/lab2"
    image_id    = "sha256:ce742cdc2cabfc920f587c004560300e5367a3585a4272225a31827bce0cf749"
    name        = "furryowolord/lab2"
    repo_digest = "furryowolord/lab2@sha256:99a8657748e96665fb1f051a97717fdbd6a5694efd61a538a2f4c857c0e46a6c"
}
```
<code>terraform state list</code>
```
docker_container.custom_container
docker_image.custom_image
```

## Changes applied

```terraform apply```

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.custom_container will be created
  + resource "docker_container" "custom_container" {
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
      + image                                       = "furryowolord/lab2"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "terraform-lab4"
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
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.custom_image will be created
  + resource "docker_image" "custom_image" {
      + id          = (known after apply)
      + image_id    = (known after apply)
      + name        = "furryowolord/lab2"
      + repo_digest = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + id_of_container    = (known after apply)
  + image_of_container = "furryowolord/lab2"
  + name_of_container  = "terraform-lab4"
  + port_of_container  = [
      + {
          + external = 8000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]
```
## Output
```
id_of_container = "7cde3276fa45490d2dee9a3ec2715347db3b415da30cb2d5f4eb9153e6be982a"
image_of_container = "furryowolord/lab2"
name_of_container = "terraform-lab4"
port_of_container = tolist([
  {
    "external" = 8000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

# For Yandex Cloud

```terraform state list```

```
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```terraform state show yandex_compute_disk.boot-disk-1```
```
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-27T16:34:12Z"
    folder_id   = "b1gvup3s47j516kd9hdh"
    id          = "fhmkjbl97rvtkaiamr31"
    image_id    = "fd87ap2ld09bjiotu5v0"
    name        = "boot-disk-1"
    product_ids = [
        "f2ea07nu3lns12491hku",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

```terraform state show yandex_compute_instance.vm-1```
```
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T16:34:18Z"
    folder_id                 = "b1gvup3s47j516kd9hdh"
    fqdn                      = "fhm24ltfa3g50emcmdl3.auto.internal"
    id                        = "fhm24ltfa3g50emcmdl3"
    metadata                  = {
        "ssh-keys" = <<-EOT
            *my ssh key*
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmkjbl97rvtkaiamr31"
        disk_id     = "fhmkjbl97rvtkaiamr31"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd87ap2ld09bjiotu5v0"
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
        ip_address         = "192.168.10.4"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:22:57:af:50"
        nat                = true
        nat_ip_address     = "51.250.82.195"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bc3e3s75bpipp399v4"
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
``` terraform state show yandex_vpc_network.network-1 ```
```
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-27T16:34:12Z"
    default_security_group_id = "enpk4pmb1qfaf829epeb"
    folder_id                 = "b1gvup3s47j516kd9hdh"
    id                        = "enpuj599931covdoj74a"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}
```
```terraform state show yandex_vpc_subnet.subnet-1  ```
```
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-27T16:34:15Z"
    folder_id      = "b1gvup3s47j516kd9hdh"
    id             = "e9bc3e3s75bpipp399v4"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpuj599931covdoj74a"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Changes applied

```terraform apply```
```
Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = "b1gvup3s47j516kd9hdh"
      + id          = (known after apply)
      + image_id    = "fd87ap2ld09bjiotu5v0"
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
      + folder_id                 = "b1gvup3s47j516kd9hdh"
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
              *my ssh key*
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
      + folder_id                 = "b1gvup3s47j516kd9hdh"
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = "b1gvup3s47j516kd9hdh"
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
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 5s [id=enpuj599931covdoj74a]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9bc3e3s75bpipp399v4]
yandex_compute_disk.boot-disk-1: Creation complete after 8s [id=fhmkjbl97rvtkaiamr31]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Creation complete after 27s [id=fhm24ltfa3g50emcmdl3]
```

## Output
```terraform output```
```
external_ip_address_vm_1 = "51.250.82.195"
internal_ip_address_vm_1 = "192.168.10.4"
```

# Best practices

- Use ```terraform fmt```
- Use ```terraform validate``` and ```terraform plan``` before applying the changes
- Use dependency lock file
- Use variables and outputs
- Use ```terraform import``` to manage existing resourses
- Use ```.gitignore``` for terraform state files