# Answers to Lab 4

## Outputs for Docker Infrastructure

```bash
terraform state list

docker_container.default
docker_image.default
docker_tag.default
```

```bash
terraform state show docker_container.default
 
# docker_container.default:
resource "docker_container" "default" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "flask",
        "run",
        "--host",
        "0.0.0.0",
        "--port",
        "8080",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "dfc7f8e59f1e"
    id                                          = "dfc7f8e59f1e762fd36f72c43cb5ed3cce4a05c9e63a308898734d83a8f2d79a"
    image                                       = "sha256:a5f437e8b6460d8520d5d16384cd64407cfe6aff4d394708fb5a33b90f2ad220"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devops-flask-app"
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
    working_dir                                 = "/app_python"

    labels {
        label = "description"
        value = "Flask Web Application displaying current time in Moscow"
    }
    labels {
        label = "maintainer"
        value = "rekhlov"
    }

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```bash
terraform state show docker_image.default
 
# docker_image.default:
resource "docker_image" "default" {
    id           = "sha256:a5f437e8b6460d8520d5d16384cd64407cfe6aff4d394708fb5a33b90f2ad220rekhlov/devops-flask-app"
    image_id     = "sha256:a5f437e8b6460d8520d5d16384cd64407cfe6aff4d394708fb5a33b90f2ad220"
    keep_locally = false
    name         = "rekhlov/devops-flask-app"

    build {
        cache_from   = []
        context      = "../../"
        dockerfile   = "Dockerfile"
        extra_hosts  = []
        remove       = true
        security_opt = []
        tag          = []
    }
}
```

```bash
terraform output

container_id = "dfc7f8e59f1e762fd36f72c43cb5ed3cce4a05c9e63a308898734d83a8f2d79a"
```

## Ouput for Github Infrastructure

```bash
terraform state list

github_branch_default.main
github_branch_protection.default
github_repository.S24-core-course-labs
```

```bash
terraform state show github_branch_default.main

# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"c5f535adb555a121057727c98a51d1081894cf03fbee8dcd86dd2d4c5a827f53\""
    id         = "S24-core-course-labs"
    rename     = false
    repository = "S24-core-course-labs"
}
```

```bash
terraform state show github_branch_protection.default

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    enforce_admins                  = false
    id                              = "BPR_kwDOLNvbN84C00K2"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "S24-core-course-labs"
    require_conversation_resolution = false
    require_signed_commits          = false
    required_linear_history         = false
}
```

```bash
terraform state show github_repository.S24-core-course-labs

# github_repository.S24-core-course-labs:
resource "github_repository" "S24-core-course-labs" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Repo with the solutions to S24-DevOps course in Innopolis University"
    etag                        = "W/\"c5f535adb555a121057727c98a51d1081894cf03fbee8dcd86dd2d4c5a827f53\""
    full_name                   = "plov-cyber/S24-core-course-labs"
    git_clone_url               = "git://github.com/plov-cyber/S24-core-course-labs.git"
    gitignore_template          = "Python"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/plov-cyber/S24-core-course-labs"
    http_clone_url              = "https://github.com/plov-cyber/S24-core-course-labs.git"
    id                          = "S24-core-course-labs"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S24-core-course-labs"
    node_id                     = "R_kgDOLNvbNw"
    primary_language            = "Python"
    private                     = false
    repo_id                     = 752606007
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:plov-cyber/S24-core-course-labs.git"
    svn_url                     = "https://github.com/plov-cyber/S24-core-course-labs"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
    web_commit_signoff_required = false

    security_and_analysis {
        secret_scanning {
            status = "disabled"
        }
        secret_scanning_push_protection {
            status = "disabled"
        }
    }
}
```

## Output for Yandex Cloud Infrastructure

```bash
terraform state list

data.template_file.default
data.yandex_compute_image.default
yandex_compute_disk.boot-disk
yandex_compute_instance.default
yandex_vpc_network.default
yandex_vpc_subnet.default
```

```bash
terraform state show data.template_file.default

# data.template_file.default:
data "template_file" "default" {
    id       = "a2ed0dd5d181bc28a4cf2d6960e60e1e9be7eaa33d86370610acf84502f49f55"
    rendered = <<-EOT
        #ps1
        # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux
        
        # logging
        Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
        "Bootstrap script started" | Write-Host
        
        # inserting value's from terraform
        $MyUserName = "rekhlov"
        $MyPlainTextPassword = "12345678"
        if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
            "Create user" | Write-Host
            $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
            $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
            $MyUser | Add-LocalGroupMember -Group 'Administrators'
            $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
        }
        
        # inserting value's from terraform
        $MyAdministratorPlainTextPassword = "87654321"
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
        "admin_pass" = "87654321"
        "user_name"  = "rekhlov"
        "user_pass"  = "12345678"
    }
}
```

```bash
terraform state show data.yandex_compute_image.default

