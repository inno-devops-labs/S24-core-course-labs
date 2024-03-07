# Docker Infrastructure with Terraform

## Show Docker Image State:
```terrraform state show docker_image.nginx```

`docker_image.nginx`:
```
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

## Show Docker Container State:
```terraform state show docker_container.nginx```

`docker_container.nginx`:
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
    hostname                                    = "e1d127f1a68d"
    id                                          = "e1d127f1a68d685ca6f77bb4ad5fbaa6f89f62457b21847768bbd33e2dce8ffc"
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
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:03"
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

## Show Docker Network State:
```terraform state show docker_network.nginx```
```terraform state list```
docker_container.nginx
docker_image.nginx

## Apply Terraform:
```terraform apply```
```
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
      + name         = "nginx"
      + repo_digest  = (known after apply)

Plan: 2 to add, 0 to change, 0 to destroy.
```

## Show Terraform Output:
```terraform output```
```
container_id = "0a2af269a767e3e74b3eee8ebb55d583ac621fc99a1a0e4e3d2cc07439e1e4ae"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
```

# Yandex Cloud Setting

`terraform state list`
```
data.template_file.default
yandex_compute_disk.boot-disk
yandex_compute_image.default
yandex_compute_instance.default
yandex_vpc_network.default
yandex_vpc_subnet.default
```

`terraform state show yandex_compute_image.default`
```
# yandex_compute_image.default:
resource "yandex_compute_image" "default" {
    created_at    = "2024-02-27T20:45:47Z"
    folder_id     = "b1grh1oiajrordvcn1c6"
    id            = "fd8f8hfn3tggpnj5h5q8"
    min_disk_size = 3
    pooled        = false
    product_ids   = [
        "f2ejqncm1j4oqo7g92da",
    ]
    size          = 2
    source_family = "ubuntu-1804-lts"
    status        = "ready"
}
```

`terraform state show yandex_compute_instance.default`
```
# yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    created_at                = "2024-02-27T20:46:14Z"
    folder_id                 = "b1grh1oiajrordvcn1c6"
    fqdn                      = "fhm4pcfbhkp1qrjgt8v0.auto.internal"
    id                        = "fhm4pcfbhkp1qrjgt8v0"
    metadata                  = {
        "user-data" = <<-EOT
            #ps1
            # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux

            # logging
            Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
            "Bootstrap script started" | Write-Host

            # inserting value's from terraform
            $MyUserName = "user-katykosh"
            $MyPlainTextPassword = "password1"
            if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
                "Create user" | Write-Host
                $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
                $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
                $MyUser | Add-LocalGroupMember -Group 'Administrators'
                $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
            }

            # inserting value's from terraform
            $MyAdministratorPlainTextPassword = "password2"
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
    }
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmucd288qa1j7qgakfv"
        disk_id     = "fhmucd288qa1j7qgakfv"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8f8hfn3tggpnj5h5q8"
            name       = "boot-disk"
            size       = 50
            type       = "network-ssd"
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
        ip_address         = "192.168.10.20"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:4c:b1:eb:8d"
        nat                = true
        nat_ip_address     = "84.201.158.25"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9besct6odu86quus7vm"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }

    timeouts {
        create = "10m"
        delete = "10m"
    }
}
```

`terraform state show yandex_vpc_network.default`  
```
# yandex_vpc_network.default:
resource "yandex_vpc_network" "default" {
    created_at                = "2024-02-27T20:45:47Z"
    default_security_group_id = "enpasli6engjnq3s53bm"
    folder_id                 = "b1grh1oiajrordvcn1c6"
    id                        = "enp93nur0ouav9fvm4mh"
    labels                    = {}
    name                      = "ya-network"
    subnet_ids                = []
}
```

`terraform state show yandex_vpc_subnet.default`
```
# yandex_vpc_subnet.default:
resource "yandex_vpc_subnet" "default" {
    created_at     = "2024-02-27T20:45:49Z"
    folder_id      = "b1grh1oiajrordvcn1c6"
    id             = "e9besct6odu86quus7vm"
    labels         = {}
    name           = "ya-network"
    network_id     = "enp93nur0ouav9fvm4mh"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

`terraform output`

```address = "84.201.158.25"```

# Terraform-related best practices

1. **Modularization**: The Terraform code is divided into separate files (`main.tf`, `variables.tf`, `terraform.tfvars`) based on their purpose. This makes the code easier to understand and maintain.

2. **Use of Variables**: Variables are used extensively in the Terraform code. This allows for code reusability and makes it easier to make changes in the future.

3. **Sensitive Data Handling**: Sensitive data like passwords are stored in the `terraform.tfvars` file. This is a good practice as it separates sensitive data from the main code.

4. **Use of Outputs**: The `main.tf` file includes output variables. This is a good practice as it allows you to easily access important data about your resources after they have been created.

5. **Explicit Provider Versioning**: The `required_providers` block in the `main.tf` file specifies the source of the provider. This is a good practice as it ensures that the correct provider is used.

6. **Resource Naming**: Resources are given meaningful names, which makes it easier to understand what each resource is for.

7. **Timeout Settings**: The `timeout_create` and `timeout_delete` variables are used to specify timeouts for resource creation and deletion. This is a good practice as it can prevent Terraform operations from hanging indefinitely.

8. **Use of Data Sources**: The `data` block is used to fetch data about existing resources. This is a good practice as it allows you to use data from outside of Terraform in your configuration.

9. **Documentation**: The `TF.md` file includes detailed documentation about the Terraform code, including how to view the state of resources and how to apply the configuration. This is a good practice as it makes it easier for others to understand and use your code.
