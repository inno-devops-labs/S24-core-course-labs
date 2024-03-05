# Terraform on local machine

---

## Terraform state show

```shell
terraform state show docker_container.nginx
```

```
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
    hostname                                    = "167b4644899f"
    id                                          = "167b4644899fd05f94a90eef76275256592aaf608d795ef2552dc847f023fd00"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "nginx_container"
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
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

```

## Terraform state list

```
docker_container.nginx
docker_image.nginx
```

## Document a part of the log with the applied changes

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.nginx will be created
  + resource "docker_container" "nginx" {
      + attach                                      = false
      + bridge                                      = (known after apply)
      + command                                     = (known after apply)
      + container_logs                              = (known after apply)
      + container_read_refresh_timeout_milliseconds = 15000
      + entrypoint                                  = (known after apply)
      + env                                         = (known after apply)
      + exit_code                                   = (known after apply)
      + hostname                                    = (known after apply)
      + id                                          = (known after apply)
      + image                                       = (known after apply)
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "nginx_container"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = false
      + runtime                                     = (known after apply)
      + security_opts                               = (known after apply)
      + shm_size                                    = (known after apply)
      + start                                       = true
      + stdin_open                                  = false
      + stop_signal                                 = (known after apply)
      + stop_timeout                                = (known after apply)
      + tty                                         = false
      + wait                                        = false
      + wait_timeout                                = 60

      + ports {
          + external = 8000
          + internal = 80
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # docker_image.nginx will be created
  + resource "docker_image" "nginx" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "nginx:latest"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id = (known after apply)
  + image_id     = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_image.nginx: Creating...
docker_image.nginx: Creation complete after 9s [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 2s [id=167b4644899fd05f94a90eef76275256592aaf608d795ef2552dc847f023fd00]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "167b4644899fd05f94a90eef76275256592aaf608d795ef2552dc847f023fd00"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"

```

## Terraform output

```
container_id = "04ce4c6c32afb98e38941e56cbcf84ab0d794f408afa35cd5184ef69298d1ea1"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

---

# Terraform on Timeweb

---

## Document a part of the log with the applied changes

```
data.twc_os.os: Reading...
data.twc_configurator.configurator: Reading...
twc_ssh_key.your-key: Refreshing state... [id=159285]
data.twc_configurator.configurator: Read complete after 0s [id=11]
data.twc_os.os: Read complete after 0s [id=61]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # twc_server.my-timeweb-server will be created
  + resource "twc_server" "my-timeweb-server" {
      + availability_zone = (known after apply)
      + avatar_id         = (known after apply)
      + boot_mode         = (known after apply)
      + cloud_init        = (known after apply)
      + comment           = (known after apply)
      + configurator_id   = (known after apply)
      + cpu               = (known after apply)
      + cpu_frequency     = (known after apply)
      + disks             = (known after apply)
      + id                = (known after apply)
      + is_ddos_guard     = (known after apply)
      + location          = (known after apply)
      + main_ipv4         = (known after apply)
      + name              = "webserver"
      + networks          = (known after apply)
      + os                = (known after apply)
      + os_id             = 61
      + preset_id         = (known after apply)
      + project_id        = (known after apply)
      + ram               = (known after apply)
      + software          = (known after apply)
      + ssh_keys_ids      = [
          + 159285,
        ]
      + start_at          = (known after apply)
      + status            = (known after apply)
      + vnc_pass          = (sensitive value)

      + configuration {
          + configurator_id = 11
          + cpu             = 1
          + disk            = 10240
          + ram             = 1024
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + twc_configuration_id = {
      + configurator_id = 11
      + cpu             = 1
      + disk            = 10240
      + ram             = 1024
    }
  + twc_os_id            = 61

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

twc_server.my-timeweb-server: Creating...
twc_server.my-timeweb-server: Creation complete after 2s [id=2600803]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

twc_configuration_id = {
  "configurator_id" = 11
  "cpu" = 1
  "disk" = 10240
  "ram" = 1024
}
twc_os_id = 61
```

## Terraform state show

```shell
terraform state show twc_server.data.twc_configurator.configurator
```

```
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
```

## Terraform state list

```
data.twc_configurator.configurator
data.twc_os.os
twc_server.my-timeweb-server
twc_ssh_key.your-key
```

## Terraform output

```
Outputs:

twc_configuration_id = {
  "configurator_id" = 11
  "cpu" = 1
  "disk" = 10240
  "ram" = 1024
}
twc_os_id = 61
```

---

# Best practices

- Tokens are read from files (Not hardcoded)
- Used variables for potentially changing data
- Outputs for necessary data