# Terraform 

## Docker
* Command `terraform state list` gives the following:

```
$ terraform state list
docker_container.app_python_container
docker_image.app_python_image
```

* command `terraform state show docker_container.app_python_container`:

```
$ terraform state show docker_container.app_python_container
# docker_container.app_python_container:
resource "docker_container" "app_python_container" {
    attach                                      = false
    command                                     = [
        "python",
        "src/app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "a6cca2a1e9e6"
    id                                          = "a6cca2a1e9e60ea34198b507a5f78afbae5acc91914ce468c0aabd90b15b49dc"
    image                                       = "sha256:1ab02b2d335c73d656be3262cc373cb142797d8a291d71701e248350c25b6f90"
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
    user                                        = "python:python"
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
```

* command `terraform state show docker_image.app_python_image`:
```
$ terraform state show docker_image.app_python_image
# docker_image.app_python_image:
resource "docker_image" "app_python_image" {
    id           = "sha256:1ab02b2d335c73d656be3262cc373cb142797d8a291d71701e248350c25b6f90sokolofff/app_python"
    image_id     = "sha256:1ab02b2d335c73d656be3262cc373cb142797d8a291d71701e248350c25b6f90"
    keep_locally = false
    name         = "sokolofff/app_python"
    repo_digest  = "sokolofff/app_python@sha256:33379e57597f3eac8e023bb0063c1dcdae0dc4354e8f41d95a734ef60b4a7375"
}
```

* command `terraform output`:

```
$ terraform output
container_id = "a6cca2a1e9e60ea34198b507a5f78afbae5acc91914ce468c0aabd90b15b49dc"
container_name = "app_python"
image_id = "sha256:1ab02b2d335c73d656be3262cc373cb142797d8a291d71701e248350c25b6f90sokolofff/app_python"
image_name = "sokolofff/app_python"
```

* command `terraform apply`:

```
$ terraform apply
docker_image.app_python_image: Refreshing state... [id=sha256:1ab02b2d335c73d656be3262cc373cb142797d8a291d71701e248350c25b6f90sokolofff/app_python]
docker_container.app_python_container: Refreshing state... [id=a6cca2a1e9e60ea34198b507a5f78afbae5acc91914ce468c0aabd90b15b49dc]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_python_container must be replaced
-/+ resource "docker_container" "app_python_container" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "python",
          - "src/app.py",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "a6cca2a1e9e6" -> (known after apply)
      ~ id                                          = "a6cca2a1e9e60ea34198b507a5f78afbae5acc91914ce468c0aabd90b15b49dc" -> (known after apply)
      ~ image                                       = "sha256:1ab02b2d335c73d656be3262cc373cb142797d8a291d71701e248350c25b6f90" -> "sokolofff/app_python" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "app_python"
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
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "python:python" -> null
      - working_dir                                 = "/app" -> null
        # (13 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id   = "a6cca2a1e9e60ea34198b507a5f78afbae5acc91914ce468c0aabd90b15b49dc" -> (known after apply)
```

## GitHub
### New repo
After running command, [new repo](https://github.com/SokolOFFF/S23-DevOps-Terraform) created.

### Import 
```angular2html
$ terraform import github_repository.S23-DevOps-Terraform "S23-DevOps-Terraform"
github_repository.S23-DevOps-Terraform: Importing from ID "S23-DevOps-Terraform"...
github_repository.S23-DevOps-Terraform: Import prepared!
  Prepared github_repository for import
╷
│ Error: Resource already managed by Terraform
│
│ Terraform is already managing a remote object for
│ github_repository.S23-DevOps-Terraform. To import to this address you must
│ first remove the existing object from the state.
╵
```