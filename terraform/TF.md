# Terraform

---
## Docker
<code> terraform state show docker_container.flask_app </code>

```
# docker_container.flask_app:
resource "docker_container" "flask_app" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "flask",
        "run",
        "--host=0.0.0.0",
        "--port=5000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "af10776b3a26"
    id                                          = "af10776b3a26c291ac0b6c09896fe47e7a495500ce18ee03cc9aa27ceebc8c3c"
    image                                       = "sha256:041a753e8ca77e6d95108647ef91386f3c411e1a4abf1c429bcc0d5aa8b1884b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "flask-web-app"
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
    user                                        = "userwithoutroot"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/home/userwithoutroot/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
<code> terraform state list </code>

```
docker_container.flask_app
docker_image.flask_app
```

Output from Terraform:

<code> terraform output </code>

```
container_id = "af10776b3a26c291ac0b6c09896fe47e7a495500ce18ee03cc9aa27ceebc8c3c"
image_id = "sha256:041a753e8ca77e6d95108647ef91386f3c411e1a4abf1c429bcc0d5aa8b1884bcustom_app:latest"
```

---
## Cloud
<code>  terraform state show yandex_compute_disk.boot-disk-1 </code>

```
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-26T21:38:03Z"
    folder_id   = "b1gtrhju6da0t81776al"
    id          = "fhmpo3u2rp55ue0n0s5q"
    image_id    = "fd81u2vhv3mc49l1ccbb"
    name        = "boot-disk-1"
    product_ids = [
        "f2e92qu6f879vvpe8jad",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-26T21:38:14Z"
    folder_id                 = "b1gtrhju6da0t81776al"
    fqdn                      = "fhm0299qh6vah93l4gnf.auto.internal"
    id                        = "fhm0299qh6vah93l4gnf"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICjMTOLcHhFkutBFJDPN4GhAL92esl0bkiF8rjL8kpad code
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmpo3u2rp55ue0n0s5q"
        disk_id     = "fhmpo3u2rp55ue0n0s5q"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd81u2vhv3mc49l1ccbb"
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
        ip_address         = "192.168.10.6"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:12:53:a8:9b"
        nat                = true
        nat_ip_address     = "51.250.66.89"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bevur4ljd3mqc6nvck"
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
# yandex_vpc_network.network-1:
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-26T21:38:03Z"
    default_security_group_id = "enpqpnppsf0fj6ss6i5e"
    folder_id                 = "b1gtrhju6da0t81776al"
    id                        = "enp6ghttqcf3rhukmjif"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}
# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-26T21:38:08Z"
    folder_id      = "b1gtrhju6da0t81776al"
    id             = "e9bevur4ljd3mqc6nvck"
    labels         = {}
    name           = "subnet1"
    network_id     = "enp6ghttqcf3rhukmjif"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```
<code> terraform state list </code>

```
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

Output from Terraform:

<code> terraform output  </code>

```
external_ip_address_vm_1 = "51.250.66.89"
internal_ip_address_vm_1 = "192.168.10.6"
```

---
## GitHub
<code> terraform state show </code>

```
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "TerraformCheck"
    repository = "TerraformCheck"
}
# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLYYU7c4C0nPv"
    pattern                         = "main"
    repository_id                   = "TerraformCheck"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        require_code_owner_reviews      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}
# github_repository.S24-DevOps-labs:
resource "github_repository" "S24-DevOps-labs" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    archived                    = false
    auto_init                   = true
    branches                    = [
        {
            name      = "main"
            protected = false
        },
    ]
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Repository for DevOps lab grading"
    etag                        = "W/\"08be9ac658af61e8f703069dd8d3ebae6e3e86a7568c5f4e4191198aa11af1ab\""
    full_name                   = "nikzor/TerraformCheck"
    git_clone_url               = "git://github.com/nikzor/TerraformCheck.git"
    gitignore_template          = "Python"
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/nikzor/TerraformCheck"
    http_clone_url              = "https://github.com/nikzor/TerraformCheck.git"
    id                          = "TerraformCheck"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "TerraformCheck"
    node_id                     = "R_kgDOLYYU7Q"
    private                     = false
    repo_id                     = 763761901
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:nikzor/TerraformCheck.git"
    svn_url                     = "https://github.com/nikzor/TerraformCheck"
    visibility                  = "public"
    vulnerability_alerts        = false
}
```
<code> terraform state list </code>

```
github_branch_default.main
github_branch_protection.default
github_repository.S24-DevOps-labs
```

Output from Terraform:

<code> terraform output  </code>

```
branch = "main"
id = "TerraformCheck"
name = "TerraformCheck"
```

---

# Terraform Best Practices Documentation

This document provides the best practices employed in managing Terraform configurations within this project. 
These practices are geared towards ensuring the manageability, version control, and organization of configurations 
across various platforms such as GitHub, Docker, and Yandex Cloud.

## Organized Directory Structure

- Each Terraform configuration resides within a dedicated directory based on its respective platform.
- Directory names are clearly marked to correspond to the specific service they configure (e.g., `github/`, `docker/`, `cloud/`).

## Separated Configuration Files

- Terraform configurations are divided into multiple files to enhance readability and ease of maintenance:
  - `main.tf`: Contains the primary set of resources being provisioned.
  - `variables.tf`: Configures the variables that keep data.
  - `outputs.tf`: Configures the outputs of terraform

## Versioning

- Version constraints are employed to ensure compatibility and stability within our Terraform configurations:
  - The `required_version` parameter within `main.tf` is configured to lock the Terraform CLI to a specific version range.
  - Provider versions are fixed using the `version` argument within the `required_providers` block to prevent unexpected alterations.
