<code>terraform state show docker_container.custom_container</code>
```
# docker_container.custom_container:
resource "docker_container" "custom_container" {
    attach                                      = false
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "7749629e319f"
    id                                          = "7749629e319fd120a3ffd8067f04149ad68b26237ccee47de13674b2614f785235fa7587"
    image                                       = "sha256:a4784ab66ad5990ed7664047b93db42bee27e3087d13630f79609c63a27ab6cb"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "terraform-lab4"
    network_data                                = [
        {
            gateway                   = "192.168.1.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "192.168.1.10"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "00:1A:2B:3C:4D:5E"
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

<code>terraform state show docker_image.custom_image</code>
```
# docker_image.custom_image:
resource "docker_image" "custom_image" {
    id          = "sha256:a4784ab66ad5990ed7664047b93db42bee27e3087d13630f79609c63a27ab6cbi.ezhova/lab2"
    image_id    = "sha256:a4784ab66ad5990ed7664047b93db42bee27e3087d13630f79609c63a27ab6cb"
    name        = "i.ezhova/lab2"
    repo_digest = "i.ezhova/lab2@sha256:99a8657748e96665fb1f051a97717fdbd6a5694efd61a538a2f4c857c0e46a6c"
}
```
<code>terraform state list</code>
```
docker_container.custom_container
docker_image.custom_image
```

## Changes Applied:

```terraform apply```

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.custom_container will be created
  + resource "docker_container" "custom_container" {
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
      + image                                       = "i.ezhova/lab2"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "terraform-lab4"
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
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.custom_image will be created
  + resource "docker_image" "custom_image" {
      + id          = (known after apply)
      + image_id    = (known after apply)
      + name        = "i.ezhova/lab2"
      + repo_digest = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + id_of_container    = (known after apply)
  + image_of_container = "i.ezhova/lab2"
  + name_of_container  = "terraform-lab4"
  + port_of_container  = [
      + {
          + external = 8000
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        },
    ]
```
## Output
```
id_of_container = "3f8a2c6d9e5b4a7f1d0e2c9b7a3f5e4d7c8b9a0f1e2d3c4a5b6d9e8f7a4b5"
image_of_container = "i.ezhova/lab2"
name_of_container = "terraform-lab4"
port_of_container = tolist([
  {
    "external" = 8000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```