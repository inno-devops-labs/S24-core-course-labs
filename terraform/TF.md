# Docker

Output of the `terraform show` command:

```bash
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python",
        "time_zone.py",
    ]
    env                                         = []
    hostname                                    = "6ae1008a2c5a"
    id                                          = "6ae1008a2c5ac30cfd11e41bc0bad38d339d35bdc4ab3da8ffd61f2be3d0b3c9"
    image                                       = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdec"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
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
    user                                        = "app_python"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/home/app_python"

    ports {
        external = 8000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest"
    image_id     = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdec"
    keep_locally = false
    name         = "nikitagrigorenko/app_python:latest"
    repo_digest  = "nikitagrigorenko/app_python@sha256:7ed4ccf4d20cd45f938f60d9f8e2c3eede216b0d0a64c25c3010e2d297d9cbc3"
}


Outputs:

container_id = "6ae1008a2c5ac30cfd11e41bc0bad38d339d35bdc4ab3da8ffd61f2be3d0b3c9"
image_id = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest"
```

Output of the `terraform show` command:
```bash
docker_container.app_python
docker_image.app_python
```

Output of the `terraform apply` command:
```bash
docker_image.app_python: Refreshing state... [id=sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest]
docker_container.app_python: Refreshing state... [id=03c52d93ac74fd705c149c357288764918208cce6fae677eb556f325b1dd8094]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_python must be replaced
-/+ resource "docker_container" "app_python" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "python",
          - "time_zone.py",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "03c52d93ac74" -> (known after apply)
      ~ id                                          = "03c52d93ac74fd705c149c357288764918208cce6fae677eb556f325b1dd8094" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "app_python"
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
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "app_python" -> null
      - working_dir                                 = "/home/app_python" -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ internal = 80 -> 5000 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id = "03c52d93ac74fd705c149c357288764918208cce6fae677eb556f325b1dd8094" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_python: Destroying... [id=03c52d93ac74fd705c149c357288764918208cce6fae677eb556f325b1dd8094]
docker_container.app_python: Destruction complete after 0s
docker_container.app_python: Creating...
docker_container.app_python: Creation complete after 0s [id=f31bdd5d0c71aa4a9f5a11dd015c1f8d08f73074cf636e8e0d264b18d69e37ef]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "f31bdd5d0c71aa4a9f5a11dd015c1f8d08f73074cf636e8e0d264b18d69e37ef"
image_id = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest"
```

Output of the `terraform output` command:
```bash
container_id = "f31bdd5d0c71aa4a9f5a11dd015c1f8d08f73074cf636e8e0d264b18d69e37ef"
image_id = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest"
```


# Cloud Yandex
Output of the `terraform apply` command:
```bash
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = "b1gfsnafkp1luu3mjsah"
      + id          = (known after apply)
      + image_id    = "fd83s8u085j3mq231ago"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 20
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + created_at                = (known after apply)
      + folder_id                 = "b1gfsnafkp1luu3mjsah"
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "user-data" = <<-EOT
                #cloud-config
                users:
                  - name: terraform1
                    groups: sudo
                    shell: /bin/bash
                    sudo: 'ALL=(ALL) NOPASSWD:ALL'
                    ssh-authorized-keys:
                      - AAAAC3NzaC1lZDI1NTE5AAAAIEAReCbooaAtIv/SzJV8UOup9xbDXFO+Pi33uzln9pGF nikitagrigorenko@MacBook-Pro.local
            EOT
        }
      + name                      = "terraform1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
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
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = "b1gfsnafkp1luu3mjsah"
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = "b1gfsnafkp1luu3mjsah"
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet-1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 2s [id=ensd523u43n0fdsf732o]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 0s [id=e12qt12343362bt4123m]
yandex_compute_disk.boot-disk-1: Creation complete after 6s [id=f1233vu123189l1231mp]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 30s [id=fasdmasdpx13pq8t12sd]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "51.201.12.197"
internal_ip_address_vm_1 = "192.168.10.30"
```

Output of the `terraform state list` command:
```bash
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

Output of the `terraform output` command:
```bash
external_ip_address_vm_1 = "51.201.12.197"
internal_ip_address_vm_1 = "192.168.10.30"
```


# GitHub

Outpur of the `terraform import "github_repository.repo" "sample-repo"`
```bash
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Importing from ID "sample-repo"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=sample-repo]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

Output of the `terraform apply` command:
```bash
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "sample-repo"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be created
  + resource "github_repository" "repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Sample Lab4 DevOps"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_downloads               = true
      + has_issues                  = true
      + has_projects                = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "sample-repo"
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

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Creating...
github_repository.repo: Creation complete after 6s [id=sample-repo]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=sample-repo]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYwmrs4C0uIY]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

Output of the `terraform show` command:
```bash
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"9935d9c3a99096c2664081d1dbc78a620b9579f08570a800bbd9bd3e31e7097b\""
    id         = "sample-repo"
    rename     = false
    repository = "sample-repo"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLYwmrs4C0uIY"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "sample-repo"
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
    description                 = "Sample Lab4 DevOps"
    etag                        = "W/\"9935d9c3a99096c2664081d1dbc78a620b9579f08570a800bbd9bd3e31e7097b\""
    full_name                   = "nik-grig-dev-ops/sample-repo"
    git_clone_url               = "git://github.com/nik-grig-dev-ops/sample-repo.git"
    has_discussions             = false
    has_downloads               = true
    has_issues                  = true
    has_projects                = true
    has_wiki                    = true
    html_url                    = "https://github.com/nik-grig-dev-ops/sample-repo"
    http_clone_url              = "https://github.com/nik-grig-dev-ops/sample-repo.git"
    id                          = "sample-repo"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "sample-repo"
    node_id                     = "R_kgDOLYwmrg"
    private                     = false
    repo_id                     = 764159662
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:nik-grig-dev-ops/sample-repo.git"
    svn_url                     = "https://github.com/nik-grig-dev-ops/sample-repo"
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

