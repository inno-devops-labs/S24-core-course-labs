# Terraform

## Best Practices

- The Recommended Terraform Workspace Structure
- Separate Environments
- Naming conventions

## 1.3

```bash
➜  terraform apply

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
      + name                                        = "my_tf_created_docker_container"
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

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Still creating... [20s elapsed]
docker_image.nginx: Creation complete after 24s [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 4s [id=c95a4409758186bff21f7c24fde2ca80c637fca50cf1beabf83d036f9974249f]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

```bash
➜  terraform state list
docker_container.nginx
docker_image.nginx
```

```bash
➜  terraform state show docker_image.nginx                  
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107" }

```

```bash
➜  TF_VAR_nginx_container_name=name_from_env terraform apply
docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx]
docker_container.nginx: Refreshing state... [id=c95a4409758186bff21f7c24fde2ca80c637fca50cf1beabf83d036f9974249f]

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
      ~ hostname                                    = "c95a44097581" -> (known after apply)
      ~ id                                          = "c95a4409758186bff21f7c24fde2ca80c637fca50cf1beabf83d036f9974249f" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "my_tf_created_docker_container" -> "name_from_env" # forces replacement
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

docker_container.nginx: Destroying... [id=c95a4409758186bff21f7c24fde2ca80c637fca50cf1beabf83d036f9974249f]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 3s [id=959d13636b1543709ecada5743e969f49da02ccdf2f5d7f95f6730068785f25f]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
DevOps/terraform/docker on  lab4 [?] took 16.0s 
```

## 1.4

```bash
➜ terraform state list
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

```bash
➜ terraform state show yandex_compute_instance.vm-1
# yandex_compute_instance.vm-1:
resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T21:20:03Z"
    folder_id                 = "b1gmfdd1gnldod4ejkta"
    fqdn                      = "fhmmlgj9ecplrrovdbmi.auto.internal"
    id                        = "fhmmlgj9ecplrrovdbmi"
    metadata                  = {
        "user-data" = <<-EOT
            #cloud-config
            users:
              - name: diana
                groups: sudo
                shell: /bin/bash
                sudo: 'ALL=(ALL) NOPASSWD:ALL'
                ssh-authorized-keys:
                  - ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJtZr88I5bnb8hxEjdVbTDUvanq5nUS2WE391luVvybH tomilovediana@gmail.com
        EOT
    }
    name                      = "terraform1"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm6dtnma6kus42ej87k"
        disk_id     = "fhm6dtnma6kus42ej87k"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8autg36kchufhej85b"
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
        ip_address         = "192.168.10.19"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:16:ac:26:97"
        nat                = true
        nat_ip_address     = "62.84.113.190"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bfgr62slkacvcqc3fb"
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
➜  terraform output                                         
external_ip_address_vm_1 = "62.84.113.190"
internal_ip_address_vm_1 = "192.168.10.19"
```

## 2

```bash
➜ terraform state list
github_branch_default.main
github_branch_protection.default
github_repository.core-course-labs
```

```bash
➜ terraform state show github_repository.core-course-labs
# github_repository.core-course-labs:
resource "github_repository" "core-course-labs" {
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
            name      = "lab4"
            protected = false
        },
        {
            name      = "main"
            protected = false
        },
    ]
    default_branch              = "main"
    delete_branch_on_merge      = false
    etag                        = "W/\"8dffef980459d0d49d60b40c49054e5e8df5ca27bed8b0b6faeadde309699f68\""
    full_name                   = "sl1depengwyn/core-course-labs"
    git_clone_url               = "git://github.com/sl1depengwyn/core-course-labs.git"
    has_downloads               = true
    has_issues                  = false
    has_projects                = true
    has_wiki                    = true
    html_url                    = "https://github.com/sl1depengwyn/core-course-labs"
    http_clone_url              = "https://github.com/sl1depengwyn/core-course-labs.git"
    id                          = "core-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "core-course-labs"
    node_id                     = "R_kgDOKP1GRQ"
    private                     = false
    repo_id                     = 687687237
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:sl1depengwyn/core-course-labs.git"
    svn_url                     = "https://github.com/sl1depengwyn/core-course-labs"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
}
```

## Github Teams

```bash
➜ terraform state list
github_branch_default.main
github_repository.devops-lab4-teams
github_team.dev
github_team.devops
github_team_repository.dev_devops-lab4-teams
github_team_repository.devops_devops-lab4-teams
```

```bash
➜ terraform state show github_team_repository.dev_devops-lab4-teams
# github_team_repository.dev_devops-lab4-teams:
resource "github_team_repository" "dev_devops-lab4-teams" {
    etag       = "W/\"09273d3735e015fd736166efb7cffff969161c811e6a096737c4b98a2ca73a61\""
    id         = "8651062:devops-lab4-teams"
    permission = "push"
    repository = "devops-lab4-teams"
    team_id    = "8651062"
}
```

```bash
➜ terraform state show github_team_repository.devops_devops-lab4-teams
# github_team_repository.devops_devops-lab4-teams:
resource "github_team_repository" "devops_devops-lab4-teams" {
    etag       = "W/\"392124e853bd7bdaedf5c48889d8cfe41d0d0653d936a9ee52b23ddaef80d23e\""
    id         = "8651061:devops-lab4-teams"
    permission = "maintain"
    repository = "devops-lab4-teams"
    team_id    = "8651061"
}
```
