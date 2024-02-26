# Terraform

## Docker
### Outputs for the following commands:

```bash
terraform state show
terraform state list
```

```bash
# docker_container.moscow-app:
resource "docker_container" "moscow-app" {
    attach                                      = false
    command                                     = [
        "python",
        "-u",
        "app.py",
        "--host",
        "0.0.0.0",
        "--port",
        "5000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "5ea70b7f3710"
    id                                          = "5ea70b7f37107ab52c50a091bb0c79d8fc7962d3070baefa3b5e5e6de47b592e"
    image                                       = "sha256:6226a1ed9ac8da9b943ff45ef669e01a134a954522aadb9e6e70e00574dbfc08"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devops-moscow-app"
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
    working_dir                                 = "/app"

    ports {
        external = 8000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Outputs for the following commands:

```bash
terraform output
```

```bash
container_id = "5ea70b7f37107ab52c50a091bb0c79d8fc7962d3070baefa3b5e5e6de47b592e"
container_name = "devops-moscow-app"
```

## Yandex Cloud

### Outputs for the following commands:

```bash
terraform state show
terraform state list
```

```bash
# yandex_compute_disk.boot-disk-1:
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-25T17:25:56Z"
    folder_id   = "b1gg65k13122o9pouqi4"
    id          = "fhmg37jifootcrsmujbg"
    image_id    = "fd8t8vqitgjou20saanq"
    labels      = {}
    name        = "boot-disk-1"
    product_ids = [
        "f2ectu5pkit47tfmaev0",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}

