# Terraform

## Best Practices

- Resources have been logically segregated into various files such as
  `variables.tf`, `output.tf`, and others.
- The Terraform code has been broken down into reusable modules, promoting code
  reuse and enhancing the maintainability and understandability of the codebase.
- The `terraform fmt` command has been used to format the code.
- The `terraform validate` command has been used to check the code for any
  errors, and `terraform fmt` has been used to automatically format the code
  according to Terraform's standards, ensuring code quality and readability.
- Version pinning has been applied: the versions of the Terraform providers have
  been pinned to ensure that the infrastructure doesn't break due to updates in
  the providers.

## CLI Outputs

### Docker

1. `TF_VAR_container_name=lab4 terraform apply`

    ```text
    docker_image.app: Refreshing state... [id=sha256:6c9e192a55b63e88f1b38547b1230388cd5a0e54aca148d8340ccab8b3982113fedorivn/simple-web-app:python-1.0.0]
    docker_container.app: Refreshing state... [id=5168431cd83ba5e0073f1ae286315bbd26f2176d2c07d30d775e75e7b0b0c41a]

    Terraform used the selected providers to generate the following execution plan. Resource
    actions are indicated with the following symbols:
    + create

    Terraform will perform the following actions:

    # docker_container.app will be created
    + resource "docker_container" "app" {
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
        + image                                       = "sha256:6c9e192a55b63e88f1b38547b1230388cd5a0e54aca148d8340ccab8b3982113"
        + init                                        = (known after apply)
        + ipc_mode                                    = (known after apply)
        + log_driver                                  = (known after apply)
        + logs                                        = false
        + must_run                                    = true
        + name                                        = "lab4"
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

    Plan: 1 to add, 0 to change, 0 to destroy.

    Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.

    Enter a value: yes

    docker_container.app: Creating...
    docker_container.app: Creation complete after 1s [id=1dc801b2b631c2be359f17f978e0fd01739fb019a333347dfe8c81921a366b49]

    Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
    ```

1. `terraform state list`

    ```text
    docker_container.app
    docker_image.app
    ```

1. `terraform state show docker_container.app`

    ```hcl
    # docker_container.app:
    resource "docker_container" "app" {
        attach                                      = false
        command                                     = [
            "uvicorn",
            "main:app",
            "--host",
            "0.0.0.0",
            "--port",
            "80",
        ]
        container_read_refresh_timeout_milliseconds = 15000
        cpu_shares                                  = 0
        entrypoint                                  = []
        env                                         = []
        hostname                                    = "5168431cd83b"
        id                                          = "5168431cd83ba5e0073f1ae286315bbd26f2176d2c07d30d775e75e7b0b0c41a"
        image                                       = "sha256:6c9e192a55b63e88f1b38547b1230388cd5a0e54aca148d8340ccab8b3982113"
        init                                        = false
        ipc_mode                                    = "private"
        log_driver                                  = "json-file"
        logs                                        = false
        max_retry_count                             = 0
        memory                                      = 0
        memory_swap                                 = 0
        must_run                                    = true
        name                                        = "simple-web-app"
        network_data                                = [
            {
                gateway                   = "172.17.0.1"
                global_ipv6_address       = ""
                global_ipv6_prefix_length = 0
                ip_address                = "172.17.0.6"
                ip_prefix_length          = 16
                ipv6_gateway              = ""
                mac_address               = "02:42:ac:11:00:06"
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
        user                                        = "uvicorn"
        wait                                        = false
        wait_timeout                                = 60
        working_dir                                 = "/app"

        ports {
            external = 8000
            internal = 80
            ip       = "0.0.0.0"
            protocol = "tcp"
        }
    }
    ```

1. `terraform output`

    ```text
    terraform output 
    container_id = "1dc801b2b631c2be359f17f978e0fd01739fb019a333347dfe8c81921a366b49"
    image_id = "sha256:6c9e192a55b63e88f1b38547b1230388cd5a0e54aca148d8340ccab8b3982113fedorivn/simple-web-app:python-1.0.0"
    ```

### Yandex Cloud

