# Docker infrestructure with Terraform

## Output of `terraform state show docker_container.nginx`:

```bash
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
    hostname                                    = "189db9ff11d1"
    id                                          = "189db9ff11d181b7ede5572a86a05cbb0078acd1c77eceee82621fa39986b1fc"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
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
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

## Output of `terraform state show docker_image.nginx`:

```bash
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

## Output of `terraform state list`

```bash
docker_container.nginx
docker_image.nginx
```

## Document a part of the log with the applied changes. (Output of `terraform apply`)

```bash
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
      + name                                        = "ExampleNginxContainer"
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
docker_image.nginx: Creation complete after 8s [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=189db9ff11d181b7ede5572a86a05cbb0078acd1c77eceee82621fa39986b1fc]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

container_id = "189db9ff11d181b7ede5572a86a05cbb0078acd1c77eceee82621fa39986b1fc"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## Utilize input variables to rename your Docker container.

To do it, you can execute the following command:

```bash
terraform apply -var "container_name=YetAnotherName"
```

After that, you can see (using `docker ps`) that the container has new name: **YetAnotherName**

```bash
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
6c3defc623ef   e4720093a3c1   "/docker-entrypoint.…"   12 seconds ago   Up 11 seconds   0.0.0.0:8000->80/tcp   YetAnotherName
```

## Output of `terraform output`

```bash
container_id = "6c3defc623efb896bf0d504e441b7ed42bd27105a7af16822fe8a8db1daba23d"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

# Timeweb Cloud Infrastructure using Terraform

## Output of `terraform state show data.twc_configurator.configurator`:

```t
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

## Output of `terraform state show data.twc_os.os`:

```t
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
```

## Output of `terraform state show twc_server.my-timeweb-server`:

```t
# twc_server.my-timeweb-server:
resource "twc_server" "my-timeweb-server" {
    availability_zone = "spb-2"
    boot_mode         = "std"
    configurator_id   = 11
    cpu               = 1
    cpu_frequency     = "3.3"
    disks             = [
        {
            id          = 16775201
            is_mounted  = true
            is_system   = true
            size        = 15360
            status      = "done"
            system_name = "vda"
            type        = "nvme"
            used        = 0
        },
    ]
    id                = "2600797"
    is_ddos_guard     = false
    location          = "ru-1"
    main_ipv4         = "217.25.88.213"
    name              = "My Timeweb Server"
    networks          = [
        {
            bandwidth     = 200
            ips           = [
                {
                    ip      = "2a03:6f00:5:1::e6a"
                    is_main = true
                    ptr     = ""
                    type    = "ipv6"
                },
                {
                    ip      = "217.25.88.213"
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
    project_id        = 420513
    ram               = 1024
    software          = []
    ssh_keys_ids      = [
        159287,
    ]
    status            = "installing"

    configuration {
        configurator_id = 11
        cpu             = 1
        disk            = 15360
        ram             = 1024
    }
}
```

## Output of `terraform state show twc_ssh_key.timeweb-ssh-key`:

```
# twc_ssh_key.timeweb-ssh-key:
resource "twc_ssh_key" "timeweb-ssh-key" {
    body       = <<ssh-key here>>
    created_at = "2024-02-27T23:39:37.000Z"
    id         = "159287"
    name       = "TimeWeb SSH key"
    used_by    = []
}
```

## Output of `terraform state list`

```bash
data.twc_configurator.configurator
data.twc_os.os
twc_server.my-timeweb-server
twc_ssh_key.timeweb-ssh-key
```

## Document a part of the log with the applied changes. (Output of `terraform apply`)

```bash
data.twc_configurator.configurator: Reading...
data.twc_os.os: Reading...
data.twc_os.os: Read complete after 0s [id=61]
data.twc_configurator.configurator: Read complete after 0s [id=11]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
symbols:
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
      + name              = "ExampleTimewebServer"
      + networks          = (known after apply)
      + os                = (known after apply)
      + os_id             = 61
      + preset_id         = (known after apply)
      + project_id        = (known after apply)
      + ram               = (known after apply)
      + software          = (known after apply)
      + ssh_keys_ids      = (known after apply)
      + start_at          = (known after apply)
      + status            = (known after apply)
      + vnc_pass          = (sensitive value)

      + configuration {
          + configurator_id = 11
          + cpu             = 1
          + disk            = 15360
          + ram             = 1024
        }
    }

  # twc_ssh_key.timeweb-ssh-key will be created
  + resource "twc_ssh_key" "timeweb-ssh-key" {
      + body       = <<ssh-key here>>
      + created_at = (known after apply)
      + id         = (known after apply)
      + name       = "TimeWeb SSH key"
      + used_by    = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + instance_id        = (known after apply)
  + instance_public_ip = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

twc_ssh_key.timeweb-ssh-key: Creating...
twc_ssh_key.timeweb-ssh-key: Creation complete after 1s [id=159307]
twc_server.my-timeweb-server: Creating...
twc_server.my-timeweb-server: Creation complete after 4s [id=2600843]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

instance_id = "2600843"
instance_public_ip = "185.104.113.100"
```

## Utilize input variables to rename your Server.

To do it, you can execute the following command:

```bash
terraform apply -var "server_name=YetAnotherName"
```

After that, you can see (in the timeweb console) that the server has new name: **YetAnotherName**

## Output of `terraform output`

```bash
instance_id = "2600837"
instance_public_ip = "92.255.76.109"
```

# Terraform-related best practices

1. Use version control (Git)

2. Organize the code: use separate directories for different environments and break down your configurations into several files.

3. Use variables and outputs

4. Plan before applying.

5. Keep dependencies up to date.

6. Use environment variables for tokens.