Output of the `terraform state list` command:
```bash
github_branch_default.main
github_branch_protection.default
github_repository.repo
```


# GitHub Teams
Output of the `terraform apply` command:
```bash
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 


Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_team.dev will be created
  + resource "github_team" "dev" {
      + create_default_maintainer = false
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Dev"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.man will be created
  + resource "github_team" "man" {
      + create_default_maintainer = false
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Man"
      + node_id                   = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_membership.membership_for_nikitagrigorenko will be created
  + resource "github_team_membership" "membership_for_nikitagrigorenko" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = (known after apply)
      + username = "nikitagrigorenko"
    }

  # github_team_membership.membership_for_y0szx will be created
  + resource "github_team_membership" "membership_for_y0szx" {
      + etag     = (known after apply)
      + id       = (known after apply)
      + role     = "member"
      + team_id  = (known after apply)
      + username = "y0szx"
    }

  # github_team_repository.dev_bind will be created
  + resource "github_team_repository" "dev_bind" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = (sensitive value)
      + team_id    = (known after apply)
    }

  # github_team_repository.man_bind will be created
  + resource "github_team_repository" "man_bind" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "admin"
      + repository = (sensitive value)
      + team_id    = (known after apply)
    }

Plan: 6 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.dev: Creating...
github_team.man: Creating...
github_team.dev: Creation complete after 8s [id=9569716]
github_team_repository.dev_bind: Creating...
github_team_membership.membership_for_y0szx: Creating...
github_team.man: Creation complete after 9s [id=9569717]
github_team_membership.membership_for_nikitagrigorenko: Creating...
github_team_repository.man_bind: Creating...
github_team_membership.membership_for_y0szx: Creation complete after 4s [id=9569716:y0szx]
github_team_membership.membership_for_nikitagrigorenko: Creation complete after 6s [id=9569717:nikitagrigorenko]
github_team_repository.dev_bind: Creation complete after 8s [id=9569716:sample-repo]
github_team_repository.man_bind: Creation complete after 7s [id=9569717:sample-repo]

Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
```

Output of the `terraform show` command:
```bash
# github_team.dev:
resource "github_team" "dev" {
    create_default_maintainer = false
    etag                      = "W/\"afeac971628d6e2df5c05dbf9346eb113e4a402ca4f98bd6b9940e575ff4d3ed\""
    id                        = "9569716"
    members_count             = 0
    name                      = "Dev"
    node_id                   = "T_kwDOCaAcJM4AkgW0"
    privacy                   = "closed"
    slug                      = "dev"
}

# github_team.man:
resource "github_team" "man" {
    create_default_maintainer = false
    etag                      = "W/\"2fab4b7ebb2d781c7ee9af10f56961c17adc640f9dffc44c719621d3db2ec308\""
    id                        = "9569717"
    members_count             = 0
    name                      = "Man"
    node_id                   = "T_kwDOCaAcJM4AkgW1"
    privacy                   = "closed"
    slug                      = "man"
}

# github_team_membership.membership_for_nikitagrigorenko:
resource "github_team_membership" "membership_for_nikitagrigorenko" {
    etag     = "W/\"787bd32dcb534ac36bb6abd452e4d5c9d31f8943f79eb6887d2b317811ee7b4b\""
    id       = "9569717:nikitagrigorenko"
    role     = "maintainer"
    team_id  = "9569717"
    username = "nikitagrigorenko"
}

# github_team_membership.membership_for_y0szx:
resource "github_team_membership" "membership_for_y0szx" {
    etag     = "W/\"752c103e779e14c80b54157b2e56fb457e13a990bf7d64e157a05f2b36f3218f\""
    id       = "9569716:y0szx"
    role     = "member"
    team_id  = "9569716"
    username = "y0szx"
}

# github_team_repository.dev_bind:
resource "github_team_repository" "dev_bind" {
    etag       = "W/\"9ce70ca972f84d3da5cbc2e7b54251fba74ef9c9ef1e6206a0c576fe227a35f6\""
    id         = "9569716:sample-repo"
    permission = "maintain"
    repository = (sensitive value)
    team_id    = "9569716"
}

# github_team_repository.man_bind:
resource "github_team_repository" "man_bind" {
    etag       = "W/\"fc638ed64318424e19b2d4985a93301d66332a738bd0653b061cc9c76c4e015a\""
    id         = "9569717:sample-repo"
    permission = "admin"
    repository = (sensitive value)
    team_id    = "9569717"
}

```

Output of the `terraform state list` command:
```bash
github_team.dev
github_team.man
github_team_membership.membership_for_nikitagrigorenko
github_team_membership.membership_for_y0szx
github_team_repository.dev_bind
github_team_repository.man_bind
```


# Best Practices 

- Variables and output were devided into other files. 

- Environment variables were used due to safety reasons.

- The Terraform code has been divided into reusable modules, which encourages code reuse and improves the codebase's readability and maintainability.

- To ensure code quality and readability, the terraform validate command has been used to verify the code for mistakes. Additionally, terraform fmt has been used to automatically format the code in accordance with Terraform's standards.

- Version pinning has been envolved: in order to prevent infrastructure failures caused by provider upgrades, the versions of the Terraform providers have been pinned.
