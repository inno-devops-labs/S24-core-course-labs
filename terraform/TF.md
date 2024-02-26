# Best practices

# Commands Output

## Docker

```console
$ terraform state list
docker_container.app
docker_image.app
```

```console
$ terraform state show docker_container.app
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python",
        "app.py",
    ]
    env                                         = []
    hostname                                    = "476df821c902"
    id                                          = "476df821c902003b67fb47876217ccc8b148d5a11c8008883df38a694a1180df"
    image                                       = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981c"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscowtime-web-app"
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
        external = 8000
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```console
$ terraform state show docker_image.app
# docker_image.app:
resource "docker_image" "app" {
    id           = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981cnabuki/moscowtime-web:latest"
    image_id     = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981c"
    keep_locally = false
    name         = "nabuki/moscowtime-web:latest"
    repo_digest  = "nabuki/moscowtime-web@sha256:b6cf9958dab002926aae0b956ff2f6a4c23a73ba47dbe79fdf6eb29be3d145f3"
}
```

```console
$ terraform output
container_id = "476df821c902003b67fb47876217ccc8b148d5a11c8008883df38a694a1180df"
image_id = "sha256:a9eee15f45da3b91fe22a0fc15b35db6134a4bb5dbbfc08b71e4c94c3a36981cnabuki/moscowtime-web:latest"
```