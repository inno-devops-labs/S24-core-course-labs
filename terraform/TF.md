## Docker
1. **`terraform state list`**
    ```
    docker_container.nginx
    docker_image.nginx
    ```

2. **`terraform state show docker_container.nginx`**
    ```
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
        hostname                                    = "2c3401053cc5"
        id                                          = "2c3401053cc5a9f9dfcaf3d2c07c187b0bbe5c84c070881872ee936959bec312"
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

3. **`terraform state show docker_image.nginx`**
    ```
    resource "docker_image" "nginx" {
        id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
        image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
        keep_locally = false
        name         = "nginx:latest"
        repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
    }
    ```

4. **`terraform output`**
    ```
    container_id = "3154af8b3156a3c55149041e6b001a63a530131c81e7c8b88d64e7a3087d5ee3"
    image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
    ```

## Yandex

1. **`terraform state list`**
    ```
    yandex_compute_disk.boot-disk-1
    yandex_compute_disk.boot-disk-2
    yandex_compute_instance.vm-1
    yandex_compute_instance.vm-2
    yandex_vpc_network.network-1
    yandex_vpc_subnet.subnet-1
    ```

2. **`terraform state show yandex_compute_disk.boot-disk-1`**
    ```
    # yandex_compute_disk.boot-disk-1:
    resource "yandex_compute_disk" "boot-disk-1" {
        block_size  = 4096
        created_at  = "2024-03-04T13:33:16Z"
        folder_id   = "b1gdfa5g164ijsjslt2f"
        id          = "epdfujo4qo2oc9a2g8q5"
        image_id    = "fd8adntm80abl0lh2pa8"
        name        = "boot-disk-1"
        product_ids = [
            "f2emovtn3j6rb7e1vfg5",
        ]
        size        = 20
        status      = "ready"
        type        = "network-hdd"
        zone        = "ru-central1-b"

        disk_placement_policy {}
    }
    ```

3. **`terraform state show yandex_compute_disk.boot-disk-2`**
    ```
    # yandex_compute_disk.boot-disk-2:
    resource "yandex_compute_disk" "boot-disk-2" {
        block_size  = 4096
        created_at  = "2024-03-04T13:33:16Z"
        folder_id   = "b1gdfa5g164ijsjslt2f"
        id          = "epdvmrp6b4jaj963m5m6"
        image_id    = "fd8adntm80abl0lh2pa8"
        name        = "boot-disk-2"
        product_ids = [
            "f2emovtn3j6rb7e1vfg5",
        ]
        size        = 20
        status      = "ready"
        type        = "network-hdd"
        zone        = "ru-central1-b"

        disk_placement_policy {}
    }
    ```

4. **`terraform state show yandex_compute_instance.vm-1`**
    ```
    # yandex_compute_instance.vm-1:
    resource "yandex_compute_instance" "vm-1" {
        created_at                = "2024-03-04T13:33:26Z"
        folder_id                 = "b1gdfa5g164ijsjslt2f"
        fqdn                      = "epdtvbocd08ep105lmit.auto.internal"
        id                        = "epdtvbocd08ep105lmit"
        metadata                  = {
            "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICrrApeAaCsWZVLgYst1TqSeIHs63hWVgkD4jv7+wjPT sarhan@sarhan-HP
            EOT
        }
        name                      = "terraform1"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        status                    = "running"
        zone                      = "ru-central1-b"

        boot_disk {
            auto_delete = true
            device_name = "epdfujo4qo2oc9a2g8q5"
            disk_id     = "epdfujo4qo2oc9a2g8q5"
            mode        = "READ_WRITE"

            initialize_params {
                block_size = 4096
                image_id   = "fd8adntm80abl0lh2pa8"
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
            ip_address         = "192.168.10.21"
            ipv4               = true
            ipv6               = false
            mac_address        = "d0:0d:1d:fa:f0:c6"
            nat                = true
            nat_ip_address     = "84.201.140.230"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e2l9h9iskuprghf4574k"
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

5. **`terraform state show yandex_compute_instance.vm-2`**
    ```
    # yandex_compute_instance.vm-2:
    resource "yandex_compute_instance" "vm-2" {
        created_at                = "2024-03-04T13:33:25Z"
        folder_id                 = "b1gdfa5g164ijsjslt2f"
        fqdn                      = "epdjseb162u4badp1vj4.auto.internal"
        id                        = "epdjseb162u4badp1vj4"
        metadata                  = {
            "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICrrApeAaCsWZVLgYst1TqSeIHs63hWVgkD4jv7+wjPT sarhan@sarhan-HP
            EOT
        }
        name                      = "terraform2"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        status                    = "running"
        zone                      = "ru-central1-b"

        boot_disk {
            auto_delete = true
            device_name = "epdvmrp6b4jaj963m5m6"
            disk_id     = "epdvmrp6b4jaj963m5m6"
            mode        = "READ_WRITE"

            initialize_params {
                block_size = 4096
                image_id   = "fd8adntm80abl0lh2pa8"
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
            ip_address         = "192.168.10.15"
            ipv4               = true
            ipv6               = false
            mac_address        = "d0:0d:13:e3:96:13"
            nat                = true
            nat_ip_address     = "84.201.153.200"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e2l9h9iskuprghf4574k"
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

7. **`terraform state show yandex_vpc_network.network-1`**
    ```
    # yandex_vpc_network.network-1:
    resource "yandex_vpc_network" "network-1" {
        created_at                = "2024-03-04T13:28:10Z"
        default_security_group_id = "enpah66ruo6b9ggmi62b"
        folder_id                 = "b1gdfa5g164ijsjslt2f"
        id                        = "enp9o7dfbur6qatnoo3k"
        labels                    = {}
        name                      = "network1"
        subnet_ids                = [
            "e9bvpeq4k5bf5718ffd2",
        ]
    }
    ```
8. **`terraform state show yandex_vpc_subnet.subnet-1`**
    ```
    # yandex_vpc_subnet.subnet-1:
    resource "yandex_vpc_subnet" "subnet-1" {
        created_at     = "2024-03-04T13:32:58Z"
        folder_id      = "b1gdfa5g164ijsjslt2f"
        id             = "e2l9h9iskuprghf4574k"
        labels         = {}
        name           = "subnet1"
        network_id     = "enp9o7dfbur6qatnoo3k"
        v4_cidr_blocks = [
            "192.168.10.0/24",
        ]
        v6_cidr_blocks = []
        zone           = "ru-central1-b"
    }
    ```

9. **`terraform output`**
    ```
    external_ip_address_vm_1 = "84.201.140.230"
    external_ip_address_vm_2 = "84.201.153.200"
    internal_ip_address_vm_1 = "192.168.10.21"
    internal_ip_address_vm_2 = "192.168.10.15"
    ```