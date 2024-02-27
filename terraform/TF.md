## Terraform built infrastructure

```sh
terraform show
terraform state list
```


## Docker_container.nginx:
```
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
    hostname                                    = "5f0e4138a63f"
    id                                          = "5f0e4138a63f413af2fb745f3eaf792c1b23998ec1d9e443ed4167297679b99a"
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
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}

```

## Terraform state list
```
docker_container.nginx
docker_image.nginx
```

## Terraform state show docker_image.nginx
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
## Terraform changes (inputs)
```
docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx]
docker_container.nginx: Refreshing state... [id=c4f3843cc7d1ad470bbb87863fe9a9e5c74b59b329b9cd464c36b148f93942b4]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
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
      ~ hostname                                    = "c4f3843cc7d1" -> (known after apply)
      ~ id                                          = "c4f3843cc7d1ad470bbb87863fe9a9e5c74b59b329b9cd464c36b148f93942b4" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "tutorial" -> "lab4" # forces replacement
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

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=c4f3843cc7d1ad470bbb87863fe9a9e5c74b59b329b9cd464c36b148f93942b4]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=b1a2a5f1637269d69ab96121c9fd46d73613a9a83edd0c1bbec88c85ed0f52fa]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

```
## Docker outputs
```
container_id = "b1a2a5f1637269d69ab96121c9fd46d73613a9a83edd0c1bbec88c85ed0f52fa"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
```




# Yandex Cloud

```sh
terraform show
terraform state list
```

## yandex_compute_disk.boot-disk-1:
```
resource "yandex_compute_disk" "boot-disk-1" {
    block_size  = 4096
    created_at  = "2024-02-27T22:07:17Z"
    folder_id   = "b1g74pecf3ifm06nl8rt"
    id          = "fhmccebi80j2ibmupfnt"
    image_id    = "fd8auu58m9ic4rtekngm"
    name        = "boot-disk-1"
    product_ids = [
        "f2eukfbpru6me6o1vj06",
    ]
    size        = 20
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}

# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T22:07:26Z"
    folder_id                 = "b1g74pecf3ifm06nl8rt"
    fqdn                      = "fhmsfc9ljku7e3ps5eil.auto.internal"
    id                        = "fhmsfc9ljku7e3ps5eil"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC79Io4sBpu8sOKea9iXtCevz/y96T67hmd174JYsblH3PfO1017uou6FgWAT+w1LXrZOAJr9ubp+UvgB796Ct9PAwhVW7AcW91fi9lZUnNcTsmm6ndNuEqjxi26L2VJrauozZvEEg+ElgbIwQNYCwiFTqT2O9Ukf+FotExeOdLkCHzyJwHUzDab0aLwcHzLbSdPGbuQheCv6ADnYx4zFpJKPeamy50waKUo3m5/QxE/zkg/EuGzsiDBUeUzTOSj06+SkgXyGBBwWxBgQPW4ElMulVijjCd0vsi8jWQpzjG15Lhk7m/lbNA+XUh6zIbd4TbCXPJISAS/sGsILLI3pl+alBO9Z6sv9xEm0bEo8V3OZzZj/aiF5pBiu7QNb77qOCUAIrII0KS94igsQ2J3yXzPLXhl2wY/mORX5Q67DL+RHUBgO6oI42C7FOdx3fK4s05+gcP6lOtO2p96uCV2zHNDlMEynt4RvppzEwGuFRIRYg8Ez3TiD8nNJPyPiEiRFr3lRQeFIBkP3ZboxvrnUoxcReMbZtxmAtMaX5ws7c9BjpIhTdBATd24Hh/2q1HlU+Q8geV2QkjI23CnR7MiD21Hw1wtH2G1ZxKZIEKqp/W4U2C0+7wJ+qlRPVCgq3Z4N0CLHjqmder705tBPHl/w6ovVt6G169xwjywKCsZ1yuDw== nfedorovich@nfedorovich-linux
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmccebi80j2ibmupfnt"
        disk_id     = "fhmccebi80j2ibmupfnt"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8auu58m9ic4rtekngm"
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
        ip_address         = "192.168.10.21"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1c:7b:13:59"
        nat                = true
        nat_ip_address     = "51.250.90.45"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b5nfq8q0c6vd80eoum"
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
    created_at                = "2024-02-27T21:58:15Z"
    default_security_group_id = "enpidc79djnaqn2cfrp6"
    folder_id                 = "b1g74pecf3ifm06nl8rt"
    id                        = "enppg11govojmhamum2d"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9b5nfq8q0c6vd80eoum",
    ]
}

# yandex_vpc_subnet.subnet-1:
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-27T22:05:35Z"
    folder_id      = "b1g74pecf3ifm06nl8rt"
    id             = "e9b5nfq8q0c6vd80eoum"
    labels         = {}
    name           = "subnet1"
    network_id     = "enppg11govojmhamum2d"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Cloud state list
```
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

## Cloud outputs
```
network_id = "enppg11govojmhamum2d"
subnet_id = "e9b5nfq8q0c6vd80eoum"
```



# Terraform for GitHub

```sh
terraform show
terraform state list
```

## github_branch_default.main:
```
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"6476121ff20d2918f592ec61e87ef9c17db48676371f6da91825096c60078983\""
    id         = "unique-repo-name"
    rename     = false
    repository = "unique-repo-name"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLY70ls4C0xaE"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "unique-repo-name"
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
    description                 = "DevOps lab4"
    etag                        = "W/\"6476121ff20d2918f592ec61e87ef9c17db48676371f6da91825096c60078983\""
    full_name                   = "Uzifam/unique-repo-name"
    git_clone_url               = "git://github.com/Uzifam/unique-repo-name.git"
    gitignore_template          = "Python"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/Uzifam/unique-repo-name"
    http_clone_url              = "https://github.com/Uzifam/unique-repo-name.git"
    id                          = "unique-repo-name"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "unique-repo-name"
    node_id                     = "R_kgDOLY70lg"
    private                     = false
    repo_id                     = 764343446
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Uzifam/unique-repo-name.git"
    svn_url                     = "https://github.com/Uzifam/unique-repo-name"
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

## GitHub state list
```
github_branch_default.main
github_branch_protection.default
github_repository.repo
```




# Best practices
* Modular Structure: The configuration is modular, with separate sections for providers, resources, and variables. This modular structure improves readability, maintainability, and reusability of the code.

* Use of Variables: Variables are used to parameterize the configuration, allowing for flexibility and easier management. This includes `var.token`, `var.folder_id`, and `var.image_id`, which can be provided externally or through input files.

* Provider Configuration: Provider configuration is centralized at the beginning of the file, making it easy to manage and modify provider settings. This helps in maintaining consistency across multiple resources.

* Resource Naming: Resources are named using descriptive names such as `boot-disk-1`, `vm-1`, `network-1`, and `subnet-1`. Descriptive naming improves readability and clarity of the code.