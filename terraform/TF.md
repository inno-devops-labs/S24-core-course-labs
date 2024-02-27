# Terraform
## With Docker
I followed this [guide](https://developer.hashicorp.com/terraform/tutorials/docker-get-started)

### Initial

First output of `terraform show` command:

```
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
    hostname                                    = "fefaac17d60f"
    id                                          = "fefaac17d60fb29a8e2a1551d592d2b0caa50dc55ebdf1b7b1844f1548ccd7da"
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

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

First output of `terraform state list` command:

```
docker_container.nginx
docker_image.nginx
```

### Change infrastructure

**I changed port `8000` to `8080`**:

Part of output of `terraform show` after changes:

```
    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

### Add Variables and Outputs
I added name of container as a variable. In order to do so, I had to create `variables.tf` file and change a line in `main.tf`:

```
  name  = var.container_name
```

Name of docker container was changed, too. `docker ps`:
```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
8c38481ed651   e4720093a3c1   "/docker-entrypoint.…"   29 seconds ago   Up 28 seconds   0.0.0.0:8080->80/tcp   ExampleNginxContainer
```

I added outputs - ids of docker image and container `terraform output`:
```
container_id = "8c38481ed65112ec9e2cb3e181fde2f92742cab2a064e86f6579ba0417b1579f"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
```

## With cloud

I used Yandex cloud form this [guide](https://cloud.yandex.ru/docs/tutorials/infrastructure-management/terraform-quickstart)

Initial `terraform show`:
```
# data.template_file.default:
data "template_file" "default" {
    id       = "439c712299e7e8cbdc85ba356590969ae8dc685ac36982938b2699a0c851627b"
    rendered = <<-EOT
        #ps1
        # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux

        # logging
        Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
        "Bootstrap script started" | Write-Host

        # inserting value's from terraform
        $MyUserName = ""
        $MyPlainTextPassword = ""
        if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
            "Create user" | Write-Host
            $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
            $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
            $MyUser | Add-LocalGroupMember -Group 'Administrators'
            $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
        }

        # inserting value's from terraform
        $MyAdministratorPlainTextPassword = ""
        if (-not [string]::IsNullOrEmpty($MyAdministratorPlainTextPassword)) {
            "Set local administrator password" | Write-Host
            $MyAdministratorPassword = $MyAdministratorPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
            # S-1-5-21domain-500 is a well-known SID for Administrator
            # https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows
            $MyAdministrator = Get-LocalUser | Where-Object -Property "SID" -like "S-1-5-21-*-500"
            $MyAdministrator | Set-LocalUser -Password $MyAdministratorPassword
        }

        "Bootstrap script ended" | Write-Host
    EOT
    template = <<-EOT
        #ps1
        # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux

        # logging
        Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
        "Bootstrap script started" | Write-Host

        # inserting value's from terraform
        $MyUserName = "${ user_name }"
        $MyPlainTextPassword = "${ user_pass }"
        if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
            "Create user" | Write-Host
            $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
            $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
            $MyUser | Add-LocalGroupMember -Group 'Administrators'
            $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
        }

        # inserting value's from terraform
        $MyAdministratorPlainTextPassword = "${ admin_pass }"
        if (-not [string]::IsNullOrEmpty($MyAdministratorPlainTextPassword)) {
            "Set local administrator password" | Write-Host
            $MyAdministratorPassword = $MyAdministratorPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
            # S-1-5-21domain-500 is a well-known SID for Administrator
            # https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/security-identifiers-in-windows
            $MyAdministrator = Get-LocalUser | Where-Object -Property "SID" -like "S-1-5-21-*-500"
            $MyAdministrator | Set-LocalUser -Password $MyAdministratorPassword
        }

        "Bootstrap script ended" | Write-Host
    EOT
    vars     = {
        "admin_pass" = ""
        "user_name"  = ""
        "user_pass"  = ""
    }
}

# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-27T23:14:27Z"
    folder_id   = "b1g1g3o13qjhhu3gptpj"
    id          = "fhmttrfqc2rdgbo9dhdj"
    image_id    = "fd83s8u085j3mq231ago"
    labels      = {}
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

# yandex_compute_image.default:
resource "yandex_compute_image" "default" {
    created_at    = "2024-02-27T23:12:36Z"
    folder_id     = "b1g1g3o13qjhhu3gptpj"
    id            = "fd8nrunseebc01gagpq2"
    labels        = {}
    min_disk_size = 3
    pooled        = false
    product_ids   = [
        "f2ejqncm1j4oqo7g92da",
    ]
    size          = 2
    source_family = "ubuntu-1804-lts"
    status        = "ready"
}

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    allow_stopping_for_update = true
    created_at                = "2024-02-27T23:15:29Z"
    folder_id                 = "b1g1g3o13qjhhu3gptpj"
    fqdn                      = "fhmr3ggl87qhia1s7i9s.auto.internal"
    id                        = "fhmr3ggl87qhia1s7i9s"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHHyfPLcGeqgONjgTgi1Pe407pYwSKvpDHQpfyrE7dDI zhuko@rostislavpc
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v2"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmttrfqc2rdgbo9dhdj"
        disk_id     = "fhmttrfqc2rdgbo9dhdj"
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
        ip_address         = "192.168.10.3"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1b:1c:21:54"
        nat                = true
        nat_ip_address     = "51.250.81.108"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bvid19nm1m1hore8ko"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 5
        cores         = 2
        gpus          = 0
        memory        = 1
    }

    scheduling_policy {
        preemptible = true
    }
}

# yandex_vpc_network.default:
resource "yandex_vpc_network" "default" {
    created_at                = "2024-02-27T23:12:36Z"
    default_security_group_id = "enpfhgc5hbh1an5206j7"
    folder_id                 = "b1g1g3o13qjhhu3gptpj"
    id                        = "enp1aqk6q320nhul5d82"
    labels                    = {}
    name                      = "ya-network"
    subnet_ids                = [
        "e9bvid19nm1m1hore8ko",
    ]
}

# yandex_vpc_subnet.default:
resource "yandex_vpc_subnet" "default" {
    created_at     = "2024-02-27T23:12:38Z"
    folder_id      = "b1g1g3o13qjhhu3gptpj"
    id             = "e9bvid19nm1m1hore8ko"
    labels         = {}
    name           = "ya-network"
    network_id     = "enp1aqk6q320nhul5d82"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}


Outputs:

external_ip_address_vm_1 = "51.250.81.108"
internal_ip_address_vm_1 = "192.168.10.3"
```
