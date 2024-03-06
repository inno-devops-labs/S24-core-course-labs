# Command output

## Docker

`terraform state show docker_container.my_container`:

```
# docker_container.my_container:
resource "docker_container" "my_container" {
    attach                                      = false
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "7c509a462a4a"
    id                                          = "7c509a462a4adbcb4787599f79167f59199723e3c71abce3bdd1f72cc79d6b95"
    image                                       = "sha256:acd7c8e704f5485b22d4643193265ef45194f15f7f4fafcb4c6b280d2baa346a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "default"
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
    user                                        = "myuser"
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

`terraform state show docker_image.my_image`:

```
# docker_image.my_image:
resource "docker_image" "my_image" {
    id          = "sha256:acd7c8e704f5485b22d4643193265ef45194f15f7f4fafcb4c6b280d2baa346abatdockerivankornienko/app_python"
    image_id    = "sha256:acd7c8e704f5485b22d4643193265ef45194f15f7f4fafcb4c6b280d2baa346a"
    name        = "batdockerivankornienko/app_python"
    repo_digest = "batdockerivankornienko/app_python@sha256:8bda2ba10d7eb716f3cf5d8c6d4bf85332a9b95042f7b4558f80fa2870c57be7"
}
```

`terraform state list`:

```
docker_container.my_container
docker_image.my_image
```

### Applying changes

`terraform apply`

```
docker_image.my_image: Refreshing state... [id=sha256:acd7c8e704f5485b22d4643193265ef45194f15f7f4fafcb4c6b280d2baa346abatdockerivankornienko/app_python]
docker_container.my_container: Refreshing state... [id=7da8c668920e4727ec3981366604daf0f8e6b3a06bbaf87787ff9bf69ac66a93]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected this plan:

  # docker_container.my_container has been deleted
  - resource "docker_container" "my_container" {
      - id                                          = "7da8c668920e4727ec3981366604daf0f8e6b3a06bbaf87787ff9bf69ac66a93" -> null
        name                                        = "default"
        # (16 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following plan may include actions to undo or respond   
to these changes.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.my_container will be created
  + resource "docker_container" "my_container" {
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
      + image                                       = "batdockerivankornienko/app_python"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "default"
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
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + container_id    = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.my_container: Creating...
docker_container.my_container: Creation complete after 2s [id=7c509a462a4adbcb4787599f79167f59199723e3c71abce3bdd1f72cc79d6b95]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

container_id = "7c509a462a4adbcb4787599f79167f59199723e3c71abce3bdd1f72cc79d6b95"
container_image = "batdockerivankornienko/app_python"
container_name = "default"
container_port = tolist([
  {
    "external" = 8000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

## Output

`terraform output`:

```
container_id = "018ff0858b1964b589c2b6c4402abb94817563fc46a04ff3d26df1c5a9e2d11c"
container_image = "batdockerivankornienko/app_python"
container_name = "devops-lab4"
container_port = tolist([
  {
    "external" = 8000
    "internal" = 5000
    "ip" = "0.0.0.0"
    "protocol" = "tcp"
  },
])
```

# Best practices used

- Used `.gitignore` to exclude state files
- Performed `terraform fmt` to make canonical format
- Performed `terraform validate` and `terraform plan` before using `terraform apply` command
- Managed existing repo using `terraform import`
- Handled variables and outputs
