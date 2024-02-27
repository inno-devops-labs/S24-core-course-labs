run `terraform state list`
```bash
$ terraform state list
docker_container.nginx
docker_image.nginx
```


```bash
$ terraform state show docker_container.nginx
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
    hostname                                    = "5a2a3815c251"
    id                                          = "5a2a3815c2510d3797ffdd7ba75b2e1fb781b9e1db3462e29da7d30c31b1ab96"
    image                                       = "sha256:6efc10a0510f143a90b69dc564a914574973223e88418d65c1f8809e08dc0a1f"
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
        external = 8081
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```


```bash
$ terraform state show docker_image.nginx
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:6efc10a0510f143a90b69dc564a914574973223e88418d65c1f8809e08dc0a1fnginx"
    image_id     = "sha256:6efc10a0510f143a90b69dc564a914574973223e88418d65c1f8809e08dc0a1f"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:63b44e8ddb83d5dd8020327c1f40436e37a6fffd3ef2498a6204df23be6e7e94"
}
```


I changed my external port in the configuration from `8081` to `8082` and got the following output after running `terraform apply`:
```bash
$ terraform apply
docker_container.nginx: Destroying... [id=5a2a3815c2510d3797ffdd7ba75b2e1fb781b9e1db3462e29da7d30c31b1ab96]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=e6865b62c446100d1243d0edb8d37b3dd5fe46d4f65103fc589f506252760bd9]
Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

I added `variables.tf` file with the following content:
```bash
variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "ExampleNginxContainer"
}
```

Then run `terraform apply` again
```bash
$ terraform apply
docker_container.nginx: Destroying... [id=e6865b62c446100d1243d0edb8d37b3dd5fe46d4f65103fc589f506252760bd9]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=7b86cb84f0df677a8604371b8698d79b5aac202a41ac5b595b812e750cf84956]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

## Yandex cloud
```bash
$ terraform state list
yandex_compute_instance.default
yandex_vpc_network.network
yandex_vpc_subnet.subnetwork
```

```bash
$ terraform show
# yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    allow_stopping_for_update = true
    created_at                = "2024-02-27T18:16:17Z"
    folder_id                 = "b1gjtumbnfshl713ms12"
    fqdn                      = "fhma3q1dvje3d8rsav3b.auto.internal"
    id                        = "fhma3q1dvje3d8rsav3b"
    name                      = "default"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm0qh2nn1suuicek45j"
        disk_id     = "fhm0qh2nn1suuicek45j"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd80bm0rh4rkepi5ksdi"
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
        ip_address         = "10.228.0.3"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:a1:e8:2d:fc"
        nat                = true
        nat_ip_address     = "158.160.97.167"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b2tfmhm1a5cmdm4g8u"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = true
    }
}

# yandex_vpc_network.network:
resource "yandex_vpc_network" "network" {
    created_at                = "2024-02-27T18:13:16Z"
    default_security_group_id = "enpvt3moo0d67deg5d88"
    folder_id                 = "b1gjtumbnfshl713ms12"
    id                        = "enpkgmumpgtlrigijqc7"
    labels                    = {}
    subnet_ids                = [
        "e9b2tfmhm1a5cmdm4g8u",
    ]
}

# yandex_vpc_subnet.subnetwork:
resource "yandex_vpc_subnet" "subnetwork" {
    created_at     = "2024-02-27T18:13:20Z"
    folder_id      = "b1gjtumbnfshl713ms12"
    id             = "e9b2tfmhm1a5cmdm4g8u"
    labels         = {}
    network_id     = "enpkgmumpgtlrigijqc7"
    v4_cidr_blocks = [
        "10.228.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}


Outputs:

external_ip = "158.160.97.167"
```

## GitHub

```bash
$ terraform show
 github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "S24-DevOps"
    repository = "S24-DevOps"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLOk0Mc4C0vw-"
    pattern                         = "main"
    repository_id                   = "S24-DevOps"
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

# github_repository.S24-DevOps:
resource "github_repository" "S24-DevOps" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    archived                    = false
    auto_init                   = false
    branches                    = [
        {
            name      = "lab1"
            protected = false
        },
        {
            name      = "lab2"
            protected = false
        },
        {
            name      = "lab3"
            protected = false
        },
        {
            name      = "main"
            protected = false
        },
    ]
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "My awesome codebase"
    etag                        = "W/\"299bd6826df811b7529054eb5cd6f16159c6ee509ca5e371e791ab4238d45929\""
    full_name                   = "Vikono/S24-DevOps"
    git_clone_url               = "git://github.com/Vikono/S24-DevOps.git"
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/Vikono/S24-DevOps"
    http_clone_url              = "https://github.com/Vikono/S24-DevOps.git"
    id                          = "S24-DevOps"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S24-DevOps"
    node_id                     = "R_kgDOLOk0MQ"
    private                     = false
    repo_id                     = 753480753
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Vikono/S24-DevOps.git"
    svn_url                     = "https://github.com/Vikono/S24-DevOps"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
}
```
