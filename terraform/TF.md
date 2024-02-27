# Best practices

1. Variables: I use almost every value in variable
2. Outputs: I set proper outputs where it is needed
3. Use Terraform plan before apply: This allows me to review and confirm the changes before applying them

## Docker

To run:

```bash
terraform apply
```

Result of `terraform state list`:

```text
docker_container.app
docker_image.app
```

Result of `terraform state show docker_container.app`:

```text
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = [
        "python",
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "c54e0835f42f"
    id                                          = "c54e0835f42f1a3ef8f51e8c317bdc5b532e6aa58963ead20f38af54267ab15d"
    image                                       = "sha256:1d6a5efaab9a6e2dc39c43deab7ec7fd86874911d5e3cfa0146be4024c7dbba1"
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
    user                                        = "myuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

Result of `terraform output`:

```text
container_id = "c54e0835f42f1a3ef8f51e8c317bdc5b532e6aa58963ead20f38af54267ab15d"
image_id = "sha256:1d6a5efaab9a6e2dc39c43deab7ec7fd86874911d5e3cfa0146be4024c7dbba1pgrammer/app_python:latest"
```

## Yandex Cloud

Result of `terraform state list`

```text
yandex_compute_disk.boot-disk
yandex_compute_image.default
yandex_compute_instance.vm
yandex_vpc_network.yc-network
yandex_vpc_subnet.subnet-1
```

Result of `terraform state show yandex_compute_instance.vm`

```text
# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2024-02-27T21:44:43Z"
    folder_id                 = "b1gv4t2t9ahap1g9phga"
    fqdn                      = "fhmmitepbb91cik59ouf.auto.internal"
    id                        = "fhmmitepbb91cik59ouf"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAnOOQ+Ncp1VdPHjQgxJp7D7a/bb+YHasDkX7UrpFSaC anron@anron-vivobookasuslaptopm3500qam3500qa
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmubhfkseh1lhv2q0fs"
        disk_id     = "fhmubhfkseh1lhv2q0fs"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8bihd0ret6ui88lle3"
            name       = "boot-disk"
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
        ip_address         = "192.168.10.3"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:16:97:5d:95"
        nat                = true
        nat_ip_address     = "51.250.12.85"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bhdhvspq1sfohkur4s"
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

Result of `terraform output`:

```text
external_ip_address_vm = "51.250.12.85"
internal_ip_address_vm = "192.168.10.3"
```

## GitHub

Result of `terraform import "github_repository.repo" "S24-DevOps-labs-test"`:

```text
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Importing from ID "S24-DevOps-labs-test"...
github_repository.repo: Import prepared!

  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=S24-DevOps-labs-test]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

