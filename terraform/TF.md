# Best practices

# Commands Output

## Docker

```console
$ terraform state list
docker_container.app
docker_image.app
```

```console
$ terraform state show docker_container.app
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python",
        "app.py",
    ]
    env                                         = []
    hostname                                    = "476df821c902"
    id                                          = "476df821c902003b67fb47876217ccc8b148d5a11c8008883df38a694a1180df"
    image                                       = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981c"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscowtime-web-app"
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
    user                                        = "appuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```console
$ terraform state show docker_image.app
# docker_image.app:
resource "docker_image" "app" {
    id           = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981cnabuki/moscowtime-web:latest"
    image_id     = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981c"
    keep_locally = false
    name         = "nabuki/moscowtime-web:latest"
    repo_digest  = "nabuki/moscowtime-web@sha256:b6cf9958dab002926aae0b956ff2f6a4c23a73ba47dbe79fdf6eb29be3d145f3"
}
```

```console
$ terraform output
container_id = "476df821c902003b67fb47876217ccc8b148d5a11c8008883df38a694a1180df"
image_id = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981cnabuki/moscowtime-web:latest"
```

## Yandex Cloud

```console
$ terraform state list
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```console
$ terraform state show yandex_compute_disk.boot-disk-1
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-26T22:41:47Z"
    folder_id   = "b1go42d8nahe3jt1ksa7"
    id          = "fhmucnpgo6ploakfu5u4"
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

```console
$ terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-26T22:41:57Z"
    folder_id                 = "b1go42d8nahe3jt1ksa7"
    fqdn                      = "fhm3ic1qks8ibepbjjg4.auto.internal"
    id                        = "fhm3ic1qks8ibepbjjg4"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGIQcNLErVe6Au22kY/YIRAtKnpOqS0lgbxEOQGlVaqB nabuki@LAPTOP-6UP0H37T
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmucnpgo6ploakfu5u4"
        disk_id     = "fhmucnpgo6ploakfu5u4"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8hnnsnfn3v88bk0k1o"
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
        mac_address        = "d0:0d:39:30:3a:a7"
        nat                = true
        nat_ip_address     = "51.250.78.242"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9br45ol393470oqud3m"
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

```console
$ terraform state show yandex_vpc_network.network-1
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-26T22:37:50Z"
    default_security_group_id = "enpvur6835nb7ph5g333"
    folder_id                 = "b1go42d8nahe3jt1ksa7"
    id                        = "enp9a5sk2a2b3avrngkg"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9br45ol393470oqud3m",
    ]
}
```

```console
$ terraform state show yandex_vpc_subnet.subnet-1
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-26T22:37:52Z"
    folder_id      = "b1go42d8nahe3jt1ksa7"
    id             = "e9br45ol393470oqud3m"
    labels         = {}
    name           = "subnet1"
    network_id     = "enp9a5sk2a2b3avrngkg"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

```console
$ terraform output
external_ip_address_vm_1 = "51.250.78.242"
internal_ip_address_vm_1 = "192.168.10.10"
```