1. `terraform apply`

    ```text
    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
    with the following symbols:
    + create

    Terraform will perform the following actions:

    # yandex_compute_disk.boot-disk-1 will be created
    + resource "yandex_compute_disk" "boot-disk-1" {
        + block_size  = 4096
        + created_at  = (known after apply)
        + folder_id   = (known after apply)
        + id          = (known after apply)
        + image_id    = "fd8t8vqitgjou20saanq"
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
        + folder_id                 = (known after apply)
        + fqdn                      = (known after apply)
        + gpu_cluster_id            = (known after apply)
        + hostname                  = (known after apply)
        + id                        = (known after apply)
        + maintenance_grace_period  = (known after apply)
        + maintenance_policy        = (known after apply)
        + metadata                  = {
            + "ssh-keys" = <<-EOT
                    ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILycRbR32YtN1cD0SkJOwwO1cZgpaKVjJs42nTNh2RCD ivnfedor@gmail.com
                EOT
            }
        + name                      = "terraform1"
        + network_acceleration_type = "standard"
        + platform_id               = "standard-v1"
        + service_account_id        = (known after apply)
        + status                    = (known after apply)
        + zone                      = "ru-central1-a"

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
        + folder_id                 = (known after apply)
        + id                        = (known after apply)
        + labels                    = (known after apply)
        + name                      = "network1"
        + subnet_ids                = (known after apply)
        }

    # yandex_vpc_subnet.subnet-1 will be created
    + resource "yandex_vpc_subnet" "subnet-1" {
        + created_at     = (known after apply)
        + folder_id      = (known after apply)
        + id             = (known after apply)
        + labels         = (known after apply)
        + name           = "subnet1"
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
    yandex_vpc_network.network-1: Creation complete after 2s [id=enpm579u5mn0fd3f7dmo]
    yandex_vpc_subnet.subnet-1: Creating...
    yandex_vpc_subnet.subnet-1: Creation complete after 0s [id=e9bqt7i476ec6btt1m4m]
    yandex_compute_disk.boot-disk-1: Creation complete after 6s [id=fhmgcvu2ld689l09aimp]
    yandex_compute_instance.vm-1: Creating...
    yandex_compute_instance.vm-1: Still creating... [10s elapsed]
    yandex_compute_instance.vm-1: Still creating... [20s elapsed]
    yandex_compute_instance.vm-1: Still creating... [30s elapsed]
    yandex_compute_instance.vm-1: Creation complete after 30s [id=fhmamghpkdpq8tp2s49d]

    Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

    Outputs:

    external_ip_address_vm_1 = "51.250.12.10"
    internal_ip_address_vm_1 = "192.168.10.7"
    ```

1. `terraform state list`

    ```text
    yandex_compute_disk.boot-disk-1
    yandex_compute_instance.vm-1
    yandex_vpc_network.network-1
    yandex_vpc_subnet.subnet-1
    ```

1. `terraform state show yandex_compute_instance.vm-1`

    ```text
    # yandex_compute_instance.vm-1:
    resource "yandex_compute_instance" "vm-1" {
        created_at                = "2024-02-24T21:15:12Z"
        folder_id                 = "b1g5k33mjblji5mutq8m"
        fqdn                      = "fhmamghpkdpq8tp2s49d.auto.internal"
        id                        = "fhmamghpkdpq8tp2s49d"
        metadata                  = {
            "ssh-keys" = <<-EOT
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILycRbR32YtN1cD0SkJOwwO1cZgpaKVjJs42nTNh2RCD ivnfedor@gmail.com
            EOT
        }
        name                      = "terraform1"
        network_acceleration_type = "standard"
        platform_id               = "standard-v1"
        status                    = "running"
        zone                      = "ru-central1-a"

        boot_disk {
            auto_delete = true
            device_name = "fhmgcvu2ld689l09aimp"
            disk_id     = "fhmgcvu2ld689l09aimp"
            mode        = "READ_WRITE"

            initialize_params {
                block_size = 4096
                image_id   = "fd8t8vqitgjou20saanq"
                name       = "boot-disk-1"
                size       = 20
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
            ip_address         = "192.168.10.7"
            ipv4               = true
            ipv6               = false
            mac_address        = "d0:0d:ab:42:39:a3"
            nat                = true
            nat_ip_address     = "51.250.12.10"
            nat_ip_version     = "IPV4"
            security_group_ids = []
            subnet_id          = "e9bqt7i476ec6btt1m4m"
        }

        placement_policy {
            host_affinity_rules       = []
            placement_group_partition = 0
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
    ```

1. `terraform output`

    ```text
    external_ip_address_vm_1 = "51.250.12.10"
    internal_ip_address_vm_1 = "192.168.10.7"
    ```

### Github

1. `terraform apply`

    ```text
    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
    with the following symbols:
    + create

    Terraform will perform the following actions:

    # github_branch_default.main will be created
    + resource "github_branch_default" "main" {
        + branch     = "main"
        + etag       = (known after apply)
        + id         = (known after apply)
        + rename     = false
        + repository = "example-repo"
        }

    # github_branch_protection.default will be created
    + resource "github_branch_protection" "default" {
        + allows_deletions                = false
        + allows_force_pushes             = false
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
        + description                 = "DevOps Lab4 Example Repo"
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
        + name                        = "example-repo"
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
    github_repository.repo: Creation complete after 5s [id=example-repo]
    github_branch_default.main: Creating...
    github_branch_default.main: Creation complete after 2s [id=example-repo]
    github_branch_protection.default: Creating...
    github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLXfnUM4C0Zsx]

    Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
    ```

1. `terraform state list`

    ```text
    github_branch_default.main
    github_branch_protection.default
    github_repository.repo
    ```

