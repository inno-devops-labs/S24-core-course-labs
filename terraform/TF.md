# Terraform

## Docker Tutorial

### Command Outputs

``terraform show``:

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
    hostname                                    = "cdb17a42db24"
    id                                          = "cdb17a42db2433a5a7641ba1894167c6de8b7edd5255537528e5323f509dd460"
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
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

``terraform state list``:

```
docker_container.nginx
docker_image.nginx
```

### Applied changes

```
docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Refreshing state... [id=cdb17a42db2433a5a7641ba1894167c6de8b7edd5255537528e5323f509dd460]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
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
      ~ hostname                                    = "cdb17a42db24" -> (known after apply)
      ~ id                                          = "cdb17a42db2433a5a7641ba1894167c6de8b7edd5255537528e5323f509dd460" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "tutorial"
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

      ~ ports {
          ~ external = 8000 -> 8080 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=cdb17a42db2433a5a7641ba1894167c6de8b7edd5255537528e5323f509dd460]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=8a85cccf67edd2f1fe32e9aa6a40f660bed2b94cf099b9effd9248ea46d6950c]
```

### Output

``terraform output``: 
```
container_id = "6800859a59d4e887d675001e5004ffa141d40b7f13b31fe44f0fbe3eb361df67"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## Yandex Cloud Provider

### Command Outputs

``terraform show``:

```
# module.app_python.docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "flask",
        "run",
        "--host=0.0.0.0",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "cb3eac873fc4"
    id                                          = "cb3eac873fc4063b51cbd49877b7fe9553e26c151b2ab287694c64d15d304caa"
    image                                       = "sha256:9f06d1166631dbbe9737250437b33a4d3667848ef8bfff7f41ed9694944f95ee"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app"
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
    rm                                          = true
    runtime                                     = "runc"
    security_opts                               = []
    shm_size                                    = 64
    start                                       = true
    stdin_open                                  = false
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "flaskuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 300
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# module.app_python.docker_image.img:
resource "docker_image" "img" {
    id           = "sha256:9f06d1166631dbbe9737250437b33a4d3667848ef8bfff7f41ed9694944f95eeevsey/flask-moscow-time-app"
    image_id     = "sha256:9f06d1166631dbbe9737250437b33a4d3667848ef8bfff7f41ed9694944f95ee"
    keep_locally = false
    name         = "evsey/flask-moscow-time-app"
    repo_digest  = "evsey/flask-moscow-time-app@sha256:f580f3506ccbf409685d89fe3ba7a3685c165b622fe0c6fec389617fa06114a2"
}
# module.github.github_branch_default.core_main:
resource "github_branch_default" "core_main" {
    branch     = "main"
    id         = "devops-test"
    rename     = false
    repository = "devops-test"
}

# module.github.github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "devops-repo"
    rename     = false
    repository = "devops-repo"
}

# module.github.github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    force_push_bypassers            = []
    id                              = "BPR_kwDOLYzscs4C0vNt"
    lock_branch                     = false
    pattern                         = "main"
    push_restrictions               = []
    repository_id                   = "devops-repo"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        dismissal_restrictions          = []
        pull_request_bypassers          = []
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}

# module.github.github_repository.core:
resource "github_repository" "core" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "core repository"
    etag                        = "W/\"bdc97f373be277fa31810918124da373df61d27d7a31af22db036a53cffb19a5\""
    full_name                   = "evsey9/devops-test"
    git_clone_url               = "git://github.com/evsey9/devops-test.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/evsey9/devops-test"
    http_clone_url              = "https://github.com/evsey9/devops-test.git"
    id                          = "devops-test"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-test"
    node_id                     = "R_kgDOLYzsgQ"
    private                     = false
    repo_id                     = 764210305
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:evsey9/devops-test.git"
    svn_url                     = "https://github.com/evsey9/devops-test"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false

    security_and_analysis {
        secret_scanning {
            status = "disabled"
        }
        secret_scanning_push_protection {
            status = "disabled"
        }
    }
}

