## terraform state show docker_container.dev-ops-course-app-python

docker_container.dev-ops-course-app-python:
resource "docker_container" "dev-ops-course-app-python" {
    attach                                      = false
    command                                     = [
        "venv/bin/uvicorn",
        "src.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "80",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "018548e2f570"
    id                                          = "018548e2f57035b95498a2dbcab465d0b5962aa6a56c04613fffc5ca0cb15db1"
    image                                       = "sha256:acba2d08082ffaeb12188e168822cf72704a2d736be888af7deabf3c361613f2"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "dev-ops-course-app-python"
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
    working_dir                                 = "/home/user"

    ports {
        external = 80
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}


## terraform state list
docker_container.dev-ops-course-app-python

## terraform output
container_id = "018548e2f57035b95498a2dbcab465d0b5962aa6a56c04613fffc5ca0cb15db1"
container_name = "dev-ops-course-app-python"
