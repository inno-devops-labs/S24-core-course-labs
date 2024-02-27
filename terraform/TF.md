# Terraform

## Docker

`terraform show`:

```
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "uvicorn",
        "app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = []
    env                                         = []
    group_add                                   = []
    hostname                                    = "b82ebec52aeb"
    id                                          = "b82ebec52aeb94df3c872ee36e586ba782e9ffe56d7169a7985c0abee084e9a9"
    image                                       = "sha256:4c911da08925c632ae835297a678ba6d6206da66d52d9026e750b226dfa334d1"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devops"
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
    storage_opts                                = {}
    sysctls                                     = {}
    tmpfs                                       = {}
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:4c911da08925c632ae835297a678ba6d6206da66d52d9026e750b226dfa334d1vladdan16/app_python"
    image_id     = "sha256:4c911da08925c632ae835297a678ba6d6206da66d52d9026e750b226dfa334d1"
    keep_locally = false
    name         = "vladdan16/app_python"
    repo_digest  = "vladdan16/app_python@sha256:3891e451b5b6ff055e422495bd4a92bd9fd2355fce60992071a013f6b1741f60"
}


Outputs:

container_id = "b82ebec52aeb94df3c872ee36e586ba782e9ffe56d7169a7985c0abee084e9a9"
image_id = "sha256:4c911da08925c632ae835297a678ba6d6206da66d52d9026e750b226dfa334d1vladdan16/app_python"
```

`terraform state list`:

```
docker_container.app_python
docker_image.app_python
```

Log after applying changes

```
docker_image.app_python: Refreshing state... [id=sha256:4c911da08925c632ae835297a678ba6d6206da66d52d9026e750b226dfa334d1vladdan16/app_python]
docker_container.app_python: Refreshing state... [id=b82ebec52aeb94df3c872ee36e586ba782e9ffe56d7169a7985c0abee084e9a9]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_python must be replaced
-/+ resource "docker_container" "app_python" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "uvicorn",
          - "app:app",
          - "--host",
          - "0.0.0.0",
          - "--port",
          - "8000",
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
      ~ hostname                                    = "b82ebec52aeb" -> (known after apply)
      ~ id                                          = "b82ebec52aeb94df3c872ee36e586ba782e9ffe56d7169a7985c0abee084e9a9" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "devops"
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
      - working_dir                                 = "/app" -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ external = 8080 -> 8081 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id = "b82ebec52aeb94df3c872ee36e586ba782e9ffe56d7169a7985c0abee084e9a9" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_python: Destroying... [id=b82ebec52aeb94df3c872ee36e586ba782e9ffe56d7169a7985c0abee084e9a9]
docker_container.app_python: Destruction complete after 1s
docker_container.app_python: Creating...
docker_container.app_python: Creation complete after 0s [id=9cfb2ba8ca12d9fa733ed816fd6b16490061fe58f7e78083f2b878990347bba7]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "9cfb2ba8ca12d9fa733ed816fd6b16490061fe58f7e78083f2b878990347bba7"
image_id = "sha256:4c911da08925c632ae835297a678ba6d6206da66d52d9026e750b226dfa334d1vladdan16/app_python"
```

## Best practices

* store configuration for terraform in several files
* secure personal access tokens

