# Terraform

## Best practices

1. .gitignore
2. separate modules
3. hidding secrets

## Cloud

```bash
terraform state list
```

```
yandex_compute_instance.compute["devops-compute"]
```

```bash
terraform show
```

```h
# yandex_compute_instance.compute["devops-compute"]:
resource "yandex_compute_instance" "compute" {
    created_at                = "2024-02-27T16:08:01Z"
    folder_id                 = "b1gbn2p3grvofh87hel0"
    fqdn                      = "epdvvmd57jgqm4l46qqe.auto.internal"
    id                        = "epdvvmd57jgqm4l46qqe"
    metadata                  = {
        "user-data" = (sensitive value)
    }
    name                      = "devops-compute"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-b"

    boot_disk {
        auto_delete = true
        device_name = "epdi00v2ejkhvem74hrc"
        disk_id     = "epdi00v2ejkhvem74hrc"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd80bm0rh4rkepi5ksdi"
            size       = 64
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
        ip_address         = "10.6.0.27"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:1f:fd:9a:53"
        nat                = true
        nat_ip_address     = "130.193.40.13"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e2l4cukdh6m7n3uavhh2"
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


Outputs:

compute_public_ips = [
    {
        ip   = "130.193.40.13"
        name = "devops-compute"
    },
]
```

## Github

```bash
terraform state list
```

```
github_branch_default.main
github_branch_protection.default
github_repository.devops
```

```bash
terraform show
```

```h
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    id         = "S24-core-course-labs"
    repository = "S24-core-course-labs"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLOTuic4C0upN"
    pattern                         = "main"
    push_restrictions               = []
    repository_id                   = "S24-core-course-labs"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        dismissal_restrictions          = []
        pull_request_bypassers          = []
        require_code_owner_reviews      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}

# github_repository.devops:
resource "github_repository" "devops" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    archived                    = false
    auto_init                   = false
    branches                    = [
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
    etag                        = "W/\"33063ca79ee7e34843171b8bd1f9035b3587cb5101491fe8f2340feab98c0ff6\""
    full_name                   = "Legolass322/S24-core-course-labs"
    git_clone_url               = "git://github.com/Legolass322/S24-core-course-labs.git"
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/Legolass322/S24-core-course-labs"
    http_clone_url              = "https://github.com/Legolass322/S24-core-course-labs.git"
    id                          = "S24-core-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S24-core-course-labs"
    node_id                     = "R_kgDOLOTuiQ"
    private                     = false
    repo_id                     = 753200777
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Legolass322/S24-core-course-labs.git"
    svn_url                     = "https://github.com/Legolass322/S24-core-course-labs"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
}
```

## Dockerized services

### APP_GO

Have troubles :(

Didn't solve yet

### APP_PYTHON

```bash
terraform state list
```

```
docker_container.app_python
docker_image.app_python
```

```bash
terraform show
```

```h
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "/bin/sh",
        "-c",
        "python ./ptime/main.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "83e23dede0cd"
    id                                          = "83e23dede0cdce017c5e1721388bcf3f8498861a1f78e5dbddd97bccdb612353"
    image                                       = "sha256:3a9cc603dc5c5a6753c03843aa48168473670e996d38a1eb2ac9aa68848ad65b"
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
    user                                        = "appuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:3a9cc603dc5c5a6753c03843aa48168473670e996d38a1eb2ac9aa68848ad65blegolass322/devops:app_python"
    image_id     = "sha256:3a9cc603dc5c5a6753c03843aa48168473670e996d38a1eb2ac9aa68848ad65b"
    keep_locally = false
    name         = "legolass322/devops:app_python"
    repo_digest  = "legolass322/devops@sha256:e2bc43bf0a9b8ca81321b528cc928e1c318bbafe81d2d97fab3b17b7e2f8378d"
}
```