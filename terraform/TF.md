# Terraform

## Best practices

1. Gitignore for Terraform
2. Use variables for hiding secrets such as Yandex cloud/folder IDs, IAM token,
and the whole configuration via variables with default values
3. Use `terraform validate` and `terraform fmt`
4. Use `terraform plan` before any applying anything
5. Use outputs for verbosity
6. Prefer `terraform import` for repos (check the output below)

## Docker

I decided to deploy both apps at the same time, so there are
`custom_container_python` and `custom_container_java`.

### Docker `terraform state list`

```text
docker_container.custom_container_java
docker_container.custom_container_python
```

### Docker `terraform state show docker_container.custom_container_python`

```text
# docker_container.custom_container_python:
resource "docker_container" "custom_container_python" {
    attach                                      = false
    command                                     = [
        "sh",
        "-c",
        "python3 -m gunicorn --bind 0.0.0.0:8080 app.app:wsgi_app",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "cd66f8261702"
    id                                          = "cd66f8261702eaa5f8c0d933907ab2ccc03d875997dbcdeafa2c3e81fc4f7637"
    image                                       = "sha256:749f24067e5408f155eeed1487ac2f50319ea52c19d672d3fedc694a475cfe7a"
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
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "app_python_user"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Docker `terraform state show docker_container.custom_container_java`

```text
# docker_container.custom_container_java:
resource "docker_container" "custom_container_java" {
    attach                                      = false
    command                                     = [
        "sh",
        "-c",
        "java -jar app.jar",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/__cacert_entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "64370a9c6b37"
    id                                          = "64370a9c6b37674828a4d3b0a7f1c779b316b1e77a20bcc54598a68c93567132"
    image                                       = "sha256:df854918b688fada57b69c65ca9ff5cfc3da4abd933ea2248faf7b6c87fa0c9f"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_java"
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
    user                                        = "app_java_user"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_java"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Docker `terraform apply`

```text
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.custom_container_java will be created
  + resource "docker_container" "custom_container_java" {
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
      + image                                       = "dmfrpro/app_java"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app_java"
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
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_container.custom_container_python will be created
  + resource "docker_container" "custom_container_python" {
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
      + image                                       = "dmfrpro/app_python"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "app_python"
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
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id_java      = (known after apply)
  + container_id_python    = (known after apply)
  + container_image_java   = "dmfrpro/app_java"
  + container_image_python = "dmfrpro/app_python"
  + container_name_java    = "app_java"
  + container_name_python  = "app_python"
  + container_port_java    = [
      + {
          + external = 8000
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]
  + container_port_python  = [
      + {
          + external = 8080
          + internal = 8080
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.custom_container_python: Creating...
docker_container.custom_container_java: Creating...
docker_container.custom_container_java: Creation complete after 0s [id=64370a9c6b37674828a4d3b0a7f1c779b316b1e77a20bcc54598a68c93567132]
docker_container.custom_container_python: Creation complete after 0s [id=cd66f8261702eaa5f8c0d933907ab2ccc03d875997dbcdeafa2c3e81fc4f7637]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

### Docker Outputs

```text
Outputs:

container_id_java = "64370a9c6b37674828a4d3b0a7f1c779b316b1e77a20bcc54598a68c93567132"
container_id_python = "cd66f8261702eaa5f8c0d933907ab2ccc03d875997dbcdeafa2c3e81fc4f7637"
container_image_java = "dmfrpro/app_java"
container_image_python = "dmfrpro/app_python"
container_name_java = "app_java"
container_name_python = "app_python"
container_port_java = tolist([
  {
    "external" = 8000
    "internal" = 8000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
container_port_python = tolist([
  {
    "external" = 8080
    "internal" = 8080
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Yandex Cloud

### Yandex `terraform state list`

```text
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### Yandex `terraform state show yandex_compute_instance.vm-1`

```text
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T20:43:36Z"
    folder_id                 = "b1go3pon6gei7cgqs6oi"
    fqdn                      = "epdrml36ofoa9dnspvgh.auto.internal"
    id                        = "epdrml36ofoa9dnspvgh"
    metadata                  = {
        "ssh-keys" = (sensitive value)
    }
    name                      = "terraform-vm"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epdf8do2c0li4j78r1h7"
        disk_id     = "epdf8do2c0li4j78r1h7"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd83s8u085j3mq231ago"
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
        ip_address         = "192.168.20.24"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1b:b5:46:6c"
        nat                = true
        nat_ip_address     = "130.193.41.60"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e2lr1osdcac0p53dij7u"
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

### Yandex `terraform state show yandex_vpc_network.network-1`

```text
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-27T20:43:27Z"
    default_security_group_id = "enpgtreci0r4qulj8tsu"
    folder_id                 = "b1go3pon6gei7cgqs6oi"
    id                        = "enper1j3v785og413vo6"
    labels                    = {}
    name                      = "default"
    subnet_ids                = []
}
```

### Yandex `terraform state show yandex_vpc_subnet.subnet-1`

```text
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-27T20:43:29Z"
    folder_id      = "b1go3pon6gei7cgqs6oi"
    id             = "e2lr1osdcac0p53dij7u"
    labels         = {}
    name           = "Subnet 1"
    network_id     = "enper1j3v785og413vo6"
    v4_cidr_blocks = [
        "192.168.20.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-b"
}
```

### Yandex `terraform apply`

```text
var.cloud_id
  Cloud ID

  Enter a value:

var.folder_id
  Foder ID within the cloud

  Enter a value:

var.iam_token
  Specifies IAM token for auth in Yandex Cloud

  Enter a value:


Terraform used the selected providers to generate the following execution plan.
Resource actions are
indicated with the following symbols:
  + create

Terraform will perform the following actions:

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
          + "ssh-keys" = (sensitive value)
        }
      + name                      = "terraform-vm"
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

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd83s8u085j3mq231ago"
              + name        = (known after apply)
              + size        = (known after apply)
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
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
      + name                      = "default"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "Subnet 1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.20.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-b"
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_vpc_network.network-1: Still creating... [10s elapsed]
yandex_vpc_network.network-1: Creation complete after 13s [id=enpfirhjkpi1as8edk7g]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e2l0hp614mfg2d9qk519]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Still creating... [40s elapsed]
yandex_compute_instance.vm-1: Still creating... [50s elapsed]
yandex_compute_instance.vm-1: Still creating... [1m0s elapsed]
yandex_compute_instance.vm-1: Creation complete after 1m3s [id=epdkmaichijt7capejrp]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

## Github

### Github `terraform import "github_repository.repo" "devops-test"`

I have created a test repository
[devops-test](https://github.com/dmfrpro/devops-test) Let's import it:

```text
var.github_pat
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value:

github_repository.repo: Importing from ID "devops-test"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=devops-test]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

### Github `terraform apply`

```text
var.github_pat
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value:

github_repository.repo: Refreshing state... [id=devops-test]

Terraform used the selected providers to generate the following execution plan.
Resource actions are
indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-test"
    }

  # github_branch_protection.repo_main will be created
  + resource "github_branch_protection" "repo_main" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "devops-test"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ auto_init                   = false -> true
      - has_downloads               = true -> null
      - has_projects                = true -> null
        id                          = "devops-test"
      + license_template            = "mit"
        name                        = "devops-test"
        # (31 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Changes to Outputs:
  + default_branch  = "main"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=devops-test]
github_repository.repo: Modifications complete after 2s [id=devops-test]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=devops-test]
github_branch_protection.repo_main: Creating...
github_branch_protection.repo_main: Creation complete after 4s [id=BPR_kwDOLY65C84C0xNt]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

Outputs:

default_branch = "main"
repository_id = "devops-test"
repository_name = "devops-test"
```

## Github Team

I created an organization [dmfrpro-org](https://github.com/orgs/dmfrpro-org)
with terraform-maintained
[repository](https://github.com/dmfrpro-org/devops-test-team-repo) and [two
teams](https://github.com/orgs/dmfrpro-org/teams).

### `terraform apply`

```text
var.github_pat
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value:


Terraform used the selected providers to generate the following execution plan. Resource
actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.repo_main will be created
  + resource "github_branch_default" "repo_main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-test-team-repo"
    }

  # github_branch_protection.repo_protection will be created
  + resource "github_branch_protection" "repo_protection" {
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
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-test-team-repo"
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

  # github_team.developers will be created
  + resource "github_team" "developers" {
      + create_default_maintainer = false
      + description               = "DevOps guys please we don't follow best practices"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "Development Team"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team.devops will be created
  + resource "github_team" "devops" {
      + create_default_maintainer = false
      + description               = "We propose best practices"
      + etag                      = (known after apply)
      + id                        = (known after apply)
      + members_count             = (known after apply)
      + name                      = "DevOps Team"
      + node_id                   = (known after apply)
      + parent_team_read_id       = (known after apply)
      + parent_team_read_slug     = (known after apply)
      + privacy                   = "closed"
      + slug                      = (known after apply)
    }

  # github_team_repository.developers_repo will be created
  + resource "github_team_repository" "developers_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "push"
      + repository = "devops-test-team-repo"
      + team_id    = (known after apply)
    }

  # github_team_repository.devops_repo will be created
  + resource "github_team_repository" "devops_repo" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "devops-test-team-repo"
      + team_id    = (known after apply)
    }

Plan: 7 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + repositories = [
      + {
          + branch_protection_rule = (known after apply)
          + default_branch         = "main"
          + description            = ""
          + name                   = "devops-test-team-repo"
          + visibility             = "public"
        },
    ]

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_team.developers: Creating...
github_team.devops: Creating...
github_repository.repo: Creating...
github_team.developers: Still creating... [10s elapsed]
github_team.devops: Still creating... [10s elapsed]
github_repository.repo: Still creating... [10s elapsed]
github_team.devops: Creation complete after 10s [id=9573688]
github_team.developers: Creation complete after 13s [id=9573689]
github_repository.repo: Creation complete after 14s [id=devops-test-team-repo]
github_branch_default.repo_main: Creating...
github_team_repository.developers_repo: Creating...
github_team_repository.devops_repo: Creating...
github_team_repository.devops_repo: Creation complete after 3s [id=9573688:devops-test-team-repo]
github_branch_default.repo_main: Creation complete after 4s [id=devops-test-team-repo]
github_branch_protection.repo_protection: Creating...
github_team_repository.developers_repo: Creation complete after 5s [id=9573689:devops-test-team-repo]
github_branch_protection.repo_protection: Creation complete after 4s [id=BPR_kwDOLY8LSM4C0xd9]

Apply complete! Resources: 7 added, 0 changed, 0 destroyed.

Outputs:

repositories = [
  {
    "branch_protection_rule" = "BPR_kwDOLY8LSM4C0xd9"
    "default_branch" = "main"
    "description" = ""
    "name" = "devops-test-team-repo"
    "visibility" = "public"
  },
]
```
