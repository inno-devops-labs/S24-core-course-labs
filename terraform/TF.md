When we call terraform state list:
```bash
esadmazi@Muhammeds-MacBook-Air terraform % terraform state list
docker_container.my-python-app
docker_image.my-python-app
```
When we call terraform state show
```bash
esadmazi@Muhammeds-MacBook-Air terraform % terraform state show docker_container.my-python-app

# docker_container.my-python-app:
resource "docker_container" "my-python-app" {
    attach                                      = false
    command                                     = [
        "python3",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "f52f2a8fb3bc"
    id                                          = "f52f2a8fb3bc9d49d0bcde96b8ab59e38f1bc832b8fc72dfcd0db54098d2467b"
    image                                       = "sha256:ada83d6529b996d4a9e09e9ebe98d3af5ef1016aff5add8479f0741407a84554"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "my-python-app-container"
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
    user                                        = "appuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/python_app"

    ports {
        external = 8080
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

esadmazi@Muhammeds-MacBook-Air terraform % terraform state show docker_image.my-python-app    

# docker_image.my-python-app:
resource "docker_image" "my-python-app" {
    id           = "sha256:ada83d6529b996d4a9e09e9ebe98d3af5ef1016aff5add8479f0741407a84554esadmazi/my-python-app:latest"
    image_id     = "sha256:ada83d6529b996d4a9e09e9ebe98d3af5ef1016aff5add8479f0741407a84554"
    keep_locally = false
    name         = "esadmazi/my-python-app:latest"
    repo_digest  = "esadmazi/my-python-app@sha256:a63a2d44a14ddee2b7f87dede57694a2aa226b5a8348de0ee0319e972a4590f7"
}
```
When we do some changes, output of terraform apply looks like this:
```bash
esadmazi@Muhammeds-MacBook-Air terraform % terraform apply
docker_image.my-python-app: Refreshing state... [id=sha256:ada83d6529b996d4a9e09e9ebe98d3af5ef1016aff5add8479f0741407a84554esadmazi/my-python-app:latest]
docker_container.my-python-app: Refreshing state... [id=0380dc521a02edfb2d877aae767d9a1524e297ed7b70bac84cdc6d9466d3b5d8]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following
symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.my-python-app must be replaced
-/+ resource "docker_container" "my-python-app" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "python3",
          - "app.py",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "0380dc521a02" -> (known after apply)
      ~ id                                          = "0380dc521a02edfb2d877aae767d9a1524e297ed7b70bac84cdc6d9466d3b5d8" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "my-python-app-container"
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
      - user                                        = "appuser" -> null
      - working_dir                                 = "/python_app" -> null
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

docker_container.my-python-app: Destroying... [id=0380dc521a02edfb2d877aae767d9a1524e297ed7b70bac84cdc6d9466d3b5d8]
docker_container.my-python-app: Destruction complete after 0s
docker_container.my-python-app: Creating...
docker_container.my-python-app: Creation complete after 1s [id=1f59eeff62211ae5de9f4d25777202d8c52d1609822f20e024f3c5c66c710ee8]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```
```bash
esadmazi@Muhammeds-MacBook-Air terraform % terraform output
container_id = "1f59eeff62211ae5de9f4d25777202d8c52d1609822f20e024f3c5c66c710ee8"
image_id = "sha256:ada83d6529b996d4a9e09e9ebe98d3af5ef1016aff5add8479f0741407a84554esadmazi/my-python-app:latest"
```
