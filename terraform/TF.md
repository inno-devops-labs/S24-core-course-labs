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
    hostname                                    = "f7a95d57eb51"
    id                                          = "f7a95d57eb51a4cda7414fe1025ec6e45492b67ccfef11e1800f106840f05d49"
    image                                       = "sha256:ce742cdc2cabfc920f587c004560300e5367a3585a4272225a31827bce0cf749"
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
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:03"
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
    id          = "sha256:ce742cdc2cabfc920f587c004560300e5367a3585a4272225a31827bce0cf749furryowolord/lab2"
    image_id    = "sha256:ce742cdc2cabfc920f587c004560300e5367a3585a4272225a31827bce0cf749"
    name        = "furryowolord/lab2"
    repo_digest = "furryowolord/lab2@sha256:99a8657748e96665fb1f051a97717fdbd6a5694efd61a538a2f4c857c0e46a6c"
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
      + image                                       = "furryowolord/lab2"
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
      + name        = "furryowolord/lab2"
      + repo_digest = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + id_of_container    = (known after apply)
  + image_of_container = "furryowolord/lab2"
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
id_of_container = "7cde3276fa45490d2dee9a3ec2715347db3b415da30cb2d5f4eb9153e6be982a"
image_of_container = "furryowolord/lab2"
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