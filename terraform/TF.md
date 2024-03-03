# The results and outputs while following the tutorial

## Docker-container tutorial

### Output of `terraform show` for docker

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
        hostname                                    = "55816607744c"
        id                                          = "55816607744c193ca5a6c5090061109d7b088b54d44f430f9d5d6be710ac8b80"
        image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
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

    # docker_image.nginx:
    resource "docker_image" "nginx" {
        id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
        image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
        keep_locally = false
        name         = "nginx"
        repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
    }

### Output of `terraform state list` for docker

    docker_container.nginx
    docker_image.nginx

### Logs after `terraform apply` for docker

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
        + name                                        = "tutorial"
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
        + name         = "nginx"
        + repo_digest  = (known after apply)
        }

    Plan: 2 to add, 0 to change, 0 to destroy.

    Do you want to perform these actions?
    Only 'yes' will be accepted to approve.


    docker_image.nginx: Creating...
    docker_image.nginx: Still creating... [20s elapsed]
    docker_image.nginx: Creation complete after 25s [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx]
    docker_container.nginx: Creating...
    docker_container.nginx: Creation complete after 4s [id=55816607744c193ca5a6c5090061109d7b088b54d44f430f9d5d6be710ac8b80]

    Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

### Output after `terraform apply` which was run after the changing ports.external from 8000 to 8080 for docker

    docker_image.nginx: Refreshing state... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx]
    docker_container.nginx: Refreshing state... [id=55816607744c193ca5a6c5090061109d7b088b54d44f430f9d5d6be710ac8b80]

    Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
    -/+ destroy and then create replacement

    Terraform will perform the following actions:

    # docker_container.nginx must be replaced
    -/+ resource "docker_container" "nginx" {
        + bridge                                      = (known after apply)
        ~ command                                     = [
            - "nginx",
            - "-g",
            - "daemon off;",
            ] -> (known after apply)
        + container_logs                              = (known after apply)
        - cpu_shares                                  = 0 -> null
        - dns                                         = [] -> null
        - dns_opts                                    = [] -> null
        - dns_search                                  = [] -> null
        ~ entrypoint                                  = [
            - "/docker-entrypoint.sh",
            ] -> (known after apply)
        ~ env                                         = [] -> (known after apply)
        + exit_code                                   = (known after apply)
        - group_add                                   = [] -> null
        ~ hostname                                    = "55816607744c" -> (known after apply)
        ~ id                                          = "55816607744c193ca5a6c5090061109d7b088b54d44f430f9d5d6be710ac8b80" -> (known after apply)
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
        ~ stop_signal                                 = "SIGQUIT" -> (known after apply)
        ~ stop_timeout                                = 0 -> (known after apply)
        - storage_opts                                = {} -> null
        - sysctls                                     = {} -> null
        - tmpfs                                       = {} -> null
            # (14 unchanged attributes hidden)

        ~ ports {
            ~ external = 8000 -> 8080 # forces replacement
                # (3 unchanged attributes hidden)
            }
        }

    Plan: 1 to add, 0 to change, 1 to destroy.

    Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.

    Enter a value: yes

    docker_container.nginx: Destroying... [id=55816607744c193ca5a6c5090061109d7b088b54d44f430f9d5d6be710ac8b80]
    docker_container.nginx: Destruction complete after 2s
    docker_container.nginx: Creating...
    docker_container.nginx: Creation complete after 2s [id=cffead8fe066ca805fbcdc5e1184af266f461b515dae8f4230c6d1a60c563ab3]

    Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

### Output after `terraform output` for docker

    container_id = "0594ff42b336d7bd72b6b191ee3f4da19cbe809cda9f6475cb32de7b33214961"
    image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"

## Yandex-cloud tutorial

### Output after `terraform state list` for cloud

    yandex_compute_disk.boot-disk-1
    yandex_compute_disk.boot-disk-2
    yandex_compute_instance.vm-1
    yandex_compute_instance.vm-2
    yandex_vpc_network.network-1
    yandex_vpc_subnet.subnet-1

### Output after `terraform output` for cloud

    external_ip_address_vm_1 = "51.250.86.2"
    external_ip_address_vm_2 = "51.250.89.68"
    internal_ip_address_vm_1 = "192.168.10.18"
    internal_ip_address_vm_2 = "192.168.10.33"

## Terraform Best Practices

During the setup of the GitHub infrastructure using Terraform, the following best practices were applied:

1. Modularization:
   - The Terraform code was structured using reusable modules, promoting code reusability, maintainability, and scalability.

2. Input Variables:
   - Input variables were used to make the Terraform configurations more flexible and customizable, allowing for easy configuration changes without modifying the code.

3. Environment Separation:
   - Separate Terraform configurations were created for different environments (e.g., development, staging, production) to maintain isolation and prevent accidental changes in one environment affecting others.

4. Terraform State Management:
   - Terraform's state management features were utilized to keep track of the infrastructure state accurately, ensuring that Terraform can manage resources accordingly.

5. Terraform Workspaces:
   - Terraform workspaces were used to isolate state and configuration for each environment or deployment, facilitating better management and deployment of infrastructure changes.

6. Terraform Backends:
   - A backend configuration was set up to store the Terraform state file remotely, enabling better collaboration, locking, and versioning of the state file.
