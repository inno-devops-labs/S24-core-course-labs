# Terraform lab

## Docker infrastructure command outputs

As a result of building infrastructure, the container was built and launched and port 5000 was exposed to the host.

### terraform state list

```
docker_container.time-server
docker_image.flask-time-server
```

### terraform state show docker_container.time-server

```
# docker_container.time-server:
resource "docker_container" "time-server" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "python3",
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "5f5c4d3383f8"
    id                                          = "5f5c4d3383f8ad75e81c25799d2fe37afbc2f822381dc3d0b81ed106ec49962b"
    image                                       = "sha256:77b57d2f57258f29e52b28055c2a13888cdca6b0848da3a9aaa362736d5547a2"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "time-server"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
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
    stop_signal                                 = null
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "server"
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### terraform state show docker_image.flask-time-server

```
# docker_image.flask-time-server:
resource "docker_image" "flask-time-server" {
    id           = "sha256:77b57d2f57258f29e52b28055c2a13888cdca6b0848da3a9aaa362736d5547a2qexik1/flask-time-server"
    image_id     = "sha256:77b57d2f57258f29e52b28055c2a13888cdca6b0848da3a9aaa362736d5547a2"
    keep_locally = false
    name         = "qexik1/flask-time-server"
    repo_digest  = "qexik1/flask-time-server@sha256:77b57d2f57258f29e52b28055c2a13888cdca6b0848da3a9aaa362736d5547a2"
}
```

### terraform output

```
container_id = {
  "attach" = false
  "bridge" = ""
  "capabilities" = toset([])
  "cgroupns_mode" = tostring(null)
  "command" = tolist([
    "python3",
    "main.py",
  ])
  "container_logs" = tostring(null)
  "container_read_refresh_timeout_milliseconds" = 15000
  "cpu_set" = ""
  "cpu_shares" = 0
  "destroy_grace_seconds" = tonumber(null)
  "devices" = toset([])
  "dns" = toset(null) /* of string */
  "dns_opts" = toset(null) /* of string */
  "dns_search" = toset(null) /* of string */
  "domainname" = ""
  "entrypoint" = tolist([])
  "env" = toset([])
  "exit_code" = tonumber(null)
  "gpus" = tostring(null)
  "group_add" = toset(null) /* of string */
  "healthcheck" = tolist(null) /* of object */
  "host" = toset([])
  "hostname" = "5f5c4d3383f8"
  "id" = "5f5c4d3383f8ad75e81c25799d2fe37afbc2f822381dc3d0b81ed106ec49962b"
  "image" = "sha256:77b57d2f57258f29e52b28055c2a13888cdca6b0848da3a9aaa362736d5547a2"
  "init" = false
  "ipc_mode" = "private"
  "labels" = toset([])
  "log_driver" = "json-file"
  "log_opts" = tomap(null) /* of string */
  "logs" = false
  "max_retry_count" = 0
  "memory" = 0
  "memory_swap" = 0
  "mounts" = toset([])
  "must_run" = true
  "name" = "time-server"
  "network_data" = tolist([
    {
      "gateway" = "172.17.0.1"
      "global_ipv6_address" = ""
      "global_ipv6_prefix_length" = 0
      "ip_address" = "172.17.0.2"
      "ip_prefix_length" = 16
      "ipv6_gateway" = ""
      "mac_address" = "02:42:ac:11:00:02"
      "network_name" = "bridge"
    },
  ])
  "network_mode" = "bridge"
  "networks_advanced" = toset([])
  "pid_mode" = ""
  "ports" = tolist([
    {
      "external" = 5000
      "internal" = 5000
      "ip" = "0.0.0.0"
      "protocol" = "tcp"
    },
  ])
  "privileged" = false
  "publish_all_ports" = false
  "read_only" = false
  "remove_volumes" = true
  "restart" = "no"
  "rm" = false
  "runtime" = "runc"
  "security_opts" = toset([])
  "shm_size" = 64
  "start" = true
  "stdin_open" = false
  "stop_signal" = ""
  "stop_timeout" = 0
  "storage_opts" = tomap(null) /* of string */
  "sysctls" = tomap(null) /* of string */
  "tmpfs" = tomap(null) /* of string */
  "tty" = false
  "ulimit" = toset([])
  "upload" = toset([])
  "user" = "server"
  "userns_mode" = ""
  "volumes" = toset([])
  "wait" = false
  "wait_timeout" = 60
  "working_dir" = "/app_python"
}
image_id = {
  "build" = toset([])
  "force_remove" = tobool(null)
  "id" = "sha256:77b57d2f57258f29e52b28055c2a13888cdca6b0848da3a9aaa362736d5547a2qexik1/flask-time-server"
  "image_id" = "sha256:77b57d2f57258f29e52b28055c2a13888cdca6b0848da3a9aaa362736d5547a2"
  "keep_locally" = false
  "name" = "qexik1/flask-time-server"
  "platform" = tostring(null)
  "pull_triggers" = toset(null) /* of string */
  "repo_digest" = "qexik1/flask-time-server@sha256:77b57d2f57258f29e52b28055c2a13888cdca6b0848da3a9aaa362736d5547a2"
  "triggers" = tomap(null) /* of string */
}
```

## Yandex infrastructure command outputs

As a result of building infrastructure, the VM was created together with disk and network.

### terraform state list

```
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm1
yandex_vpc_network.test_net
yandex_vpc_subnet.test_subnet
```

### terraform state show yandex_compute_disk.boot-disk-1

```
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-11-10T17:27:38Z"
    description = null
    folder_id   = "b1gdudeqj0m8a31489ln"
    id          = "fhmt06fbfvobql201j37"
    image_id    = "fd84kd8dcu6tmnhbeebv"
    name        = "boot-disk-1"
    product_ids = [
        "f2ejh6htghf0mu0ope58",
    ]
    size        = 10
    snapshot_id = null
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {
        disk_placement_group_id = null
    }

    hardware_generation {
        legacy_features {
            pci_topology = "PCI_TOPOLOGY_V1"
        }
    }
}
```

### terraform state show yandex_compute_instance.vm1

```
# yandex_compute_instance.vm1:
resource "yandex_compute_instance" "vm1" {
    created_at                = "2024-11-10T17:27:51Z"
    description               = null
    folder_id                 = "b1gdudeqj0m8a31489ln"
    fqdn                      = "fhmp675p0rcdq3cp05sn.auto.internal"
    gpu_cluster_id            = null
    hardware_generation       = [
        {
            generation2_features = []
            legacy_features      = [
                {
                    pci_topology = "PCI_TOPOLOGY_V1"
                },
            ]
        },
    ]
    hostname                  = null
    id                        = "fhmp675p0rcdq3cp05sn"
    maintenance_grace_period  = null
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAMm6AucyoU8mPzodDSVzwl4SAT2C8qvF1EhT21ChqQ3 <optional_comment>
        EOT
    }
    name                      = "terraform-time-server"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    service_account_id        = null
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmt06fbfvobql201j37"
        disk_id     = "fhmt06fbfvobql201j37"
        mode        = "READ_WRITE"

        initialize_params {
            block_size  = 4096
            description = null
            image_id    = "fd84kd8dcu6tmnhbeebv"
            name        = "boot-disk-1"
            size        = 10
            snapshot_id = null
            type        = "network-hdd"
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
        ip_address         = "10.130.0.9"
        ipv4               = true
        ipv6               = false
        ipv6_address       = null
        mac_address        = "d0:0d:19:31:cb:90"
        nat                = false
        nat_ip_address     = null
        nat_ip_version     = null
        security_group_ids = []
        subnet_id          = "e9b6cj82k9sks39ltljp"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_id        = null
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

### terraform state show yandex_vpc_network.test_net

```
# yandex_vpc_network.test_net:
resource "yandex_vpc_network" "test_net" {
    created_at                = "2024-11-10T17:27:38Z"
    default_security_group_id = "enpo9vg8c47ekngfdmam"
    description               = null
    folder_id                 = "b1gdudeqj0m8a31489ln"
    id                        = "enp3e9c5re18m1rbrrf9"
    labels                    = {}
    name                      = "test_network"
    subnet_ids                = []
}
```

### terraform state show yandex_vpc_subnet.test_subnet

```
# yandex_vpc_subnet.test_subnet:
resource "yandex_vpc_subnet" "test_subnet" {
    created_at     = "2024-11-10T17:27:42Z"
    description    = null
    folder_id      = "b1gdudeqj0m8a31489ln"
    id             = "e9b6cj82k9sks39ltljp"
    labels         = {}
    name           = null
    network_id     = "enp3e9c5re18m1rbrrf9"
    route_table_id = null
    v4_cidr_blocks = [
        "10.130.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Best practices

During the lab I applied some best practices on Terraform, including:

1. Not exposing my secrets to the public
2. Using variables.tf file instead of hardcoding values into main.tf

