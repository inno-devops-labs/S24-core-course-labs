# Exploring Terraform

## Docker provider

### Initial apply

`terraform state list`:

```shell
docker_container.nginx
docker_image.nginx
```

`terraform state show docker_container.nginx`:

```shell
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
    hostname                                    = "0fcd540f4c6f"
    id                                          = "0fcd540f4c6f4d089afeaebf87de49c5282e1ae288df1fa543d8d9078072b42a"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "nginx-container"
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

`terraform state show docker_container.nginx`:

```shell
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

### Using input variables from tutorial

Afterward, I did `terraform apply -var "container_name=ANOTHER"` to rename the container. The resource was replaced.
The log contained the following lines:

```shell
# docker_container.nginx must be replaced
...
    ~ name                                        = "nginx-container" -> "ANOTHER" # forces replacement
...
```

### Outputting some data

Afterward, I added `output.tf` file, executed `terraform apply -var "container_name=ANOTHER"`, and
finally `terraform output`.

Logs from the last command:

```shell
container_id = "15c4b721c0448bc2050a0a392eb7940b6a51aff733a2df90929cd2e39e92cd53"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
```

## TimeWeb provider

### Initial apply with input variables

After setting
up `TWC_TOKEN` ([link](https://github.com/timeweb-cloud/terraform-provider-timeweb-cloud?tab=readme-ov-file#%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-api-%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%B0-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81-%D0%BF%D1%80%D0%BE%D0%B2%D0%B0%D0%B9%D0%B4%D0%B5%D1%80%D0%BE%D0%BC))
and `main.tf` with `variables.tf`, I did `terraform apply -var "server_name=SERVER"`.

Afterward, I can view state via `terraform state list`:

```shell
data.twc_configurator.configurator
data.twc_os.os
twc_server.example-server
```

`terraform state show data.twc_configurator.configurator`:

```shell
# data.twc_configurator.configurator:
data "twc_configurator" "configurator" {
    cpu_frequency = "3.3"
    disk_type     = "nvme"
    id            = "11"
    location      = "ru-1"

    requirements {
        cpu_max                = 104
        cpu_min                = 1
        cpu_step               = 1
        disk_max               = 2048000
        disk_min               = 10240
        disk_step              = 5120
        network_bandwidth_max  = 1000
        network_bandwidth_min  = 200
        network_bandwidth_step = 100
        ram_max                = 747520
        ram_min                = 1024
        ram_step               = 1024
    }
}
```

`terraform state show data.twc_os.os`:

```shell
# data.twc_os.os:
data "twc_os" "os" {
    family           = "linux"
    id               = "79"
    name             = "ubuntu"
    version          = "22.04"
    version_codename = "jammy"

    requirements {
        bandwidth_min = 0
        cpu_min       = 0
        disk_min      = 0
        ram_min       = 0
    }
}
```

`terraform state show twc_server.example-server`:

```shell
# twc_server.example-server:
resource "twc_server" "example-server" {
    availability_zone = "spb-2"
    boot_mode         = "std"
    configurator_id   = 11
    cpu               = 1
    cpu_frequency     = "3.3"
    disks             = [
        {
            id          = <REMOVED FROM LOGS FOR PRIVACY REASONS>
            is_mounted  = true
            is_system   = true
            size        = 10240
            status      = "done"
            system_name = "vda"
            type        = "nvme"
            used        = 0
        },
    ]
    id                = <REMOVED FROM LOGS FOR PRIVACY REASONS>
    is_ddos_guard     = false
    location          = "ru-1"
    main_ipv4         = <REMOVED FROM LOGS FOR PRIVACY REASONS>
    name              = "SERVER"
    networks          = [
        {
            bandwidth     = 200
            ips           = [
                {
                    ip      = <REMOVED FROM LOGS FOR PRIVACY REASONS>
                    is_main = true
                    ptr     = ""
                    type    = "ipv6"
                },
                {
                    ip      = <REMOVED FROM LOGS FOR PRIVACY REASONS>
                    is_main = true
                    ptr     = ""
                    type    = "ipv4"
                },
            ]
            is_ddos_guard = false
            nat_mode      = ""
            type          = "public"
        },
    ]
    os                = [
        {
            id      = 79
            name    = "ubuntu"
            version = "22.04"
        },
    ]
    os_id             = 79
    preset_id         = 0
    project_id        = <REMOVED FROM LOGS FOR PRIVACY REASONS>
    ram               = 1024
    software          = []
    status            = "installing"

    configuration {
        configurator_id = 11
        cpu             = 1
        disk            = 10240
        ram             = 1024
    }
}
```

### Adding simple outputs

Afterward, I added `output.tf` file, executed `terraform apply -var "server_name=SERVER"`, and
finally `terraform output`.

Logs from the last command:

```shell
availability_zone = "spb-2"
location = "ru-1"
```

## Github provider

### Initial apply with input variable

After setting `main.tf` with `variables.tf`, I did `terraform apply"`.

Afterward, I can view state via `terraform state list`:

```shell
github_branch_default.main
github_branch_protection.default
github_repository.repo
```

`terraform state show github_branch_default.main`:

```shell
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "terraform-test-repo"
    rename     = false
    repository = "terraform-test-repo"
}
```

`terraform state show github_branch_protection.default`:

```shell
# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLYymLc4C0ur3"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "terraform-test-repo"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}
```

`terraform state show github_repository.repo`:

```shell
# github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Temporary test repo for devops course"
    etag                        = "W/\"619aa88433810a572d6a1c9c1b67bcb39ffef90dbbf766a2cacee7b199f95dad\""
    full_name                   = "Dirakon/terraform-test-repo"
    git_clone_url               = "git://github.com/Dirakon/terraform-test-repo.git"
    gitignore_template          = "VisualStudio"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/Dirakon/terraform-test-repo"
    http_clone_url              = "https://github.com/Dirakon/terraform-test-repo.git"
    id                          = "terraform-test-repo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "terraform-test-repo"
    node_id                     = "R_kgDOLYymLQ"
    private                     = false
    repo_id                     = 764192301
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Dirakon/terraform-test-repo.git"
    svn_url                     = "https://github.com/Dirakon/terraform-test-repo"
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

```

### Importing another repo

Afterward, I added import section to my `main.tf` file, and
did `terraform import "github_repository.The-Root-Of-All-Evil" "The-Root-Of-All-Evil"` to import already existing repo.

After I did, `terraform apply`, no changes were introduced as the state of the repo mirrors the config already.

## Applied best practices

1. Not including any tokens in committed code, instead using env variables
2. Splitting workspaces via folders
3. Splitting configs via multiple `.tf` files
4. Viewing `terraform plan` and outputs of others `terraform` commands with foremost attention
5. Use near-latest versions of providers and ClI tools
