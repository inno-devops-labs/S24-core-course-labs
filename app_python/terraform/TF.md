## Terraform Output

### Name: docker_image.nginx

image_id = `sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffbnginx:latest`

### Name: docker_container.nginx
container_id = `12a9c28e73c980973e2c614b08feba60aaf911681859a5b50adcce70ea265492`

## Terrafotm State List

- docker_container.nginx
- docker_image.nginx

## Terraform State Show

### docker_image.nginx:
```hcl
resource "docker_image" "nginx" {
    id           = "sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffbnginx:latest"
    image_id     = "sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb"
}
```
### docker_container.nginx:
```hcl
resource "docker_container" "nginx" {
    attach                                      = false
    bridge                                      = null
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = null
    cpu_shares                                  = 0
    domainname                                  = null
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "12a9c28e73c9"
    id                                          = "12a9c28e73c980973e2c614b08feba60aaf911681859a5b50adcce70ea265492"
    image                                       = "sha256:28402db69fec7c17e179ea87882667f1e054391138f77ffaf0c3eb388efc3ffb"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "tutorial"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = null
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = null
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = null
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    user                                        = null
    userns_mode                                 = null
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = null

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
### After rename Docker container:

container_id = `c489cdf807d134b33e5f547dd949a44af15692b71f459606e2432d0d2e15cdff`
container_name = "Test"


## GitHub with Terraform

Inside folder `terraform/github` created configuration files for GitHub. After apply chages reposritory descriptions is "Terraform-managed repository". With help Terraform it is possible to build "infrastructate as a code" approach. For run ```terrafrom apply``` or ```terraform import``` commands it is need to pass GitHub token as an argument or make it is as an environment variable.