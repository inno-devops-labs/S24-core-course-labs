# Best practices

* **Specify Terraform Version and Providers:** Always specify the required Terraform version and providers in your configuration.
* **Secure GitHub Provider Token:** To enhance security, store GitHub provider token in a separate file and reference it in configuration.
* **Use Variables and Resource Attributes:** Avoid hard coding values in Terraform configuration. Instead, use variables and resource attributes to reference values.
* **Format Code According to Standards:** Use formatting standards to enhance readability and maintainability. Use consistent indentation, spacing, and naming conventions for a more organized and understandable codebase.


# Task 1.3

## Output of `terraform state show`:

```bash
# docker_container.wonderful_wiles:
resource "docker_container" "wonderful_wiles" {
    attach                                      = false
    command                                     = [
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python",
    ]
    env                                         = []
    hostname                                    = "c8f9afb5c761"
    id                                          = "c8f9afb5c761ffee0681addebc49edf1f25ae9a267021a7959179fba2ada6161"
    image                                       = "sha256:05947a1da17a56d66908467c2097413ab9bc4405e96013708082ffd9914e0243"
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
    user                                        = "app"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8080
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app-flask:
resource "docker_image" "app-flask" {
    id           = "sha256:05947a1da17a56d66908467c2097413ab9bc4405e96013708082ffd9914e0243app-flask:latest"
    image_id     = "sha256:05947a1da17a56d66908467c2097413ab9bc4405e96013708082ffd9914e0243"
    keep_locally = false
    name         = "app-flask:latest"
}
```


## Output of `terraform state list`:

```bash
docker_container.wonderful_wiles
docker_image.app-flask
```

## Outputs of changes:
```bash
docker_image.app-flask: Refreshing state... [id=sha256:05947a1da17a56d66908467c2097413ab9bc4405e96013708082ffd9914e0243app-flask:latest]
docker_container.wonderful_wiles: Refreshing state... [id=c3d31603cb77f8629f26918de3726a29e02943a4c92cf3249d899c3880db249d]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:        
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.wonderful_wiles must be replaced
-/+ resource "docker_container" "wonderful_wiles" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "app.py",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "python",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "c3d31603cb77" -> (known after apply)
      ~ id                                          = "c3d31603cb77f8629f26918de3726a29e02943a4c92cf3249d899c3880db249d" -> (known after apply)   
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "tutorial"
      ~ network_data                                = [
          - {
              - gateway                   = "172.17.0.1"
              - global_ipv6_address       = ""
              - global_ipv6_prefix_length = 0
              - ip_address                = "172.17.0.2"
              - ip_prefix_length          = 16
              - ipv6_gateway              = ""
              - mac_address               = "02:42:ac:11:00:02"
              - network_name              = "bridge"
            },
        ] -> (known after apply)
      - network_mode                                = "default" -> null
      - privileged                                  = false -> null
      - publish_all_ports                           = false -> null
      ~ runtime                                     = "runc" -> (known after apply)
      ~ security_opts                               = [] -> (known after apply)
      ~ shm_size                                    = 64 -> (known after apply)
      + stop_signal                                 = (known after apply)
      ~ stop_timeout                                = 0 -> (known after apply)
      - storage_opts                                = {} -> null
      - sysctls                                     = {} -> null
      - tmpfs                                       = {} -> null
      - user                                        = "app" -> null
      - working_dir                                 = "/app_python" -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ external = 8080 -> 8000 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.wonderful_wiles: Destroying... [id=c3d31603cb77f8629f26918de3726a29e02943a4c92cf3249d899c3880db249d]
docker_container.wonderful_wiles: Destruction complete after 1s
docker_container.wonderful_wiles: Creating...
docker_container.wonderful_wiles: Creation complete after 1s [id=d366e61015c73c0422c64c2f6f1511112f539317b83c29d6575aa9f5a82b3386]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```


## Outputs of `terraform outputs`:

```bash
container_id = "af19f503778019507cec665d5a8dd3b12faa717b9fece99ca41d6a92d93230d6"
image_id = "sha256:05947a1da17a56d66908467c2097413ab9bc4405e96013708082ffd9914e0243app-flask:latest"
```




# Task 1.4

## Outputs if `terraform show`:
```bash
# data.twc_configurator.configurator:
data "twc_configurator" "configurator" {
    cpu_frequency = "3.3"
    disk_type     = "nvme"
    id            = "11"
    location      = "ru-1"

    requirements {
        cpu_max                = 104
        cpu_min                = 1
        cpu_step               = 1
        disk_max               = 2048000
        disk_min               = 10240
        disk_step              = 5120
        network_bandwidth_max  = 1000
        network_bandwidth_min  = 200
        network_bandwidth_step = 100
        ram_max                = 747520
        ram_min                = 1024
        ram_step               = 1024
    }
}

# data.twc_os.os:
data "twc_os" "os" {
    family           = "linux"
    id               = "61"
    name             = "ubuntu"
    version          = "20.04"
    version_codename = "focal"

    requirements {
        bandwidth_min = 0
        cpu_min       = 0
        disk_min      = 0
        ram_min       = 0
    }
}

# twc_server.my-timeweb-server:
resource "twc_server" "my-timeweb-server" {
    availability_zone = "spb-2"
    boot_mode         = "std"
    configurator_id   = 11
    cpu               = 1
    cpu_frequency     = "3.3"
    disks             = [
        {
            id          = 16801143
            is_mounted  = true
            is_system   = true
            size        = 10240
            status      = "done"
            system_name = "vda"
            type        = "nvme"
            used        = 0
        },
    ]
    id                = "2600897"
    is_ddos_guard     = false
    location          = "ru-1"
    main_ipv4         = "185.104.113.125"
    name              = "DevOps Course Server"
    networks          = [
        {
            bandwidth     = 200
            ips           = [
                {
                    ip      = "2a03:6f00:5:1::eb2"
                    is_main = true
                    ptr     = ""
                    type    = "ipv6"
                },
                {
                    ip      = "185.104.113.125"
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
            id      = 61
            name    = "ubuntu"
            version = "20.04"
        },
    ]
    os_id             = 61
    preset_id         = 0
    project_id        = 707561
    ram               = 1024
    software          = []
    ssh_keys_ids      = [
        159319,
    ]
    start_at          = "2024-02-27T21:45:12.000Z"
    status            = "on"
    vnc_pass          = (sensitive value)

    configuration {
        configurator_id = 11
        cpu             = 1
        disk            = 10240
        ram             = 1024
    }
}

# twc_ssh_key.your-key
```

## Outputs of `terraform state list`:

```bash
data.twc_configurator.configurator
data.twc_os.os
twc_server.my-timeweb-server
twc_ssh_key.your-key
```

## Outputs of `terraform output`:

```bash
config_id = "11"
os_id = "61"
```
