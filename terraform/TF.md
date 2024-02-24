# Terraform

## Terraform best practices

* Separate terraform files by their responsibility: providers, variables, network, outputs, etc.
* Split files by scopes of work (GitHub, Cloud, Docker)
* Preserve one variable naming style (e.g. snake_case)
* Use `terraform fmt` to keep configs consistent
* Use `terraform validate` to keep configs correct

## Docker

### Terraform state list

```shell
(venv) shredding@SHREDDING-2 docker % terraform state list

docker_container.nginx
docker_image.nginx
```

### Terraform state show

```shell
(venv) shredding@SHREDDING-2 docker % terraform state show docker_container.nginx
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "0ee72062e62a"
    id                                          = "0ee72062e62aa72c19999b7f0ebcee3a9d25662920c0784510060eb86529b6ef"
    image                                       = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "ExampleNginxContainer"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Terraform outputs
```shell
(venv) shredding@SHREDDING-2 docker % terraform output                           
container_id = "0ee72062e62aa72c19999b7f0ebcee3a9d25662920c0784510060eb86529b6ef"
image_id = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676nginx:latest"
```