# yandex_compute_instance.devops-vm:
resource "yandex_compute_instance" "devops-vm" {
    created_at                = "2024-02-25T17:28:15Z"
    folder_id                 = "b1gg65k13122o9pouqi4"
    fqdn                      = "fhmoc59fspb0uumt06ar.auto.internal"
    id                        = "fhmoc59fspb0uumt06ar"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKrkcl3feCLcQT4ZkNRJEEFbiqMncdI47OzEAgQfm2eEcsCvPFjC6kI59EI4tzY6hrdmCpnHr1q5NP4X8OvvGHA1W3uDuQThjsbGg+bjvtF79GxVhUerGzFwIoiaBoQZSXlL2pOgAErypWWhDrI229tBuwWo7iPJ/w2P3VLJsbAL/aGtsjqv/QSkr4xs25cwcEurROXhPj5SEIztHNG/oUKN1yudlBEg4qCRtIT7a0qS79x5pVQxjdVDZfHYxMIdc9vNG07Faz1u8zeniyoTnedkaWl2qT1gb78gOpcOMrzLVL204P2Au5u1f7CaHy6YyqDLz5QZMjlkKIxviJXaL5Zgu4DyyRs6OTlKZ5CxJh0G3xUZ5LxuRpMnM2x7Q7f371dPWxyPyOjIxVyWQ8kGsNZA59RV2phKGdWyNySs2+fB1NahcqWhzq+gXPd5tEyXudo1O0xCs2yYdplQoIAh5l5OsQaJXVA1z3Xa/UeggW7SBwnoOH7vlmQveyBRJ+Ikc= exemplerie@MacBook-Air-Valeria.local
        EOT
    }
    name                      = "devops-moscow-app"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmg37jifootcrsmujbg"
        disk_id     = "fhmg37jifootcrsmujbg"
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
        ip_address         = "192.168.50.27"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:18:61:52:fe"
        nat                = true
        nat_ip_address     = "51.250.2.92"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bgv9gbjdh6kqvujqgu"
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
    created_at                = "2024-02-25T17:28:12Z"
    default_security_group_id = "enpr51puee3v0n12b3ql"
    folder_id                 = "b1gg65k13122o9pouqi4"
    id                        = "enpdrovi1c74r5qla2g3"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = []
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-25T17:28:14Z"
    folder_id      = "b1gg65k13122o9pouqi4"
    id             = "e9bgv9gbjdh6kqvujqgu"
    labels         = {}
    name           = "moscow-app"
    network_id     = "enpdrovi1c74r5qla2g3"
    v4_cidr_blocks = [
        "192.168.50.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

### Outputs for the following commands:

```bash
terraform output
```

```bash
subnet-1_id = "e9bgv9gbjdh6kqvujqgu"
vm_ip = "192.168.50.27"
vm_ssh_key = <<EOT
ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKrkcl3feCLcQT4ZkNRJEEFbiqMncdI47OzEAgQfm2eEcsCvPFjC6kI59EI4tzY6hrdmCpnHr1q5NP4X8OvvGHA1W3uDuQThjsbGg+bjvtF79GxVhUerGzFwIoiaBoQZSXlL2pOgAErypWWhDrI229tBuwWo7iPJ/w2P3VLJsbAL/aGtsjqv/QSkr4xs25cwcEurROXhPj5SEIztHNG/oUKN1yudlBEg4qCRtIT7a0qS79x5pVQxjdVDZfHYxMIdc9vNG07Faz1u8zeniyoTnedkaWl2qT1gb78gOpcOMrzLVL204P2Au5u1f7CaHy6YyqDLz5QZMjlkKIxviJXaL5Zgu4DyyRs6OTlKZ5CxJh0G3xUZ5LxuRpMnM2x7Q7f371dPWxyPyOjIxVyWQ8kGsNZA59RV2phKGdWyNySs2+fB1NahcqWhzq+gXPd5tEyXudo1O0xCs2yYdplQoIAh5l5OsQaJXVA1z3Xa/UeggW7SBwnoOH7vlmQveyBRJ+Ikc= exemplerie@MacBook-Air-Valeria.local

EOT
exemplerie@MacBook-Air-Valeria cloud-yandex % terraform output                               
subnet-1_id = "e9bgv9gbjdh6kqvujqgu"
vm_ip = "192.168.50.27"
vm_ssh_key = <<EOT
ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDKrkcl3feCLcQT4ZkNRJEEFbiqMncdI47OzEAgQfm2eEcsCvPFjC6kI59EI4tzY6hrdmCpnHr1q5NP4X8OvvGHA1W3uDuQThjsbGg+bjvtF79GxVhUerGzFwIoiaBoQZSXlL2pOgAErypWWhDrI229tBuwWo7iPJ/w2P3VLJsbAL/aGtsjqv/QSkr4xs25cwcEurROXhPj5SEIztHNG/oUKN1yudlBEg4qCRtIT7a0qS79x5pVQxjdVDZfHYxMIdc9vNG07Faz1u8zeniyoTnedkaWl2qT1gb78gOpcOMrzLVL204P2Au5u1f7CaHy6YyqDLz5QZMjlkKIxviJXaL5Zgu4DyyRs6OTlKZ5CxJh0G3xUZ5LxuRpMnM2x7Q7f371dPWxyPyOjIxVyWQ8kGsNZA59RV2phKGdWyNySs2+fB1NahcqWhzq+gXPd5tEyXudo1O0xCs2yYdplQoIAh5l5OsQaJXVA1z3Xa/UeggW7SBwnoOH7vlmQveyBRJ+Ikc= exemplerie@MacBook-Air-Valeria.local

EOT
```

## Github

### Outputs for the following commands:

```bash
terraform state show
terraform state list
```

```bash
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"44aecf8eac9947001771ed36335c066a1c917ac7a790d0774cfb4630657f8268\""
    id         = "devops-lab-4"
    rename     = false
    repository = "devops-lab-4"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLYSR-c4C0leM"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "devops-lab-4"
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

# github_repository.devops-lab-4:
resource "github_repository" "devops-lab-4" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "GitHub repository test"
    etag                        = "W/\"44aecf8eac9947001771ed36335c066a1c917ac7a790d0774cfb4630657f8268\""
    full_name                   = "exemplerie/devops-lab-4"
    git_clone_url               = "git://github.com/exemplerie/devops-lab-4.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/exemplerie/devops-lab-4"
    http_clone_url              = "https://github.com/exemplerie/devops-lab-4.git"
    id                          = "devops-lab-4"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-lab-4"
    node_id                     = "R_kgDOLYSR-Q"
    private                     = false
    repo_id                     = 763662841
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:exemplerie/devops-lab-4.git"
    svn_url                     = "https://github.com/exemplerie/devops-lab-4"
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

### Outputs for the following commands:

```bash
terraform output
```

```bash
branch = "main"
id = "devops-lab-4"
name = "devops-lab-4"
```

### Outputs for the following commands:
```bash
terraform import "github_repository.devops-lab-4" "tamagotchi"
```

```bash
github_repository.devops-lab-4: Importing from ID "tamagotchi"...
github_repository.devops-lab-4: Import prepared!
  Prepared github_repository for import
github_repository.devops-lab-4: Refreshing state... [id=tamagotchi]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```