1. `terraform state show github_repository.repo`

    ```text
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
        description                 = "DevOps Lab4 Example Repo"
        etag                        = "W/\"6c9780a3902365c1fdb9b032d65a9364f7458158865eb542d2450a340f079cdf\""
        full_name                   = "fedor-ivn-devops-demo-org/example-repo"
        git_clone_url               = "git://github.com/fedor-ivn-devops-demo-org/example-repo.git"
        has_discussions             = false
        has_downloads               = true
        has_issues                  = true
        has_projects                = true
        has_wiki                    = true
        html_url                    = "https://github.com/fedor-ivn-devops-demo-org/example-repo"
        http_clone_url              = "https://github.com/fedor-ivn-devops-demo-org/example-repo.git"
        id                          = "example-repo"
        is_template                 = false
        merge_commit_message        = "PR_TITLE"
        merge_commit_title          = "MERGE_MESSAGE"
        name                        = "example-repo"
        node_id                     = "R_kgDOLXfnUA"
        private                     = false
        repo_id                     = 762832720
        squash_merge_commit_message = "COMMIT_MESSAGES"
        squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
        ssh_clone_url               = "git@github.com:fedor-ivn-devops-demo-org/example-repo.git"
        svn_url                     = "https://github.com/fedor-ivn-devops-demo-org/example-repo"
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

1. `terraform import "github_repository.repo" "example-repo"`

    ```text
    terraform import "github_repository.repo" "example-repo"
    github_repository.repo: Importing from ID "example-repo"...
    github_repository.repo: Import prepared!
    Prepared github_repository for import
    github_repository.repo: Refreshing state... [id=example-repo]

    Import successful!

    The resources that were imported are shown above. These resources are now in
    your Terraform state and will henceforth be managed by Terraform.
    ```

    P.S: I removed my local `.tfstate` file first, then I imported it.

## GitHub Teams

1. `terraform apply`

    ```text
    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
    with the following symbols:
    + create

    Terraform will perform the following actions:

    # github_team.developers will be created
    + resource "github_team" "developers" {
        + create_default_maintainer = false
        + etag                      = (known after apply)
        + id                        = (known after apply)
        + members_count             = (known after apply)
        + name                      = "Developers"
        + node_id                   = (known after apply)
        + parent_team_read_id       = (known after apply)
        + parent_team_read_slug     = (known after apply)
        + privacy                   = "closed"
        + slug                      = (known after apply)
        }

    # github_team.managers will be created
    + resource "github_team" "managers" {
        + create_default_maintainer = false
        + etag                      = (known after apply)
        + id                        = (known after apply)
        + members_count             = (known after apply)
        + name                      = "Managers"
        + node_id                   = (known after apply)
        + parent_team_read_id       = (known after apply)
        + parent_team_read_slug     = (known after apply)
        + privacy                   = "closed"
        + slug                      = (known after apply)
        }

    # github_team_membership.membership_for_fedorivn will be created
    + resource "github_team_membership" "membership_for_fedorivn" {
        + etag     = (known after apply)
        + id       = (known after apply)
        + role     = "member"
        + team_id  = (known after apply)
        + username = "fedor-ivn"
        }

    # github_team_membership.membership_for_snejugal will be created
    + resource "github_team_membership" "membership_for_snejugal" {
        + etag     = (known after apply)
        + id       = (known after apply)
        + role     = "member"
        + team_id  = (known after apply)
        + username = "snejugal"
        }

    # github_team_repository.developeres_bind will be created
    + resource "github_team_repository" "developeres_bind" {
        + etag       = (known after apply)
        + id         = (known after apply)
        + permission = "maintain"
        + repository = (sensitive value)
        + team_id    = (known after apply)
        }

    # github_team_repository.managers_bind will be created
    + resource "github_team_repository" "managers_bind" {
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

    github_team.developers: Creating...
    github_team.managers: Creating...
    github_team.developers: Creation complete after 9s [id=9553464]
    github_team_membership.membership_for_snejugal: Creating...
    github_team_repository.developeres_bind: Creating...
    github_team.managers: Creation complete after 9s [id=9553465]
    github_team_membership.membership_for_fedorivn: Creating...
    github_team_repository.managers_bind: Creating...
    github_team_membership.membership_for_snejugal: Creation complete after 5s [id=9553464:snejugal]
    github_team_repository.developeres_bind: Creation complete after 6s [id=9553464:example-repo]
    github_team_repository.managers_bind: Creation complete after 6s [id=9553465:example-repo]
    github_team_membership.membership_for_fedorivn: Creation complete after 6s [id=9553465:fedor-ivn]

    Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
    ```

1. `terraform state list`

    ```text
    github_team.developers
    github_team.managers
    github_team_membership.membership_for_fedorivn
    github_team_membership.membership_for_snejugal
    github_team_repository.developeres_bind
    github_team_repository.managers_bind
    ```

1. `terraform state show github_team.developers`

    ```text
    # github_team.developers:
    resource "github_team" "developers" {
        create_default_maintainer = false
        etag                      = "W/\"d7baff2ef6c817a8dea7a19ff002fcf3dc33da692c2c0efc646548b7d798794b\""
        id                        = "9553464"
        members_count             = 0
        name                      = "Developers"
        node_id                   = "T_kwDOCZset84AkcY4"
        privacy                   = "closed"
        slug                      = "developers"
    }
    ```