# data.yandex_compute_image.default:
data "yandex_compute_image" "default" {
    created_at    = "2024-02-26T10:55:21Z"
    description   = "centos 7"
    family        = "centos-7"
    folder_id     = "standard-images"
    id            = "fd8p3qkkviv008rkeb83"
    image_id      = "fd8p3qkkviv008rkeb83"
    labels        = {}
    min_disk_size = 10
    name          = "centos-7-v20240226"
    os_type       = "linux"
    pooled        = true
    product_ids   = [
        "f2eo8hihti6h5tcvv773",
    ]
    size          = 2
    status        = "ready"
}
```

```bash
terraform state show yandex_compute_disk.boot-disk    

# yandex_compute_disk.boot-disk:
resource "yandex_compute_disk" "boot-disk" {
    block_size  = 4096
    created_at  = "2024-02-28T07:15:18Z"
    folder_id   = "b1g1cvrjre5nhj5nuthg"
    id          = "fhmqalb0uvrkq4j81fq2"
    image_id    = "fd8p3qkkviv008rkeb83"
    name        = "boot-disk"
    product_ids = [
        "f2eo8hihti6h5tcvv773",
    ]
    size        = 50
    status      = "ready"
    type        = "network-ssd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

```bash
terraform state show yandex_compute_instance.default

# yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    created_at                = "2024-02-28T07:15:26Z"
    folder_id                 = "b1g1cvrjre5nhj5nuthg"
    fqdn                      = "devops.ru-central1.internal"
    hostname                  = "devops"
    id                        = "fhmo5a7vik2kifc70ei6"
    metadata                  = {
        "user-data" = <<-EOT
            #ps1
            # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux
            
            # logging
            Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
            "Bootstrap script started" | Write-Host
            
            # inserting value's from terraform
            $MyUserName = "rekhlov"
            $MyPlainTextPassword = "12345678"
            if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
                "Create user" | Write-Host
                $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
                $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
                $MyUser | Add-LocalGroupMember -Group 'Administrators'
                $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
            }
            
            # inserting value's from terraform
            $MyAdministratorPlainTextPassword = "87654321"
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
    name                      = "devops"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmqalb0uvrkq4j81fq2"
        disk_id     = "fhmqalb0uvrkq4j81fq2"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8p3qkkviv008rkeb83"
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
        ip_address         = "192.168.10.11"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:18:2a:8f:f9"
        nat                = true
        nat_ip_address     = "158.160.126.166"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bvoca4a6g67pmhpafm"
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

```bash
terraform state show yandex_vpc_network.default

# yandex_vpc_network.default:
resource "yandex_vpc_network" "default" {
    created_at                = "2024-02-28T07:15:17Z"
    default_security_group_id = "enp6puh0d753amnvn6p4"
    folder_id                 = "b1g1cvrjre5nhj5nuthg"
    id                        = "enp3jtcv93bce8tr5erb"
    labels                    = {}
    name                      = "ya-network"
    subnet_ids                = []
}
```

```bash
terraform state show yandex_vpc_subnet.default

# yandex_vpc_subnet.default:
resource "yandex_vpc_subnet" "default" {
    created_at     = "2024-02-28T07:15:20Z"
    folder_id      = "b1g1cvrjre5nhj5nuthg"
    id             = "e9bvoca4a6g67pmhpafm"
    labels         = {}
    name           = "ya-network"
    network_id     = "enp3jtcv93bce8tr5erb"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Best Practices Applied in Terraform Files

### Using Required Providers:

The configuration file specifies the required provider "yandex" using the required_providers block. This ensures that
the necessary provider is available before applying the configuration.

### Separating Provider Configuration:

The provider configuration for "yandex" is defined separately from the resources. This separation allows for better
organization and makes it easier to update or change the provider configuration if needed.

### Using Variables:

The configuration file utilizes variables such as var.zone, var.network, var.subnet, etc. Variables make the code more
flexible and reusable, allowing for easier customization and maintenance.

### Defining Resources:

The configuration file defines various resources such as yandex_vpc_network, yandex_vpc_subnet, yandex_compute_disk, and
yandex_compute_instance. This modular approach helps in managing and provisioning infrastructure resources.

### Using Data Sources:

The configuration file includes a data source yandex_compute_image to fetch information about the desired image. Data
sources allow you to retrieve information from external sources and use it in your Terraform configuration.

### Using Templates:

The configuration file uses the template_file data source to render a template file (init.ps1) and pass variables to it.
This allows for dynamic generation of configuration files or scripts.

### Defining Outputs:

The configuration file defines outputs for name and address, which provide information about the created compute
instance. Outputs can be useful for retrieving information from the Terraform state after applying the configuration.
