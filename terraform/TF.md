# Terraform built infrastructure 

## terraform docker state list

```bash
docker_container.nginx
docker_image.nginx
```

## docker_container.nginx:
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
    hostname                                    = "16853f7c5a41"
    id                                          = "16853f7c5a418880b36c05f8875d42a25af45a73dd7aa40d1d62ad01195ef191"
    image                                       = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676"
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
```

## docker_image.nginx:
```bash
resource "docker_image" "nginx" {
    id           = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676nginx"
    image_id     = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```


## Terraform Changes

### Changes Applied to Infrastructure

#### Docker Container Resource - nginx:

- A new Docker container named "tutorial" has been created with the following configurations:
  - Running Nginx with specified command and entrypoint.
  - Listening on port 80 internally and port 8000 externally.
  - Running on the default network mode with specific network data.
  - Other settings like hostname, IPC mode, logging, etc., are configured as specified.

#### Docker Image Resource - nginx:

- A Docker image named "nginx" has been created with the following details:
  - Image ID: `sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676`
  - Repository Digest: `nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107`

## An input name utilization

When I set new name for docker container:
    ```name  = "devops-lab"```

I got an opportunity instantly apply my changes:

```bash
i-pechersky@i-pechersky-x docker % terraform apply
docker_image.nginx: Refreshing state... [id=sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676nginx]
docker_container.nginx: Refreshing state... [id=16853f7c5a418880b36c05f8875d42a25af45a73dd7aa40d1d62ad01195ef191]

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
      ~ hostname                                    = "16853f7c5a41" -> (known after apply)
      ~ id                                          = "16853f7c5a418880b36c05f8875d42a25af45a73dd7aa40d1d62ad01195ef191" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "tutorial" -> "devops-lab" # forces replacement
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

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.nginx: Destroying... [id=16853f7c5a418880b36c05f8875d42a25af45a73dd7aa40d1d62ad01195ef191]
docker_container.nginx: Destruction complete after 0s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 0s [id=b5ba484c937bd2d66cf54920801c4dbb6d03f5439f7a1388b82515d7974c6d60]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```


## Docker Outputs
```bash
i-pechersky@i-pechersky-x docker % terraform refresh
docker_image.nginx: Refreshing state... [id=sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676nginx]
docker_container.nginx: Refreshing state... [id=b5ba484c937bd2d66cf54920801c4dbb6d03f5439f7a1388b82515d7974c6d60]

Outputs:

container_id = "b5ba484c937bd2d66cf54920801c4dbb6d03f5439f7a1388b82515d7974c6d60"
image_id = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676nginx"
```


## Yandex cloud state list

```bash
yandex_vpc_network.network-1
yandex_vpc_subnet.subnet-1
```

### yandex_vpc_network.network-1:

```bash
resource "yandex_vpc_network" "network-1" {
    created_at                = "2024-02-25T19:42:32Z"
    default_security_group_id = "enpppevkn6pv92v7al16"
    folder_id                 = "b1gj9vkvaatrvs9cbdt7"
    id                        = "enpg5upv76s1r9moh4e9"
    labels                    = {}
    name                      = "network1"
    subnet_ids                = [
        "e9bli0tupnivfqjq6g7q",
    ]
}
```

### yandex_vpc_subnet.subnet-1:

```bash
resource "yandex_vpc_subnet" "subnet-1" {
    created_at     = "2024-02-25T19:42:35Z"
    folder_id      = "b1gj9vkvaatrvs9cbdt7"
    id             = "e9bli0tupnivfqjq6g7q"
    labels         = {}
    name           = "subnet1"
    network_id     = "enpg5upv76s1r9moh4e9"
    v4_cidr_blocks = [
        "192.168.10.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Cloud outputs

```bash
i-pechersky@i-pechersky-x cloud % terraform output                               
network_id = "enpg5upv76s1r9moh4e9"
subnet_id = "e9bli0tupnivfqjq6g7q"
```

## Github repository handling by terraform 

### Terraform Best Practices

#### 1. Variable Usage
   - Declaring variables for sensitive information such as the GitHub Personal Access Token (PAT) and organization name enhances security by allowing sensitive data to be managed separately.
   - Providing default values for non-sensitive variables like `organization` improves configurational flexibility and reduces redundancy.

#### 2. Branch Configuration
   - Configuring the default branch (`main`) using the `github_branch_default` resource ensures consistency in branch naming conventions.
   - Enforcing branch protection settings via the `github_branch_protection` resource enhances security by requiring specific review and resolution processes for pull requests.

#### 3. GitHub Branch Protection
   - Enabling settings like requiring conversation resolution and approving reviews enhances the quality and security of code contributions to the repository.
   - Setting up enforcement for administrators ensures that branch protection policies are consistently applied and adhered to.

#### 4. Consistency and Idempotency
   - Terraform's declarative nature ensures that infrastructure is consistently provisioned and maintained according to the defined configuration, promoting predictability and reliability.
   - Leveraging Terraform's state management capabilities ensures idempotent execution, where applying the configuration repeatedly yields the same desired state without unintended side effects.

#### 5. Version Control and Collaboration
   - Utilizing version control systems such as Git to manage Terraform configurations enables collaboration, change tracking, and rollback capabilities, promoting agility and teamwork in infrastructure management.


