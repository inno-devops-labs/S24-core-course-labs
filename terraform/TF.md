# Terraform

## Terraform best practices

* Separate terraform files by their responsibility: providers, variables, network, outputs, etc.
* Split files by scopes of work (GitHub, Cloud, Docker)
* Preserve one variable naming style (e.g. snake_case)
* Use `terraform fmt` to keep configs consistent
* Use `terraform validate` to keep configs correct

## Docker

### Terraform state list

```shell
(venv) shredding@SHREDDING-2 docker % terraform state list

docker_container.nginx
docker_image.nginx
```

### Terraform state show

```shell
(venv) shredding@SHREDDING-2 docker % terraform state show docker_container.nginx
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
    hostname                                    = "0ee72062e62a"
    id                                          = "0ee72062e62aa72c19999b7f0ebcee3a9d25662920c0784510060eb86529b6ef"
    image                                       = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676"
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

### Terraform outputs
```shell
(venv) shredding@SHREDDING-2 docker % terraform output                           
container_id = "0ee72062e62aa72c19999b7f0ebcee3a9d25662920c0784510060eb86529b6ef"
image_id = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676nginx:latest"
```

## YandexCloud
As russian credit cards are restricted in AWS, i decided to use YandexCLoud. 

### Init terraform:
```
terraform init -backend-config="access_key=$ACCESS_KEY"-backend-config="secret_key=$SECRET_KEY"
```
### Apply terraform:
```
terraform apply -var="cloud_id=$YC_CLOUD_ID" -var="folder_id=$YC_CATALOG_ID" -var="service_account_key_file=$YC_KEY_PATH"
```

### terraform state list

Output:
```
yandex_compute_image.ubuntu_2004
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### terraform show

Output:
```
# yandex_compute_image.ubuntu_2004:
resource "yandex_compute_image" "ubuntu_2004" {
    created_at    = "2023-09-26T11:18:46Z"
    folder_id     = "b1gqtkcc8ktga62edqu6"
    id            = "fd8m4rsmq1h574oau0as"
    min_disk_size = 5
    pooled        = false
    product_ids   = [
        "f2ed6k5slaamr94lfdqu",
    ]
    size          = 4
    source_family = "ubuntu-2004-lts"
    status        = "ready"
}

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2023-09-26T11:18:58Z"
    folder_id                 = "b1gqtkcc8ktga62edqu6"
    fqdn                      = "fhmcm18frvk6i0dhpd5g.auto.internal"
    id                        = "fhmcm18frvk6i0dhpd5g"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBg7zb98jwHYj0WUX13c9mYdzNqf5GWAjypJxwvak4S3 shredding@SHREDDING-2.local
        EOT
    }
    name                      = "terraform1"
        network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm4m7b9iak2hil0gv1i"
        disk_id     = "fhm4m7b9iak2hil0gv1i"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8m4rsmq1h574oau0as"
            size       = 5
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
        mac_address        = "d0:0d:cb:05:0f:df"
        nat                = true
        nat_ip_address     = "158.160.120.130"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b2fo6cn6loi08v5mn7"
    }

    placement_policy {
        host_affinity_rules = []
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

# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2023-09-26T10:22:51Z"
    default_security_group_id = "enp1q2cplpnm3cn3m5sv"
    folder_id                 = "b1gqtkcc8ktga62edqu6"
    id                        = "enptm3esh55lj9e46c8m"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9b2fo6cn6loi08v5mn7",
    ]
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2023-09-26T10:22:55Z"
    folder_id      = "b1gqtkcc8ktga62edqu6"
    id             = "e9b2fo6cn6loi08v5mn7"
    labels         = {}
    name           = "subnet1"
    network_id     = "enptm3esh55lj9e46c8m"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

### terraform output 

Output:
```
external_ip_address_vm_1 = "158.160.60.155"
internal_ip_address_vm_1 = "192.168.10.33"

```


## GitHub

### Terraform import

```shell
(venv) shredding@SHREDDING-2 github %  terraform import "github_repository.terraform" "devops-terraform"
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.terraform: Importing from ID "devops-terraform"...
github_repository.terraform: Import prepared!
  Prepared github_repository for import
github_repository.terraform: Refreshing state... [id=devops-terraform]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```