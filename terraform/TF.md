# Terraform

Result of 
```bash 
terraform state show docker_container.app_python
```

### docker_container.app_python:
```bash
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "/bin/sh",
        "-c",
        "python3 app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "370b43ad8d32"
    id                                          = "370b43ad8d32828b42ceb983c1fbb1c863148512bffaf962a8a61ee71a798c97"
    image                                       = "sha256:1f5aad33cf78eba92e529617963ac6a4f126aa2bdb715399f37a6ae617a740dc"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "anton_nekhaev_flask"
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
    stop_signal                                 = "SIGKILL"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "anton"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    healthcheck {
        interval     = "0s"
        retries      = 0
        start_period = "0s"
        test         = [
            "CMD-SHELL",
            "curl --fail http://localhost:5001/health || exit 1",
        ]
        timeout      = "0s"
    }

    ports {
        external = 5001
        internal = 5001
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

Result of 
```bash 
terraform state show docker_image.app
```

### docker_image.app_python:
```bash
resource "docker_image" "app_python" {
    id           = "sha256:1f5aad33cf78eba92e529617963ac6a4f126aa2bdb715399f37a6ae617a740dcnad777/anton_nekhaev_flask"
    image_id     = "sha256:1f5aad33cf78eba92e529617963ac6a4f126aa2bdb715399f37a6ae617a740dc"
    keep_locally = false
    name         = "nad777/anton_nekhaev_flask"
    repo_digest  = "nad777/anton_nekhaev_flask@sha256:6fd68117445fe875931233c16cccdbe859a03a70d340668b4909f32b0fb56668"
}

```

Result of 
```bash 
terraform state list
```
```bash
docker_container.app_python
docker_image.app_python
```

Result of 
```bash
terraform output
```

```bash
container_id = "370b43ad8d32828b42ceb983c1fbb1c863148512bffaf962a8a61ee71a798c97"
image_id = "sha256:1f5aad33cf78eba92e529617963ac6a4f126aa2bdb715399f37a6ae617a740dcnad777/anton_nekhaev_flask"
```

### Best practices

I have implemented several best practices:
- The code was formatted using IDE for better readability
- Utilization of `terraform.tfvars` file to store sensitive data (tokens and etc)
- Separate logic into `main.tf` and `variables.tf`