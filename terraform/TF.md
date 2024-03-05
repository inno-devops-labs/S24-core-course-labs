# Best practices used
- Used variables for reusing
- Used a consistent naming convention
- Always formated and validated
- Included lock-file into VCS
- Used different files for variables and outputs

# DOCKER

- `terraform apply` logs

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
      + name                                        = "devops-nginx-cont"
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
    }

Plan: 2 to add, 0 to change, 0 to destroy.
```

- `terraform state list`
```
docker_container.nginx
docker_image.nginx
```

- `terraform state show docker_container.nginx`
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
    hostname                                    = "ec08bc77aac0"
    id                                          = "ec08bc77aac0f2a7b21f6c5ec9509fd86dc81ae822d81636e32a21d9f2186e83"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devops-nginx-cont"
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

- `terraform state show docker_image.nginx`
```
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

- `terraform output`
```
container_id = "ec08bc77aac0f2a7b21f6c5ec9509fd86dc81ae822d81636e32a21d9f2186e83"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
```

# Yandex Cloud

- `terraform apply` logs
```
# yandex_compute_disk.disk will be created
  + resource "yandex_compute_disk" "disk" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8svvs3unvqn83thrdk"
      + name        = "disk"
      + product_ids = (known after apply)
      + size        = 10
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_instance.vm will be created
  + resource "yandex_compute_instance" "vm" {
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + name                      = "vm"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v2"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + resources {
          + core_fraction = 5
          + cores         = 2
          + memory        = 1
        }
    }

  # yandex_vpc_network.network will be created
  + resource "yandex_vpc_network" "network" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet will be created
  + resource "yandex_vpc_subnet" "subnet" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm = (known after apply)
  + internal_ip_address_vm = (known after apply)
```

- `terraform state list`
```
```

- `terraform state show yandex_compute_disk.disk`
```
# yandex_compute_disk.disk:
resource "yandex_compute_disk" "disk" {
    block_size  = 4096
    created_at  = "2024-03-05T12:59:42Z"
    folder_id   = "b1g1h1m1femu1na18tl9"
    id          = "fhmfk7nujkpnisl5mc3s"
    image_id    = "fd8svvs3unvqn83thrdk"
    name        = "disk"
    product_ids = [
        "f2erca36agei1p5ml8ih",
    ]
    size        = 10
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
```

- `terraform state show yandex_compute_instance.vm`
```
# yandex_compute_instance.vm:
resource "yandex_compute_instance" "vm" {
    created_at                = "2024-03-05T12:59:53Z"
    folder_id                 = "b1g1h1m1femu1na18tl9"
    fqdn                      = "fhmjap0qpf9gmbcvtnmd.auto.internal"
    id                        = "fhmjap0qpf9gmbcvtnmd"
    name                      = "vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v2"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmfk7nujkpnisl5mc3s"
        disk_id     = "fhmfk7nujkpnisl5mc3s"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8svvs3unvqn83thrdk"
            name       = "disk"
            size       = 10
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
        ip_address         = "192.168.10.30"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:13:56:41:ac"
        nat                = true
        nat_ip_address     = "84.252.129.135"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b6ik8vr4kqph3dcbk3"
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
        preemptible = false
    }
}
```

- `terraform state show yandex_vpc_network.network`
```
# yandex_vpc_network.network:
resource "yandex_vpc_network" "network" {
    created_at                = "2024-03-05T12:59:42Z"
    default_security_group_id = "enpbvtipkumerksuog8s"
    folder_id                 = "b1g1h1m1femu1na18tl9"
    id                        = "enp87ie45h4trea1n17t"
    labels                    = {}
    name                      = "network"
    subnet_ids                = []
}
```

- `terraform state show yandex_vpc_subnet.subnet`
```
# yandex_vpc_subnet.subnet:
resource "yandex_vpc_subnet" "subnet" {
    created_at     = "2024-03-05T12:59:44Z"
    folder_id      = "b1g1h1m1femu1na18tl9"
    id             = "e9b6ik8vr4kqph3dcbk3"
    labels         = {}
    name           = "subnet"
    network_id     = "enp87ie45h4trea1n17t"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

- `terraform output`
```
external_ip_address_vm = "84.252.129.135"
internal_ip_address_vm = "192.168.10.30"
```

# Github

- `terraform apply` logs
```
 # github_branch.master will be created
  + resource "github_branch" "master" {
      + branch        = "master"
      + etag          = (known after apply)
      + id            = (known after apply)
      + ref           = (known after apply)
      + repository    = "devops-terraform"
      + sha           = (known after apply)
      + source_branch = "main"
      + source_sha    = (known after apply)
    }

  # github_branch_default.master-default will be created
  + resource "github_branch_default" "master-default" {
      + branch     = "master"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-terraform"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "master"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo-devops-terraform will be created
  + resource "github_repository" "repo-devops-terraform" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "smth"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-terraform"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
      + web_commit_signoff_required = false
    }
```

- `terraform state list`
```
github_branch.master
github_branch_default.master-default
github_branch_protection.default
github_repository.repo-devops-terraform
```

- `terraform state show github_branch.master`
```
# github_branch.master:
resource "github_branch" "master" {
    branch        = "master"
    etag          = "W/\"b14fe49947459235d960a48c22c8a703b31dccfc69a593de87e48e6a6367b021\""
    id            = "devops-terraform:master"
    ref           = "refs/heads/master"
    repository    = "devops-terraform"
    sha           = "ae78c8400989854f048cb1a2b4c862a39528d5dd"
    source_branch = "main"
    source_sha    = "ae78c8400989854f048cb1a2b4c862a39528d5dd"
}
```

- `terraform state show github_branch_default.master-default`
```
# github_branch_default.master-default:
resource "github_branch_default" "master-default" {
    branch     = "master"
    etag       = "W/\"52e8ebe92288f32e65ab0751354ece05d7f8d7a5d18941f074371ea07346f7e5\""
    id         = "devops-terraform"
    rename     = false
    repository = "devops-terraform"
}
```

- `terraform state show github_branch_protection.default`
```
# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLcAKjM4C1up5"
    lock_branch                     = false
    pattern                         = "master"
    repository_id                   = "devops-terraform"
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

- `terraform state show github_repository.repo-devops-terraform`
```
# github_repository.repo-devops-terraform:
resource "github_repository" "repo-devops-terraform" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "smth"
    etag                        = "W/\"ba10204e7ddd17ff2b2e08504a8e2c16631ab8c757f12cbd85ab28ca69ce4de2\""
    full_name                   = "habur331/devops-terraform"
    git_clone_url               = "git://github.com/habur331/devops-terraform.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/habur331/devops-terraform"
    http_clone_url              = "https://github.com/habur331/devops-terraform.git"
    id                          = "devops-terraform"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-terraform"
    node_id                     = "R_kgDOLcAKjA"
    private                     = false
    repo_id                     = 767560332
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:habur331/devops-terraform.git"
    svn_url                     = "https://github.com/habur331/devops-terraform"
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