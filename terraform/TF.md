# Terraform

## Best Practices Applied

- Stored configuration files in VCS;
- Used variables and outputs files;
- Stored sensitive info in .tfvars files;
- Planned and reviewed changes before application.

## Docker command outputs

```bash
$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
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
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Creation complete after 8s [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Creating...

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

```bash
$ terraform state list
docker_container.nginx
docker_image.nginx
```

```bash
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
    hostname                                    = "597aa089ceae"
    id                                          = "597aa089ceae94fa7265912271d7b52b6fa95fe03bfa9c811a575587c6c875d4"
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

```bash
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

```bash
$ terraform output
container_id = "7777ff2e657afb002703dd76feffb8f05e525b73a5ce512d15047e175b166db6"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## Yandex Cloud command outputs

```bash
$ terraform apply
docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Refreshing state... [id=7f50b82ad3a8a14ec3ab95b07c8243560952d785a3d76c169e35a1b0558c20d3]
yandex_vpc_network.network-1: Refreshing state... [id=enpp88amqva30hnnnhhv]
yandex_compute_disk.boot-disk-1: Refreshing state... [id=fhm8716enlkivmdqktas]
yandex_vpc_subnet.subnet-1: Refreshing state... [id=e9bv27imeg76ibb3f9cd]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
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
          + "user-data" = <<-EOT
                #cloud-config
                users:
                  - name: devops_user
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh-authorized-keys:
                      - ssh-rsa AAAAB3NzaC**************************************************
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
          + disk_id     = "fhm8716enlkivmdqktas"
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
          + subnet_id          = "e9bv27imeg76ibb3f9cd"
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Creation complete after 25s [id=fhmaf932ebrtp259lo5p]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

container_id = "7f50b82ad3a8a14ec3ab95b07c8243560952d785a3d76c169e35a1b0558c20d3"
external_ip_address_vm_1 = "84.201.***.***"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
internal_ip_address_vm_1 = "192.168.10.21"
```

```bash
$ terraform state list
docker_container.nginx
docker_image.nginx
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```bash
$ terraform state show yandex_compute_disk.boot-disk-1
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-28T00:28:08Z"
    folder_id   = "b1gnnf3j8bv1kfirnuq4"
    id          = "fhm8716enlkivmdqktas"
    image_id    = "fd83s8u085j3mq231ago"
    labels      = {}
    name        = "boot-disk-1"
    product_ids = [
        "f2eth1eavhqoh47mqj08",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

```bash
$ terraform state show yandex_compute_instance.vm-1   
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-28T00:30:01Z"
    folder_id                 = "b1gnnf3j8bv1kfirnuq4"
    fqdn                      = "fhmaf932ebrtp259lo5p.auto.internal"
    id                        = "fhmaf932ebrtp259lo5p"
    metadata                  = {
        "user-data" = <<-EOT
            #cloud-config
            users:
              - name: devops_user
                groups: sudo
                shell: /bin/bash
                sudo: 'ALL=(ALL) NOPASSWD:ALL'
                ssh-authorized-keys:
                  - ssh-rsa AAAAB3Nza**********************************
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm8716enlkivmdqktas"
        disk_id     = "fhm8716enlkivmdqktas"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd83s8u085j3mq231ago"
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
        mac_address        = "d0:0d:a7:a4:62:72"
        nat                = true
        nat_ip_address     = "84.201.***.***"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bv27imeg76ibb3f9cd"
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

```bash
$ terraform state show yandex_vpc_network.network-1   
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {                                        
    created_at                = "2024-02-28T00:20:21Z"                             
    default_security_group_id = "enp3kirtt4ceob1d6cst"                             
    folder_id                 = "b1gnnf3j8bv1kfirnuq4"                             
    id                        = "enpp88amqva30hnnnhhv"                             
    labels                    = {}                                                 
    name                      = "network1"                                         
    subnet_ids                = [                                                  
        "e9bv27imeg76ibb3f9cd",                                                    
    ]                                                                              
}                        
```

```bash
$ terraform state show yandex_vpc_subnet.subnet-1     
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-28T00:21:34Z"
    folder_id      = "b1gnnf3j8bv1kfirnuq4"
    id             = "e9bv27imeg76ibb3f9cd"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpp88amqva30hnnnhhv"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

```bash
$ terraform output
container_id = "7f50b82ad3a8a14ec3ab95b07c8243560952d785a3d76c169e35a1b0558c20d3"
external_ip_address_vm_1 = "84.201.***.***"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
internal_ip_address_vm_1 = "192.168.10.21"
```
