# Terraform 

# Applied Best Practices

- main.tf is divided into main.tf, variables.tf, and outputs.tf
- used terraform validate for validation
- used terraform fmt
- description is included on all variables

## Docker

* `terraform state show docker_container.app_python_container` output:

```
# docker_container.app_python_container:
resource "docker_container" "app_python_container" {
    attach                                      = false
    command                                     = [
        "python",
        "app_python.py",
        "runserver",
        "--host",
        "0.0.0.0",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "593843601db7"
    id                                          = "593843601db7b3b82292a22770f92571c0cc83d5557e64273015f7f6c0ede7d0"
    image                                       = "sha256:06debb6210170dc3e8263dd5b879503f1207dc0aeafc7ef3fe9691dc5bd35147"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
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
    working_dir                                 = "/app_python"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
* command `terraform state show docker_image.app_python_image`:
```
# docker_image.app_python_image:
resource "docker_image" "app_python_image" {
    id           = "sha256:06debb6210170dc3e8263dd5b879503f1207dc0aeafc7ef3fe9691dc5bd35147arinazaza/app_python.py"
    image_id     = "sha256:06debb6210170dc3e8263dd5b879503f1207dc0aeafc7ef3fe9691dc5bd35147"
    keep_locally = false
    name         = "arinazaza/app_python.py"
    repo_digest  = "arinazaza/app_python.py@sha256:74b8480ddd072be066700577f7efcbe49780d76ed32247350dee57a86778f4b0"
}
```

* `terraform state list` output:

```
docker_container.app_python_container
docker_image.app_python_image
```

* `terraform output` output:

```
container_id = "593843601db7b3b82292a22770f92571c0cc83d5557e64273015f7f6c0ede7d0"
container_name = "app_python"
image_id = "sha256:06debb6210170dc3e8263dd5b879503f1207dc0aeafc7ef3fe9691dc5bd35147arinazaza/app_python.py"
image_name = "arinazaza/app_python.py"
```
* `terraform apply` output:

```
docker_image.app_python_image: Refreshing state... [id=sha256:06debb6210170dc3e8263dd5b879503f1207dc0aeafc7ef3fe9691dc5bd35147arinazaza/app_python.py]
docker_container.app_python_container: Refreshing state... [id=72b704763200a8469814c6d34c2c836a2f4aab09ef84d06da6564fd2aeef9fa3]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_python_container must be replaced
-/+ resource "docker_container" "app_python_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "python",
          - "app_python.py",
          - "runserver",
          - "--host",
          - "0.0.0.0",
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
      ~ hostname                                    = "72b704763200" -> (known after apply)
      ~ id                                          = "72b704763200a8469814c6d34c2c836a2f4aab09ef84d06da6564fd2aeef9fa3" -> (known after apply)
      ~ image                                       = "sha256:06debb6210170dc3e8263dd5b879503f1207dc0aeafc7ef3fe9691dc5bd35147" -> "arinazaza/app_python.py" # forces replacement       
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "app_python"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:02"
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
      - working_dir                                 = "/app_python" -> null
        # (13 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + container_id   = (known after apply)
  + container_name = "app_python"
  + image_id       = "sha256:06debb6210170dc3e8263dd5b879503f1207dc0aeafc7ef3fe9691dc5bd35147arinazaza/app_python.py"
  + image_name     = "arinazaza/app_python.py"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_python_container: Destroying... [id=72b704763200a8469814c6d34c2c836a2f4aab09ef84d06da6564fd2aeef9fa3]
docker_container.app_python_container: Destruction complete after 0s
docker_container.app_python_container: Creating...
docker_container.app_python_container: Creation complete after 1s [id=593843601db7b3b82292a22770f92571c0cc83d5557e64273015f7f6c0ede7d0]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "593843601db7b3b82292a22770f92571c0cc83d5557e64273015f7f6c0ede7d0"
container_name = "app_python"
image_id = "sha256:06debb6210170dc3e8263dd5b879503f1207dc0aeafc7ef3fe9691dc5bd35147arinazaza/app_python.py"
image_name = "arinazaza/app_python.py"
```

## Yandex Cloud

* `terraform apply` output:

```
yandex_vpc_network.network-1: Refreshing state... [id=enp692ghakvd14ute1lf]
yandex_vpc_subnet.subnet-1: Refreshing state... [id=e9bctkclhpja4o49u93b]
yandex_compute_instance.vm-1: Refreshing state... [id=fhm0l9kifi95j68k1ou1]

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8hnnsnfn3v88bk0k1o"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_compute_disk.boot-disk-1: Creating...
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 14s [id=fhm8js4kd2bn8n124fg2]
```
* `terraform state list` output:
```
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```
* `terraform state show yandex_compute_disk.boot-disk-1` output:

```
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-29T11:09:46Z"
    folder_id   = "b1gndq8hffhg542i3tkr"
    id          = "fhm8js4kd2bn8n124fg2"
    image_id    = "fd8hnnsnfn3v88bk0k1o"
    name        = "boot-disk-1"
    product_ids = [
        "f2ej6hk1qmuqu40ku14r",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```
* `terraform state show yandex_compute_instance.vm-1` output:
```
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-29T11:08:17Z"
    folder_id                 = "b1gndq8hffhg542i3tkr"
    fqdn                      = "fhm0l9kifi95j68k1ou1.auto.internal"
    id                        = "fhm0l9kifi95j68k1ou1"
    labels                    = {}
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINCO95nJmvYiTJfLxqTUtJqiBzDotU+5iYa2/LcjwoM4 arina@LAPTOP-6226NO20
        EOT
    }
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhms9vjcmrpr0gq0l2p8"
        disk_id     = "fhms9vjcmrpr0gq0l2p8"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd83s8u085j3mq231ago"
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
        ip_address         = "192.168.20.31"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:aa:69:27:c9"
        nat                = true
        nat_ip_address     = "158.160.123.53"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bctkclhpja4o49u93b"
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
* ` terraform state show yandex_vpc_network.network-1` output:
```
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-29T11:08:14Z"
    default_security_group_id = "enpalritdqkiodhjao8h"
    folder_id                 = "b1gndq8hffhg542i3tkr"
    id                        = "enp692ghakvd14ute1lf"
    labels                    = {}
    name                      = "network-1"
    subnet_ids                = [
        "e9bctkclhpja4o49u93b",
    ]
}
```
* `terraform state show yandex_vpc_subnet.subnet-1` output:

```
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-29T11:08:16Z"
    folder_id      = "b1gndq8hffhg542i3tkr"
    id             = "e9bctkclhpja4o49u93b"
    labels         = {}
    name           = "Subnet 1"
    network_id     = "enp692ghakvd14ute1lf"
    v4_cidr_blocks = [
        "192.168.20.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```