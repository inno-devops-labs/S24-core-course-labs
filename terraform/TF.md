# Docker

## terraform state show

### docker_container.dev-ops-labs

input command:
```bash
terraform state show docker_container.dev-ops-labs
```

output:
```bash
resource "docker_container" "dev-ops-labs" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "flask",
        "run",
        "--host=0.0.0.0",
    ]
    env                                         = []
    hostname                                    = "49d2d66be288"
    id                                          = "49d2d66be2883fbdfa09100f3c2707cb30dfc2018bd7c34de8e95f895139bbea"
    image                                       = "sha256:a9fb8bad1de196be02a885007d719c582dc44f1a040c42648792383c3ac68e08"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "dev-ops-labs"
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
    user                                        = "flask:flask"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### docker_image.dev-ops-labs

input command:

```bash
terraform state show docker_image.dev-ops-labs
```

output:

```bash
resource "docker_image" "dev-ops-labs" {
    id           = "sha256:a9fb8bad1de196be02a885007d719c582dc44f1a040c42648792383c3ac68e08glebuben/dev-ops-labs:latest"
    image_id     = "sha256:a9fb8bad1de196be02a885007d719c582dc44f1a040c42648792383c3ac68e08"
    keep_locally = false
    name         = "glebuben/dev-ops-labs:latest"
    repo_digest  = "glebuben/dev-ops-labs@sha256:cd39fb1bc96c8ac351318ba108be64d9b55d2be43c041641c1f8426feca417f1"
}
```

## terraform state list

input command:

```bash
terraform state list
```

output:

```bash
docker_container.dev-ops-labs
docker_image.dev-ops-labs
```

## terraform output

input command:

```bash
terraform output
```

output:

```bash
container_id = "49d2d66be2883fbdfa09100f3c2707cb30dfc2018bd7c34de8e95f895139bbea"
image_id = "sha256:a9fb8bad1de196be02a885007d719c582dc44f1a040c42648792383c3ac68e08glebuben/dev-ops-labs:latest"
```

# Timeweb

## terraform state show

### twc_server.example-server

input command:

```bash
terraform state show twc_server.example-server
```

output:

```bash
resource "twc_server" "example-server" {
    availability_zone = "spb-2"
    boot_mode         = "std"
    configurator_id   = 11
    cpu               = 1
    cpu_frequency     = "3.3"
    disks             = [
        {
            id          = 16801165
            is_mounted  = true
            is_system   = true
            size        = 10240
            status      = "done"
            system_name = "vda"
            type        = "nvme"
            used        = 0
        },
    ]
    id                = "2600917"
    is_ddos_guard     = false
    location          = "ru-1"
    main_ipv4         = "91.210.171.97"
    name              = "Example server"
    networks          = [
        {
            bandwidth     = 200
            ips           = [
                {
                    ip      = "2a03:6f00:5:1::eb7"
                    is_main = true
                    ptr     = ""
                    type    = "ipv6"
                },
                {
                    ip      = "91.210.171.97"
                    is_main = true
                    ptr     = ""
                    type    = "ipv4"
                },
            ]
            is_ddos_guard = false
            nat_mode      = ""
            type          = "public"
        },
    ]
    os                = [
        {
            id      = 79
            name    = "ubuntu"
            version = "22.04"
        },
    ]
    os_id             = 79
        ram             = 1024
    }
}
```

### data.twc_os.os

input command:

```bash
terraform state show data.twc_os.os
```

output:

```bash
data "twc_os" "os" {           
    family           = "linux" 
    id               = "79"    
    name             = "ubuntu"
    version          = "22.04" 
    version_codename = "jammy" 
                               
    requirements {             
        bandwidth_min = 0      
        cpu_min       = 0      
        disk_min      = 0      
        ram_min       = 0      
    }                          
}     
```

### data.twc_os.os

input command:

```bash
terraform state show data.twc_configurator.configurator
```

output:

```bash
terraform state show data.twc_configurator.configurator
        network_bandwidth_max  = 1000
        network_bandwidth_min  = 200
        network_bandwidth_step = 100
        ram_max                = 747520
        ram_min                = 1024
        ram_step               = 1024
    }
}
```

## terraform state list

input command:

```bash
terraform state list
```

output:

```bash
data.twc_configurator.configurator
data.twc_os.os
twc_server.example-server
```

## terraform output

input command:
```bash
terraform output
```

output:
```bash
main_ipv4 = "91.210.171.97"
```

# Best practices

## Modularization
Organize your Terraform code into separate files for providers, resources, variables, and outputs to enhance maintainability and readability.

## Parameterization
Utilize variables to parameterize your infrastructure configurations, promoting reusability and flexibility.

## Documentation
Document resources, variables, and outputs with clear descriptions to facilitate understanding and collaboration among team members.

## Provider Versioning
Specify provider versions with version constraints to ensure consistency and predictability in deployments.

## Dependency Management
Properly manage dependencies between resources to ensure that resources are provisioned in the correct order.

## Output Exposition
Expose important information such as resource IDs or IP addresses as outputs to enable easy retrieval and integration with other systems.

## Configuration Options
Utilize configuration options provided by providers to tailor resources to specific requirements or environments.

## Security Measures
Safeguard sensitive information such as access tokens or passwords by storing them in environment variables instead of hardcoding them in Terraform files.
```bash
export TWC_TOKEN=...
export GITHUB_TOKEN=...
```