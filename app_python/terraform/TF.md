# Terraform Best practices

1. **Descriptive Naming**: Use meaningful names for resources, variables, and outputs to enhance readability and maintainability. For instance, `name_image` instead of `name`, and `container_id` instead of `id`.

2. **Version Pinning**: Specify exact or constrained versions for providers and modules to ensure reproducibility and prevent unexpected changes. For example, `version = "~> 3.0.1"` for the Docker provider.

3. **Variable Documentation**: Provide clear descriptions for variables in `vars.tf` to aid understanding and usage. This helps collaborators and future maintainers comprehend the purpose of each variable.

4. **Separation of Concerns**: Organize resources, variables, and outputs into separate files (`main.tf`, `vars.tf`, `output.tf`) for better organization and maintainability. This separation clarifies the purpose of each file and makes it easier to locate specific components.

5. **Immutable Infrastructure**: Set `keep_locally = false` for Docker images to promote immutable infrastructure practices. This ensures consistent deployment environments and reduces the risk of unintended changes.

6. **Resource Dependency Management**: Ensure correct dependency management, such as `docker_container.nginx` depending on `docker_image.nginx`, to guarantee that resources are provisioned in the correct order and dependencies are satisfied appropriately.

## Outputs | Docker

`terraform state list`

```text
docker_container.nginx
docker_image.nginx
```

`terraform state show docker_container.nginx`

```text
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "flask",
        "run",
        "--host=0.0.0.0",
        "--port=5000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "201dd5e9bd47"
    id                                          = "201dd5e9bd478b8b3aa1c5b22f6fb86265185c56b5516f6616c264b5e8e28c43"
    image                                       = "sha256:49f3d80bb32bfe2d42d9578751c949a1be1484c2ee355daf756eb22b7ac5c917"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "webapp"
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
    user                                        = "testUser"
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


`terraform state show docker_image.nginx`

```text
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:49f3d80bb32bfe2d42d9578751c949a1be1484c2ee355daf756eb22b7ac5c917orillion1/lab2:latest"
    image_id     = "sha256:49f3d80bb32bfe2d42d9578751c949a1be1484c2ee355daf756eb22b7ac5c917"
    keep_locally = false
    name         = "orillion1/lab2:latest"
    repo_digest  = "orillion1/lab2@sha256:78713f7599e3b2db2ec40f3cb4cceed0e240ce39d8246ecbff079ad8bd10bd94"
}
```



`terraform output`

```text
container_id = "201dd5e9bd478b8b3aa1c5b22f6fb86265185c56b5516f6616c264b5e8e28c43"
image_id = "sha256:49f3d80bb32bfe2d42d9578751c949a1be1484c2ee355daf756eb22b7ac5c917orillion1/lab2:latest"
```


## Outputs | Yandex Cloud

`terraform state list`

```text
yandex_compute_disk.boot-disk
yandex_compute_image.default
yandex_compute_instance.default
yandex_vpc_network.default
yandex_vpc_subnet.default
```

`terraform apply`

```text
Apply complete! Resources: 2 added, 0 changed, 2 destroyed.

Outputs:

address = "158.160.117.23"
```
