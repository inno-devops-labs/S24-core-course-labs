# Lab 04 - Ahmad Alhussin

## Commands output for docker

1. `terraform state list`

    The previous command shows:

    ```properties
    docker_container.nginx
    docker_image.nginx
    ```

2. `terraform state show docker_container.nginx`

    The previous command shows:

    ```properties
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
        dns                                         = []
        dns_opts                                    = []
        dns_search                                  = []
        entrypoint                                  = [
            "/docker-entrypoint.sh",
        ]
        env                                         = []
        group_add                                   = []
        hostname                                    = "eef0346a36ce"
        id                                          = "eef0346a36cedea1c21012ec43ceccafe6ec2906b079b6740258ce9c21835b48"
        image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
        init                                        = false
        ipc_mode                                    = "private"
        log_driver                                  = "json-file"
        log_opts                                    = {}
        logs                                        = false
        max_retry_count                             = 0
        memory                                      = 0
        memory_swap                                 = 0
        must_run                                    = true
        name                                        = "nginx_container"
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
        storage_opts                                = {}
        sysctls                                     = {}
        tmpfs                                       = {}
        tty                                         = false
        wait                                        = false
        wait_timeout                                = 60

        ports {
            external = 8080
            internal = 80
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }
    ```

3. `terraform state show docker_image.nginx`

    The previous command shows:

    ```properties
    # docker_image.nginx:
    resource "docker_image" "nginx" {
        id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
        image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
        keep_locally = false
        name         = "nginx"
        repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
    }
    ```
4. `terraform output`

    ```properties
    container_id = "eef0346a36cedea1c21012ec43ceccafe6ec2906b079b6740258ce9c21835b48"
    image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    ```



## Commands output for yandex cloud

1. `terraform state list`

    The previous command shows:

    ```properties
    yandex_compute_disk.boot-disk-1
    yandex_compute_instance.vm-1
    yandex_vpc_network.network-1
    yandex_vpc_subnet.subnet-1
    ```

2. `terraform state show yandex_compute_disk.boot-disk-1`

    ```properties
    # yandex_compute_disk.boot-disk-1:
    resource "yandex_compute_disk" "boot-disk-1" {
        block_size  = 4096
        created_at  = "2024-02-28T00:24:06Z"
        folder_id   = "b1gqie734pcvg0ptngo1"
        id          = "epdth6o8gkamfdd11ei1"
        image_id    = "fd8hnnsnfn3v88bk0k1o"
        labels      = {}
        name        = "boot-disk-1"
        product_ids = [
            "f2ej6hk1qmuqu40ku14r",
        ]
        size        = 8
        status      = "ready"
        type        = "network-hdd"
        zone        = "ru-central1-b"

        disk_placement_policy {}
    }
    ```

3. `terraform state show yandex_compute_instance.vm-1`

    The previous command shows:

    ```properties
    # yandex_compute_instance.vm-1:
    resource "yandex_compute_instance" "vm-1" {
        allow_stopping_for_update = true
        created_at                = "2024-02-28T00:25:13Z"
        folder_id                 = "b1gqie734pcvg0ptngo1"
        fqdn                      = "epdorvn5tj91osfrt6m6.auto.internal"
        id                        = "epdorvn5tj91osfrt6m6"
        metadata                  = {
            "ssh-keys" = <<-EOT
                ubuntu:ssh-rsa <<HIDDEN FOR SECURITY>>
            EOT
        }
        name                      = "terraform"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        status                    = "running"
        zone                      = "ru-central1-b"

        boot_disk {
            auto_delete = true
            device_name = "epdth6o8gkamfdd11ei1"
            disk_id     = "epdth6o8gkamfdd11ei1"
            mode        = "READ_WRITE"

            initialize_params {
                block_size = 4096
                image_id   = "fd8hnnsnfn3v88bk0k1o"
                name       = "boot-disk-1"
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
            ip_address         = "192.168.10.7"
            ipv4               = true
            ipv6               = false
            mac_address        = "d0:0d:18:df:ee:5e"
            nat                = true
            nat_ip_address     = "51.250.104.24"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e2lnf5lcvltjcfpe0id8"
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

4. `terraform state show yandex_vpc_network.network-1`

    The previous command shows:

    ```properties
    # yandex_vpc_network.network-1:
    resource "yandex_vpc_network" "network-1" {
        created_at                = "2024-02-28T00:08:27Z"
        default_security_group_id = "enpvlfkc0dkl0rrtdq5p"
        folder_id                 = "b1gqie734pcvg0ptngo1"
        id                        = "enpm8vvkloenau5vsmpt"
        labels                    = {}
        name                      = "network-1"
        subnet_ids                = [
            "e2lnf5lcvltjcfpe0id8",
        ]
    }
    ```

5. `terraform state show yandex_vpc_subnet.subnet-1`

    ```properties
    # yandex_vpc_subnet.subnet-1:
    resource "yandex_vpc_subnet" "subnet-1" {
        created_at     = "2024-02-28T00:08:30Z"
        folder_id      = "b1gqie734pcvg0ptngo1"
        id             = "e2lnf5lcvltjcfpe0id8"
        labels         = {}
        name           = "subnet-1"
        network_id     = "enpm8vvkloenau5vsmpt"
        v4_cidr_blocks = [
            "192.168.10.0/24",
        ]
        v6_cidr_blocks = []
        zone           = "ru-central1-b"
    }
    ```


6. `terraform output`

    ```properties
    timezone = "ru-central1-b"
    ```
