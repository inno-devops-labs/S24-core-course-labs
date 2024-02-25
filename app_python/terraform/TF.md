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

<code>terraform output</code>
```
container_id = "124f05601c1e99400b087525cd5cdb1dfb158d8c3206e2f16089f8072c9cdf34"
```

# Terraform Best Practices Documentation

This TF.md file outlines best practices that have been applied to the management of Terraform configurations within this project. These practices aim to ensure that our configurations are manageable, version-controlled, and well-organized across different platforms such as GitHub, Docker, and Yandex Cloud.

## Organized Directory Structure

- Each Terraform configuration is organized by its respective platform within a dedicated directory.
- Directory names are clearly labeled to correspond to the specific service they configure (e.g., github/, docker/, cloud-terraform/).

## Separated Configuration Files

- Terraform configurations are split into multiple files for better readability and maintenance:
  - versions.tf to specify the Terraform version and required provider versions.
  - main.tf to contain the main set of resources that are being provisioned.
  - providers.tf to configure the providers which interact with the specified services.
  - Additional files like variables.tf, outputs.tf, and data.tf are used as needed to define variables, outputs, and data sources respectively.

## Versioning

- Version constraints are used to guarantee compatibility and stability within our Terraform configurations:
  - The required_version parameter within versions.tf is set to lock the Terraform CLI to a specific version range.
  - Provider versions are pinned using the version argument inside the required_providers block to prevent unexpected changes.

## Infrastructure as Code (IaC) Principles

- IaC principles have been implemented, treating infrastructure changes with the same level of scrutiny as application code.
- Changes are made through version-controlled Terraform files, ensuring an audit trail for modifications and changes.

By adhering to these best practices, the project's Terraform configurations are intended to be transparent, reliable, and maintainable. We continually seek to improve these practices, adapting to new features, services, and tools as they become available in the wider Terraform ecosystem.
