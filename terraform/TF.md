# Terraform

## Best practices


## Outputs

### Docker

- `terraform apply`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
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
      + name                                        = "moscow-time-app"
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
  # docker_image.app will be created
  + resource "docker_image" "app" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "damirafliatonov/moscow-time-app:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.app: Creating...
docker_image.app: Still creating... [10s elapsed]
docker_image.app: Still creating... [20s elapsed]
docker_image.app: Still creating... [30s elapsed]
docker_image.app: Still creating... [40s elapsed]
docker_image.app: Still creating... [50s elapsed]
docker_image.app: Creation complete after 1m0s [id=sha256:4abe7f29f5c612b8f18e8fac0d55c976a4ee62643440b030d3df990fa02d4bfcdamirafliatonov/moscow-time-app:latest]
docker_container.app: Creating...
docker_container.app: Creation complete after 0s [id=d4977a26c3277965331b19e86bfd1e194482cf11d9ee62052ffdf7486f971f7e]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

- `terraform state list`

```
docker_container.app
docker_image.app
```

- `terraform state show docker_container.app`

```
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = [
        "./main",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "d4977a26c327"
    id                                          = "d4977a26c3277965331b19e86bfd1e194482cf11d9ee62052ffdf7486f971f7e"
    image                                       = "sha256:4abe7f29f5c612b8f18e8fac0d55c976a4ee62643440b030d3df990fa02d4bfc"     
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow-time-app"
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
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

- `terraform state show docker_image.app`

```
# docker_image.app:
resource "docker_image" "app" {
    id           = "sha256:4abe7f29f5c612b8f18e8fac0d55c976a4ee62643440b030d3df990fa02d4bfcdamirafliatonov/moscow-time-app:latest"
    image_id     = "sha256:4abe7f29f5c612b8f18e8fac0d55c976a4ee62643440b030d3df990fa02d4bfc"
    keep_locally = false
    name         = "damirafliatonov/moscow-time-app:latest"
    repo_digest  = "damirafliatonov/moscow-time-app@sha256:8a81526aa332719c7d889d03ab353b8b028c08816aaa7e125a3b86cc1f543caa"    
}
```

- `terraform output`

```
container_id = "d4977a26c3277965331b19e86bfd1e194482cf11d9ee62052ffdf7486f971f7e"
image_id = "sha256:4abe7f29f5c612b8f18e8fac0d55c976a4ee62643440b030d3df990fa02d4bfcdamirafliatonov/moscow-time-app:latest"
```

### Yandex cloud

- `terraform apply`

```
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Still creating... [30s elapsed]
yandex_compute_instance.vm-1: Creation complete after 32s [id=fhmsc8jf6lf49ubejd3r]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed
```

- `terraform state list`

```
yandex_compute_disk.boot-disk-1
yandex_compute_instance.vm-1
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### Github

- `terraform apply`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following  
symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "devops-example"
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
      + repository_id                   = "devops-example"
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
github_branch_default.main: Creation complete after 2s [id=devops-example]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 5s [id=BPR_kwDOLY7o9s4C0xah]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```
