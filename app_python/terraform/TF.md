<code> terraform state show docker_container.app_container </code>

```
# docker_container.app_container:
resource "docker_container" "app_container" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "flask",
        "run",
        "--host",
        "0.0.0.0",
        "--port",
        "8080",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "2e43bf6c8e80"
    id                                          = "2e43bf6c8e8080ac43cb936a49e5fd230de7ca6e9874762f3ead63c650587799"
    image                                       = "sha256:697087bf51849fdf20b0267a9fbfa7c4a391ed83a7dc168876bc8f1447fa9c17"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow_time_web_app"
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
    user                                        = "user"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    labels {
        label = "description"
        value = "WebApp showing current Moscow time"
    }
    labels {
        label = "maintainer"
        value = "rmolochko"
    }
    labels {
        label = "version"
        value = "1.0"
    }

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

<code>terraform state show docker_image.app_image</code>
```

# docker_image.app_image:
resource "docker_image" "app_image" {
    id           = "sha256:697087bf51849fdf20b0267a9fbfa7c4a391ed83a7dc168876bc8f1447fa9c17rmoll/moscow_time_web_app"
    image_id     = "sha256:697087bf51849fdf20b0267a9fbfa7c4a391ed83a7dc168876bc8f1447fa9c17"
    keep_locally = false
    name         = "rmoll/moscow_time_web_app"

    build {
        build_arg       = {}
        build_args      = {}
        cache_from      = []
        context         = "../../"
        cpu_period      = 0
        cpu_quota       = 0
        cpu_shares      = 0
        dockerfile      = "Dockerfile"
        extra_hosts     = []
        force_remove    = false
        label           = {}
        labels          = {}
        memory          = 0
        memory_swap     = 0
        no_cache        = false
        pull_parent     = false
        remove          = true
        security_opt    = []
        shm_size        = 0
        squash          = false
        suppress_output = false
        tag             = []
    }
}
```

<code>terraform state list</code>
```
docker_container.app_container
docker_image.app_image
```
