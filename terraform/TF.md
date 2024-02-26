## Best Practices Applied:

### 1. Variable Definitions (container_name, image_name, image_tag, internal_port, external_port):

- Each variable is well-defined with a clear description.
- Default values are provided where applicable, enhancing ease of use.
- Data types are explicitly declared for each variable.

### 2. Terraform Configuration:

- Required providers are explicitly declared in the `terraform` block, ensuring proper dependency management.
- Provider version constraints are specified, promoting stability and predictability.

### 3. Provider Configuration:

- Provider configuration is cleanly separated from resources, improving readability and maintainability.

### 4. Resource Declarations:

- Resources are appropriately named, providing clarity about their purpose.
- Interpolation is used to dynamically reference variable values within resource attributes.
- Proper indentation and formatting enhance readability.

### 5. Outputs:

- Outputs are defined to expose essential information for potential downstream usage.
- Descriptions are provided for each output, aiding understanding.
- Output values are accessed using appropriate interpolation.

## Docker

1)

```bash
terraform apply -var "container_name=lab_04_python_app"
```

````

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
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
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "lab_04_python_app"
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

  # docker_image.app will be created
  + resource "docker_image" "app" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "bulatok4/app_python:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.app: Creating...
docker_image.app: Still creating... [10s elapsed]
docker_image.app: Still creating... [20s elapsed]
docker_image.app: Creation complete after 22s [id=sha256:6ce1b7549c02f84c55c64d23a510c058f7c04ed54945ce61463b4586835446debulatok4/app_python:latest]
docker_container.app: Creating...
docker_container.app: Creation complete after 0s [id=01da1567c44158ec66fa0268920db94dcedb9618605cab4869b9345777a875f5]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "01da1567c44158ec66fa0268920db94dcedb9618605cab4869b9345777a875f5"
image_id = "sha256:6ce1b7549c02f84c55c64d23a510c058f7c04ed54945ce61463b4586835446debulatok4/app_python:latest"
````

2)

```bash
terraform state list
```

```
docker_container.app
docker_image.app
```

3)

```bash
terraform state show docker_container.app
```

```
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = [
        "python",
        "main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "01da1567c441"
    id                                          = "01da1567c44158ec66fa0268920db94dcedb9618605cab4869b9345777a875f5"
    image                                       = "sha256:6ce1b7549c02f84c55c64d23a510c058f7c04ed54945ce61463b4586835446de"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "lab_04_python_app"
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
    working_dir                                 = "/myapp"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

4)

```bash
terraform output
```

```
container_id = "01da1567c44158ec66fa0268920db94dcedb9618605cab4869b9345777a875f5"
image_id = "sha256:6ce1b7549c02f84c55c64d23a510c058f7c04ed54945ce61463b4586835446debulatok4/app_python:latest"
```

## Yandex Cloud

```bash
terraform apply
```

```
yandex_vpc_network.network-1: Refreshing state... [id=enpqc90o3dd4ak3c1qkl]
yandex_vpc_subnet.subnet-1: Refreshing state... [id=e9btfne64i8umccj2ocm]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
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
                ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILfJCKvWopsvgWnoKwwNQBMRyoqOxXjhkEP707UZO0ng bulat2020205@gmail.com
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
          + subnet_id          = "e9btfne64i8umccj2ocm"
        }

      + resources {
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address_vm_1 = (known after apply)
  + internal_ip_address_vm_1 = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_compute_disk.boot-disk-1: Creating...
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=fhmj899i4e7o6akm74bi]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Creation complete after 26s [id=fhmu67ocvod061vd6pct]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address_vm_1 = "51.250.13.196"
internal_ip_address_vm_1 = "192.168.10.32"
```

```bash
terraform state list

# Output 
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```bash
terraform state show yandex_compute_instance.vm-1

# Output
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-26T19:58:39Z"
    folder_id                 = "b1gl12fk3g1aqa4hut1p"
    fqdn                      = "fhmu67ocvod061vd6pct.auto.internal"
    id                        = "fhmu67ocvod061vd6pct"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILfJCKvWopsvgWnoKwwNQBMRyoqOxXjhkEP707UZO0ng bulat2020205@gmail.com
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmj899i4e7o6akm74bi"
        disk_id     = "fhmj899i4e7o6akm74bi"
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
        ip_address         = "192.168.10.32"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1e:31:f0:cf"
        nat                = true
        nat_ip_address     = "51.250.13.196"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9btfne64i8umccj2ocm"
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

```bash
terraform output

# Output
external_ip_address_vm_1 = "51.250.13.196"
internal_ip_address_vm_1 = "192.168.10.32"
```


## Github

```bash
terraform apply


# Output
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-lab-04-test"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "devops-lab-04-test"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=devops-lab-04-test]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYWUn84C0mnV]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```


```bash
terraform state list

# Output
github_branch_default.main
github_branch_protection.default
github_repository.repo
```

```bash
terraform state show github_repository.repo

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
    description                 = "My awesome codebase"
    etag                        = "W/\"85c16ac6f9363e66b894db2c3ec59273febd8484f15bd7d7ed5fd810c4d8f699\""
    full_name                   = "bulatok/devops-lab-04-test"
    git_clone_url               = "git://github.com/bulatok/devops-lab-04-test.git"
    gitignore_template          = "Python"
    has_discussions             = false
    has_downloads               = true
    has_issues                  = true
    has_projects                = true
    has_wiki                    = true
    html_url                    = "https://github.com/bulatok/devops-lab-04-test"
    http_clone_url              = "https://github.com/bulatok/devops-lab-04-test.git"
    id                          = "devops-lab-04-test"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-lab-04-test"
    node_id                     = "R_kgDOLYWUnw"
    private                     = false
    repo_id                     = 763729055
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:bulatok/devops-lab-04-test.git"
    svn_url                     = "https://github.com/bulatok/devops-lab-04-test"
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


```bash
terraform import "github_repository.repo" "devops-lab-04-test"

# Output
github_repository.repo: Importing from ID "devops-lab-04-test"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=devops-lab-04-test]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

```