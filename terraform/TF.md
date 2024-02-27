# Docker infrestructure with Terraform

## Output of `terraform state show docker_container.app_python`:

```
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "python3",
        "-m",
        "flask",
        "run",
        "--host",
        "0.0.0.0",
        "--port",
        "5000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "37422d5acdc8"
    id                                          = "37422d5acdc8d0376951a93ea7453759f6a27278caae83615ff168ab5c308bd2"
    image                                       = "sha256:814d3260a89cabe69db01360dda47061ffd98fbf147f523fca669909c4cd1c28"
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
    working_dir                                 = "/app_python"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

## Output of `terraform state show docker_image.app_python`:

```
resource "docker_image" "app_python" {
    id           = "sha256:814d3260a89cabe69db01360dda47061ffd98fbf147f523fca669909c4cd1c28almetovkamil/app_python:v1"
    image_id     = "sha256:814d3260a89cabe69db01360dda47061ffd98fbf147f523fca669909c4cd1c28"
    keep_locally = false
    name         = "almetovkamil/app_python:v1"
    repo_digest  = "almetovkamil/app_python@sha256:fb78c4eafbeda104ff0617e068fef0943b85df61830579bff5a439545bf4d604"
}
```

## Output of `terraform state list`

```
docker_container.app_python
docker_image.app_python
```

## Document a part of the log with the applied changes.

???

## Utilize input variables to rename your Docker container.

To do it, you can execute the following command:

```
terraform apply -var "container_name=NewContainerName"
```

After that, you can see (using `docker ps`) that the container has new name: **NewContainerName**

```
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                    NAMES
42b3196bbfab   814d3260a89c   "python3 -m flask ru…"   3 minutes ago   Up 3 minutes   0.0.0.0:5000->5000/tcp   NewContainerName
```

## Output of `terraform output`

```
container_id = "42b3196bbfabc850ca1127fc0406b17688640d09cfb08492bc78ce2f46610b79"
image_id = "sha256:814d3260a89cabe69db01360dda47061ffd98fbf147f523fca669909c4cd1c28almetovkamil/app_python:v1"
```
