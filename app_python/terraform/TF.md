# Lab 4

## Outputs for Docker Infrastructure

```bash
terraform state list

docker_container.app_container
docker_image.app_image
docker_tag.app_tag
```

```bash
terraform state show docker_container.app_container

# docker_container.app_container:
resource "docker_container" "app_container" {
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
    hostname                                    = "3d02f68c621c"
    id                                          = "3d02f68c621cec8dca6b52def695436a46ef6fcebf25a5be20a17c7be1149410"
    image                                       = "sha256:2161b0e81c71798fc1a8e98ec14439bb268ee4012f35ad599bf67e620618d952"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "sapushha_flask_app"
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
    user                                        = "sapushha"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    labels {
        label = "description"
        value = "Web Application that displays the current Moscow time"
    }
    labels {
        label = "maintainer"
        value = "sapushha"
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
terraform state show docker_image.app_image

# docker_image.app_image:
resource "docker_image" "app_image" {
    id           = "sha256:2161b0e81c71798fc1a8e98ec14439bb268ee4012f35ad599bf67e620618d952sapushha/sapushha_flask_app"
    image_id     = "sha256:2161b0e81c71798fc1a8e98ec14439bb268ee4012f35ad599bf67e620618d952"
    keep_locally = false
    name         = "sapushha/sapushha_flask_app"

    build {
        cache_from   = []
        context      = "..\\..\\"
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

container_id = "3d02f68c621cec8dca6b52def695436a46ef6fcebf25a5be20a17c7be1149410"
```

## Outputs for Github Infrastructure

```bash
terraform state list

github_branch_default.main
github_branch_protection.default
github_repository.S24-core-course-labs
```

```bash
terraform state show github_branch_protection.default

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    enforce_admins                  = false
    id                              = "BPR_kwDOLN3JHc4C0zVH"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "S24-core-course-labs"
    require_conversation_resolution = false
    require_signed_commits          = false
    required_linear_history         = false
}
```

```bash
terraform state show github_branch_default.main

# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"08f9039c6a73b8abeda501708c636edb8155d67521c3887923c8c4ab7a72e535\""
    id         = "S24-core-course-labs"
    rename     = false
    repository = "S24-core-course-labs"
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
    description                 = "DevOps Engineering Labs"
    etag                        = "W/\"08f9039c6a73b8abeda501708c636edb8155d67521c3887923c8c4ab7a72e535\""
    full_name                   = "sapushha/S24-core-course-labs"
    git_clone_url               = "git://github.com/sapushha/S24-core-course-labs.git"
    gitignore_template          = "Python"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/sapushha/S24-core-course-labs"
    http_clone_url              = "https://github.com/sapushha/S24-core-course-labs.git"
    id                          = "S24-core-course-labs"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S24-core-course-labs"
    node_id                     = "R_kgDOLN3JHQ"
    primary_language            = "Python"
    private                     = false
    repo_id                     = 752732445
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:sapushha/S24-core-course-labs.git"
    svn_url                     = "https://github.com/sapushha/S24-core-course-labs"
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

## Outputs for Yandex Cloud Infrastructure

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
    id       = "44441a3ff2754e3bf6862d18966fb8f44b97579e0bd291eeb3250ab01b119989"
    rendered = <<-EOT
        #ps1
        # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux

        # logging
        Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
        "Bootstrap script started" | Write-Host

        # inserting value's from terraform
        $MyUserName = "sapushha"
        $MyPlainTextPassword = "sapushha"
        if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
            "Create user" | Write-Host
            $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
            $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
            $MyUser | Add-LocalGroupMember -Group 'Administrators'
            $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
        }

        # inserting value's from terraform
        $MyAdministratorPlainTextPassword = "sapushha"
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
        "admin_pass" = "sapushha"
        "user_name"  = "sapushha"
        "user_pass"  = "sapushha"
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
    created_at  = "2024-02-28T04:17:47Z"
    folder_id   = "b1g1cvrjre5nhj5nuthg"
    id          = "fhmkvosnp7pikg4ck51b"
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
    created_at                = "2024-02-28T04:17:53Z"
    folder_id                 = "b1g1cvrjre5nhj5nuthg"
    fqdn                      = "test.ru-central1.internal"
    hostname                  = "test"
    id                        = "fhmlv9st1tfha50uni18"
    metadata                  = {
        "user-data" = <<-EOT
            #ps1
            # ^^^ 'ps1' is only for cloudbase-init, some sort of sha-bang in linux

            # logging
            Start-Transcript -Path "$ENV:SystemDrive\provision.txt" -IncludeInvocationHeader -Force
            "Bootstrap script started" | Write-Host

            # inserting value's from terraform
            $MyUserName = "sapushha"
            $MyPlainTextPassword = "sapushha"
            if (-not [string]::IsNullOrEmpty($MyUserName) -and -not [string]::IsNullOrEmpty($MyPlainTextPassword)) {
                "Create user" | Write-Host
                $MyPassword = $MyPlainTextPassword | ConvertTo-SecureString -AsPlainText -Force
                $MyUser = New-LocalUser -Name $MyUserName -Password $MyPassword -PasswordNeverExpires -AccountNeverExpires
                $MyUser | Add-LocalGroupMember -Group 'Administrators'
                $MyUser | Add-LocalGroupMember -Group 'Remote Management Users'
            }

            # inserting value's from terraform
            $MyAdministratorPlainTextPassword = "sapushha"
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
    name                      = "test"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmkvosnp7pikg4ck51b"
        disk_id     = "fhmkvosnp7pikg4ck51b"
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
        ip_address         = "192.168.10.27"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:15:fa:79:d0"
        nat                = true
        nat_ip_address     = "158.160.37.209"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9br2l1dbd7a81808l9a"
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
    created_at                = "2024-02-28T04:17:47Z"
    default_security_group_id = "enpvftvok5q7e75dk442"
    folder_id                 = "b1g1cvrjre5nhj5nuthg"
    id                        = "enpt0t2pi30ttnh5o6eu"
    labels                    = {}
    name                      = "ya-network"
    subnet_ids                = []
}
```

```bash
terraform state show yandex_vpc_subnet.default

# yandex_vpc_subnet.default:
resource "yandex_vpc_subnet" "default" {
    created_at     = "2024-02-28T04:17:49Z"
    folder_id      = "b1g1cvrjre5nhj5nuthg"
    id             = "e9br2l1dbd7a81808l9a"
    labels         = {}
    name           = "ya-network"
    network_id     = "enpt0t2pi30ttnh5o6eu"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Best Practices I applied

### Version Constraints:

The terraform block includes a version constraint for the docker provider,
specifying that version ~> 3.0.1 is required. This ensures compatibility and
allows Terraform to automatically select compatible provider versions within
the specified range.

### Separate Provider Configuration:

The provider configuration for docker is placed in a separate block, improving
readability and maintainability of the Terraform configuration.

### Descriptive Resource Names:

The resource names docker_image.app_image, docker_container.app_container, and
docker_tag.app_tag are descriptive and provide clear indications of their
purpose. This improves the readability and understandability of the Terraform
configuration.

### Relative Paths:

The context parameter in the docker_image resource uses a relative path (
..\\..\\) to specify the build context. Using relative paths instead of
absolute paths ensures portability across different environments.

### Resource Dependencies:

The docker_container.app_container resource depends on the
docker_image.app_image resource. This ensures that the image is built before
the container is created, maintaining the correct order of resource creation.

### Resource Variables:

The docker_container.app_container resource references the
docker_image.app_image.name variable to specify the image. This allows passing
information between resources and ensures consistency.