# module.github.github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = false
    allow_squash_merge          = false
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "devops lab repo"
    etag                        = "W/\"18c24cc57a87940824787dff6b3cfe6799efc96015560d39de63cb628c9ea2ea\""
    full_name                   = "evsey9/devops-repo"
    git_clone_url               = "git://github.com/evsey9/devops-repo.git"
    gitignore_template          = "VisualStudio"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/evsey9/devops-repo"
    http_clone_url              = "https://github.com/evsey9/devops-repo.git"
    id                          = "devops-repo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-repo"
    node_id                     = "R_kgDOLYzscg"
    private                     = false
    repo_id                     = 764210290
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:evsey9/devops-repo.git"
    svn_url                     = "https://github.com/evsey9/devops-repo"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false

    security_and_analysis {
        secret_scanning {
            status = "disabled"
        }
        secret_scanning_push_protection {
            status = "disabled"
        }
    }
}
# module.yandex_cloud.data.template_file.default:
data "template_file" "default" {
    id       = "8d608f838d919be7823a4d0b3db6fbf7e56a3ee178939013e113352d36eec2b3"
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

# module.yandex_cloud.yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-27T17:40:29Z"
    folder_id   = "b1g8aian1v2o5fmf9tsh"
    id          = "fhm5393k4mt5cimedmqr"
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

# module.yandex_cloud.yandex_compute_image.default:
resource "yandex_compute_image" "default" {
    created_at    = "2024-02-27T17:40:29Z"
    folder_id     = "b1g8aian1v2o5fmf9tsh"
    id            = "fd81uojalf2rcuc9fd02"
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

# module.yandex_cloud.yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    allow_stopping_for_update = true
    created_at                = "2024-02-27T17:40:34Z"
    folder_id                 = "b1g8aian1v2o5fmf9tsh"
    fqdn                      = "fhmdbk29dfa8oi5kd0j0.auto.internal"
    id                        = "fhmdbk29dfa8oi5kd0j0"
    labels                    = {}
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDYiasYlsX6qTvltjCWAHpJwICclWZQMyztDK3djyEoGbcKKvIGRH4xS8zonGAD1I5z9BYCx0M80E27pgheeTf/hsi5odbs/RO+9plEeEjs6oVTdvkq1Jg26RFwJDtRUJlLfDlQo7MyA8UWFgjEwpFQ9y1aP/lC/FyvXS/AKHZCuBSjPAx8gMQxDUOylEq+ZDihjhCj4h+aYQWEo6/7FzJmw5Qf6+ty21jq+kBmz/HLzYonTBP8cCf4w3mMAYJADPQG1+7Y1gRIXxns9o0pmMVmqnKq+UTwP7c/H+92LGB/P/XpCwT/3httbTG6iMbjT/w1t0IlkJzL9HtzK2NLDhJxwt6KJ1+fM07ghJW+kLRJGCBIS+v4n5SMGXdoovYUsvIDrlqNr1Ld6nQP9AuL+/iUDawftEvFmyhtKJTLh5x00GpW2RCXB/+Ys4XwGxVtdWVrWjoaLZezepzd5boQ8oRXoZKf/jJRNxldc+aXyMzDJcC9DZc3Nn+rgeBpXOrLaF0= e.antonovich@innopolis.university
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v2"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm5393k4mt5cimedmqr"
        disk_id     = "fhm5393k4mt5cimedmqr"
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
        ip_address         = "192.168.10.10"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:d5:d0:49:6b"
        nat                = true
        nat_ip_address     = "158.160.106.98"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b1jjfvr4m1obio5ulp"
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

# module.yandex_cloud.yandex_vpc_network.default:
resource "yandex_vpc_network" "default" {
    created_at                = "2024-02-27T17:40:29Z"
    default_security_group_id = "enp802bondg336b2ljtp"
    folder_id                 = "b1g8aian1v2o5fmf9tsh"
    id                        = "enp43vbg1ol2df44onna"
    labels                    = {}
    name                      = "ya-network"
    subnet_ids                = [
        "e9b1jjfvr4m1obio5ulp",
    ]
}

# module.yandex_cloud.yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-27T17:40:31Z"
    folder_id      = "b1g8aian1v2o5fmf9tsh"
    id             = "e9b1jjfvr4m1obio5ulp"
    labels         = {}
    name           = "ya-network"
    network_id     = "enp43vbg1ol2df44onna"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

``terraform state list``:

```
module.app_python.docker_container.python_app
module.app_python.docker_image.img
module.github.github_branch_default.core_main
module.github.github_branch_default.main
module.github.github_branch_protection.default
module.github.github_repository.core
module.github.github_repository.repo
module.yandex_cloud.data.template_file.default
module.yandex_cloud.yandex_compute_disk.boot-disk-1
module.yandex_cloud.yandex_compute_image.default
module.yandex_cloud.yandex_compute_instance.default
module.yandex_cloud.yandex_vpc_network.default
module.yandex_cloud.yandex_vpc_subnet.subnet-1
```

### Applied changes

```
module.yandex_cloud.data.template_file.default: Reading...
module.yandex_cloud.data.template_file.default: Read complete after 0s [id=8d608f838d919be7823a4d0b3db6fbf7e56a3ee178939013e113352d36eec2b3]
module.yandex_cloud.yandex_vpc_network.default: Refreshing state... [id=enp43vbg1ol2df44onna]
module.yandex_cloud.yandex_compute_image.default: Refreshing state... [id=fd81uojalf2rcuc9fd02]
module.yandex_cloud.yandex_compute_disk.boot-disk-1: Refreshing state... [id=fhm5393k4mt5cimedmqr]
module.app_python.docker_image.img: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
module.app_python.docker_container.python_app: Refreshing state... [id=03ce52ab665ebe6e6e01a39c49256fb3bac9286abfb78568ea64ba5fd853eccc]
module.github.github_repository.core: Refreshing state... [id=devops-test]
module.github.github_repository.repo: Refreshing state... [id=devops-repo]
module.yandex_cloud.yandex_vpc_subnet.subnet-1: Refreshing state... [id=e9b1jjfvr4m1obio5ulp]
module.yandex_cloud.yandex_compute_instance.default: Refreshing state... [id=fhmdbk29dfa8oi5kd0j0]
module.github.github_branch_default.main: Refreshing state... [id=devops-repo]
module.github.github_branch_default.core_main: Refreshing state... [id=devops-test]
module.github.github_branch_protection.default: Refreshing state... [id=BPR_kwDOLYzscs4C0vNt]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # module.app_python.docker_container.python_app must be replaced
-/+ resource "docker_container" "python_app" {
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
      ~ hostname                                    = "03ce52ab665e" -> (known after apply)
      ~ id                                          = "03ce52ab665ebe6e6e01a39c49256fb3bac9286abfb78568ea64ba5fd853eccc" -> (known after apply)
      ~ image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a" # forces replacement -> (known after apply) # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "python_app"
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
        # (13 unchanged attributes hidden)

      ~ ports {
          ~ internal = 80 -> 300 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

  # module.app_python.docker_image.img must be replaced
-/+ resource "docker_image" "img" {
      ~ id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest" -> (known after apply)
      ~ image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a" -> (known after apply)
      ~ name         = "nginx:latest" -> "evsey/flask-moscow-time-app" # forces replacement
      ~ repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107" -> (known after apply)
        # (1 unchanged attribute hidden)
    }

Plan: 2 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ python_container_id = "03ce52ab665ebe6e6e01a39c49256fb3bac9286abfb78568ea64ba5fd853eccc" -> (known after apply)
╷
│ Warning: Redundant empty provider block
│
│   on docker\main.tf line 10:
│   10: provider "docker" {}
│
│ Earlier versions of Terraform used empty provider blocks ("proxy provider configurations") for child modules to
│ declare their need to be passed a provider configuration by their callers. That approach was ambiguous and is now
│ deprecated.
│
│ If you control this module, you can migrate to the new declaration syntax by removing all of the empty provider
│ "docker" blocks and then adding or updating an entry like the following to the required_providers block of
│ module.app_python:
│     docker = {
│     }
╵

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

module.app_python.docker_container.python_app: Destroying... [id=03ce52ab665ebe6e6e01a39c49256fb3bac9286abfb78568ea64ba5fd853eccc]
module.app_python.docker_container.python_app: Destruction complete after 0s
module.app_python.docker_image.img: Destroying... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
module.app_python.docker_image.img: Creating...
module.app_python.docker_image.img: Creation complete after 5s [id=sha256:9f06d1166631dbbe9737250437b33a4d3667848ef8bfff7f41ed9694944f95eeevsey/flask-moscow-time-app]
module.app_python.docker_container.python_app: Creating...
module.app_python.docker_container.python_app: Creation complete after 0s [id=cb3eac873fc4063b51cbd49877b7fe9553e26c151b2ab287694c64d15d304caa]

Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

github_repo_name = "evsey9/devops-repo"
python_container_id = "cb3eac873fc4063b51cbd49877b7fe9553e26c151b2ab287694c64d15d304caa"
```

### Output

``terraform output``: 
```
github_repo_name = "evsey9/devops-repo"
python_container_id = "cb3eac873fc4063b51cbd49877b7fe9553e26c151b2ab287694c64d15d304caa"
```

## Best Practices

- We use Version Control: We store the Terraform configurations in a version control system like Git. This allows you to track changes, collaborate with others, and revert to previous versions if needed.

- Modularize: Break your infrastructure code into reusable modules. This promotes code reusability, simplifies maintenance, and allows for better organization.

- Keep Secrets Secure: Avoid hardcoding sensitive information such as passwords or API keys directly into your Terraform configurations. Instead, use Terraform's built-in mechanisms like input variables or external secret management tools like HashiCorp Vault.

- Use Remote State Storage: Store your Terraform state files remotely rather than locally. This enables collaboration among team members and provides better security and reliability.

- Implement State Locking: Enable state locking to prevent concurrent runs of Terraform that could lead to conflicts or corruption of the state file. Services like Amazon S3 or HashiCorp Consul can be used for state locking.

- Automate Execution: Integrate Terraform with your CI/CD pipeline to automate the execution of infrastructure changes. This ensures consistency and repeatability in your deployments.

- Tag Resources: Tag your infrastructure resources with metadata such as owner, environment, and purpose. This helps with cost allocation, resource management, and tracking.

- Use Workspaces: Utilize Terraform workspaces to manage multiple environments (e.g., dev, staging, production) within the same configuration. This allows you to maintain separate state files and configurations for each environment.

- Enable Logging and Monitoring: Enable logging and monitoring for your Terraform deployments. This helps you troubleshoot issues, track changes, and ensure compliance with policies.

- Regularly Update Providers and Modules: Keep your Terraform providers and modules up to date to leverage new features, bug fixes, and security patches.

- Implement Testing: Write automated tests for your Terraform code using tools like Terratest or Kitchen-Terraform. This helps catch errors early and ensures that your infrastructure behaves as expected.

- Document Your Infrastructure: Maintain documentation for your Terraform configurations, including information about resources, dependencies, variables, and any special considerations or configurations.