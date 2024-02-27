# Terraform

## Best Practicies

- Variables and outputs are declared in separate files
- Format and validate the configuration using ```terraform fmt``` and ```terraform validate``` commands
- Provide outputs
- Avoid using hard-coded values

## Docker

<details>

### The output of the following commands
1. 
```sh
    $ terraform state list
    docker_container.nginx
    docker_image.nginx
```

2.
```sh
    $ terraform state show docker_container.nginx
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
        hostname                                    = "71aa38e9488c"
        id                                          = "71aa38e9488cafb361d3922854d94d9cc44e039c4196256f2e611fc277455b32"
        image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
        init                                        = false
        ipc_mode                                    = "private"
        log_driver                                  = "json-file"
        logs                                        = false
        max_retry_count                             = 0
        memory                                      = 0
        memory_swap                                 = 0
        must_run                                    = true
        name                                        = "ExampleNginxContainer"
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
            external = 8080
            internal = 80
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }
```

3.
```sh
    $ terraform state show docker_image.nginx
    # docker_image.nginx:
    resource "docker_image" "nginx" {
        id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
        image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
        keep_locally = false
        name         = "nginx:latest"
        repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
    }
```

### A part of the log with the applied changes

```sh
    $ terraform apply
    docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
    docker_container.nginx: Refreshing state... [id=3fb89b1397a557ea7540a7a90505e7aec6706aa7399d22392db8d985aa635e32]
    
    Terraform used the selected providers to generate the following execution plan.
    Resource actions are indicated with the following symbols:
    -/+ destroy and then create replacement
    
    Terraform will perform the following actions:
    
      # docker_container.nginx must be replaced
    -/+ resource "docker_container" "nginx" {
          + bridge                                      = (known after apply)
          ~ command                                     = [
              - "nginx",
              - "-g",
              - "daemon off;",
            ] -> (known after apply)
          + container_logs                              = (known after apply)
          - cpu_shares                                  = 0 -> null
          - dns                                         = [] -> null
          - dns_opts                                    = [] -> null
          - dns_search                                  = [] -> null
          ~ entrypoint                                  = [
              - "/docker-entrypoint.sh",
            ] -> (known after apply)
          ~ env                                         = [] -> (known after apply)
          + exit_code                                   = (known after apply)
          - group_add                                   = [] -> null
          ~ hostname                                    = "3fb89b1397a5" -> (known after apply)
          ~ id                                          = "3fb89b1397a557ea7540a7a90505e7aec6706aa7399d22392db8d985aa635e32" -> (known after apply)
          ~ init                                        = false -> (known after apply)
          ~ ipc_mode                                    = "private" -> (known after apply)
          ~ log_driver                                  = "json-file" -> (known after apply)
          - log_opts                                    = {} -> null
          - max_retry_count                             = 0 -> null
          - memory                                      = 0 -> null
          - memory_swap                                 = 0 -> null
          ~ name                                        = "YetAnotherName" -> "ExampleNginxContainer" # forces replacement
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
          ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
          ~ stop_timeout                                = 0 -> (known after apply)
          - storage_opts                                = {} -> null
          - sysctls                                     = {} -> null
          - tmpfs                                       = {} -> null
            # (14 unchanged attributes hidden)
    
            # (1 unchanged block hidden)
        }
    
    Plan: 1 to add, 0 to change, 1 to destroy.
    
    Changes to Outputs:
      + container_id = (known after apply)
      + image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

```sh
    $ terraform output
    container_id = "71aa38e9488cafb361d3922854d94d9cc44e039c4196256f2e611fc277455b32"
    image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

</details>

## Yandex Cloud

<details>

### Apply changes:

```sh
$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd83s8u085j3mq231ago"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 8
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = (known after apply)
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + allow_stopping_for_update = true
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
                ubuntu:#cloud-config
                users:
                  - name: alyona_art
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh-authorized-keys:
                      - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL7WL90vSP1Ln9IACf5ai11B6/3rwhLDgtGZVXvOuvvY everyonehateme@everyonehateme-X99-KD
            EOT
        }
      + name                      = "terraform1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v3"
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
          + core_fraction = 20
          + cores         = 2
          + memory        = 1
        }

      + scheduling_policy {
          + preemptible = true
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
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

```


```sh
    $ terraform state list
    yandex_compute_disk.boot-disk-1
    yandex_compute_instance.vm-1
    yandex_vpc_network.network-1
    yandex_vpc_subnet.subnet-1
```

```sh
$ terraform state show yandex_compute_disk.boot-disk-1
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-27T16:07:41Z"
    folder_id   = "b1gunbvm21fu9od4d9r4"
    id          = "fhmhtdp3g6hpto7b8o43"
    image_id    = "fd83s8u085j3mq231ago"
    name        = "boot-disk-1"
    product_ids = [
        "f2eth1eavhqoh47mqj08",
    ]
    size        = 8
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

```sh
$ terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    allow_stopping_for_update = true
    created_at                = "2024-02-27T16:07:52Z"
    folder_id                 = "b1gunbvm21fu9od4d9r4"
    fqdn                      = "fhm5c9r0hog8dhe4djgb.auto.internal"
    id                        = "fhm5c9r0hog8dhe4djgb"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:#cloud-config
            users:
              - name: alyona_art
                groups: sudo
                shell: /bin/bash
                sudo: 'ALL=(ALL) NOPASSWD:ALL'
                ssh-authorized-keys:
                  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL7WL90vSP1Ln9IACf5ai11B6/3rwhLDgtGZVXvOuvvY everyonehateme@everyonehateme-X99-KD
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v3"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmhtdp3g6hpto7b8o43"
        disk_id     = "fhmhtdp3g6hpto7b8o43"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd83s8u085j3mq231ago"
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
        ip_address         = "192.168.10.27"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:56:27:60:8e"
        nat                = true
        nat_ip_address     = "62.84.125.49"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b9d7bl8n2t981gkd74"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 20
        cores         = 2
        gpus          = 0
        memory        = 1
    }

    scheduling_policy {
        preemptible = true
    }
}
```

```sh
$ terraform state show yandex_vpc_network.network-1
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-27T16:07:41Z"
    default_security_group_id = "enp8slsecjp36uc42n7i"
    folder_id                 = "b1gunbvm21fu9od4d9r4"
    id                        = "enpahc4uood5r4bqn92j"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}
```

```sh
    $ terraform state show yandex_vpc_subnet.subnet-1
    # yandex_vpc_subnet.subnet-1:
    resource "yandex_vpc_subnet" "subnet-1" {
        created_at     = "2024-02-27T16:07:44Z"
        folder_id      = "b1gunbvm21fu9od4d9r4"
        id             = "e9b9d7bl8n2t981gkd74"
        labels         = {}
        name           = "subnet1"
        network_id     = "enpahc4uood5r4bqn92j"
        v4_cidr_blocks = [
            "192.168.10.0/24",
        ]
        v6_cidr_blocks = []
        zone           = "ru-central1-a"
    }
```

</details>

## Github and Github Teams

I created a test repository:
https://github.com/devops-terraform-lab4/terraform-lab-4

And attached screenshot with GitHub teams ```teams.jpg```