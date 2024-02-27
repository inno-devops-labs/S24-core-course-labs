# Terraform

## Docker Provider

Output for `terraform state list`

```
docker_container.nginx
docker_image.nginx
```

Output for `terraform state show docker_container.nginx`

```tf
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
    hostname                                    = "6ce5d6880e38"
    id                                          = "6ce5d6880e38f2aeebf44652116bd0fa9938a855954c7811b8624be26789d306"
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
            gateway                   = "192.168.215.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "192.168.215.2"
            ip_prefix_length          = 24
            ipv6_gateway              = ""
            mac_address               = "02:42:c0:a8:d7:02"
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

Output for `terraform output`

```
container_id = "6ce5d6880e38f2aeebf44652116bd0fa9938a855954c7811b8624be26789d306"
image_id = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676nginx"
```

## TimeWeb Provider

Output of `terraform state list`

```
data.twc_configurator.configurator
data.twc_os.os
twc_server.example-server
```

Output of `terraform state show data.twc_configurator.configurator`

```tf
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

Output of `terraform state show data.twc_os.os`

```tf
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

Output of `terraform state show twc_server.example-server`

```tf
# twc_server.example-server:
resource "twc_server" "example-server" {
    availability_zone = "spb-2"
    boot_mode         = "std"
    configurator_id   = 11
    cpu               = 1
    cpu_frequency     = "3.3"
    disks             = [
        {
            id          = 16774753
            is_mounted  = true
            is_system   = true
            size        = 10240
            status      = "done"
            system_name = "vda"
            type        = "nvme"
            used        = 0
        },
    ]
    id                = "2600359"
    is_ddos_guard     = false
    location          = "ru-1"
    main_ipv4         = "**************"
    name              = "Default server name"
    networks          = [
        {
            bandwidth     = 200
            ips           = [
                {
                    ip      = "******************"
                    is_main = true
                    ptr     = ""
                    type    = "ipv6"
                },
                {
                    ip      = "**************"
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
    project_id        = 241221
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

### Some outputs

I've also added some outputs

```tf
output "os" {
  description = "OS of the server"
  value       = twc_server.example-server.os.name
}
```

Output of `terraform output`

```
os = "ubuntu"
```

## GitHub Provider

Output of `terraform state list`

```
github_branch_default.main
github_branch_protection.default
github_repository.repo
```

Output of `terraform state show github_branch_default.main`

```tf
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "terraform-test"
    rename     = false
    repository = "terraform-test"
}
```

Output of `terraform state show github_branch_protection.default`

```tf
# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLY08qc4C0vWa"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "terraform-test"
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

Output of `terraform state show github_repository.repo`

```
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
    description                 = "devops course temp repo"
    etag                        = "W/\"51c9b42fe2653c82a8e6e55601f273282ab24772061037a6850cf6e25c681713\""
    full_name                   = "metafates/terraform-test"
    git_clone_url               = "git://github.com/metafates/terraform-test.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/metafates/terraform-test"
    http_clone_url              = "https://github.com/metafates/terraform-test.git"
    id                          = "terraform-test"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "terraform-test"
    node_id                     = "R_kgDOLY08qQ"
    private                     = true
    repo_id                     = 764230825
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:metafates/terraform-test.git"
    svn_url                     = "https://github.com/metafates/terraform-test"
    topics                      = []
    visibility                  = "private"
    vulnerability_alerts        = false
}
```
