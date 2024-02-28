# Lab 4

## Outputs for Docker Infrastructure

```bash
terraform state list

docker_container.app_container
docker_image.app_image
docker_tag.app_tag
```

```bash
terraform state show docker_container.app_container

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
    hostname                                    = "3d02f68c621c"
    id                                          = "3d02f68c621cec8dca6b52def695436a46ef6fcebf25a5be20a17c7be1149410"
    image                                       = "sha256:2161b0e81c71798fc1a8e98ec14439bb268ee4012f35ad599bf67e620618d952"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "sapushha_flask_app"
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
    user                                        = "sapushha"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    labels {
        label = "description"
        value = "Web Application that displays the current Moscow time"
    }
    labels {
        label = "maintainer"
        value = "sapushha"
    }

    ports {
        external = 8080
        internal = 8080
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```bash
terraform state show docker_image.app_image

# docker_image.app_image:
resource "docker_image" "app_image" {
    id           = "sha256:2161b0e81c71798fc1a8e98ec14439bb268ee4012f35ad599bf67e620618d952sapushha/sapushha_flask_app"
    image_id     = "sha256:2161b0e81c71798fc1a8e98ec14439bb268ee4012f35ad599bf67e620618d952"
    keep_locally = false
    name         = "sapushha/sapushha_flask_app"

    build {
        cache_from   = []
        context      = "..\\..\\"
        dockerfile   = "Dockerfile"
        extra_hosts  = []
        remove       = true
        security_opt = []
        tag          = []
    }
}
```

```bash
terraform output

container_id = "3d02f68c621cec8dca6b52def695436a46ef6fcebf25a5be20a17c7be1149410"
```

## Outputs for Github Infrastructure

bebebe

## Outputs for Yandex Cloud Infrastructure

bebebe

## Best Practices I applied

### Version Constraints:

The terraform block includes a version constraint for the docker provider,
specifying that version ~> 3.0.1 is required. This ensures compatibility and
allows Terraform to automatically select compatible provider versions within
the specified range.

### Separate Provider Configuration:

The provider configuration for docker is placed in a separate block, improving
readability and maintainability of the Terraform configuration.

### Descriptive Resource Names:

The resource names docker_image.app_image, docker_container.app_container, and
docker_tag.app_tag are descriptive and provide clear indications of their
purpose. This improves the readability and understandability of the Terraform
configuration.

### Relative Paths:

The context parameter in the docker_image resource uses a relative path (
..\\..\\) to specify the build context. Using relative paths instead of
absolute paths ensures portability across different environments.

### Resource Dependencies:

The docker_container.app_container resource depends on the
docker_image.app_image resource. This ensures that the image is built before
the container is created, maintaining the correct order of resource creation.

### Resource Variables:

The docker_container.app_container resource references the
docker_image.app_image.name variable to specify the image. This allows passing
information between resources and ensures consistency.
