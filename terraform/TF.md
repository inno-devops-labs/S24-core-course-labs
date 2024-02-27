# Terraform

## Docker terraform

### Docker terraform instance state

```bash
terraform state show docker_container.dev-ops-course-app-python
```

docker_container.dev-ops-course-app-python:
resource "docker_container" "dev-ops-course-app-python" {
    attach                                      = false
    command                                     = [
        "venv/bin/uvicorn",
        "src.main:app",
        "--host",
        "0.0.0.0",
        "--port",
        "80",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "018548e2f570"
    id                                          = "018548e2f57035b95498a2dbcab465d0b5962aa6a56c04613fffc5ca0cb15db1"
    image                                       = "sha256:acba2d08082ffaeb12188e168822cf72704a2d736be888af7deabf3c361613f2"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "dev-ops-course-app-python"
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
    working_dir                                 = "/home/user"

    ports {
        external = 80
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

### List of terraform docker nodes

```bash
terraform state list
```

docker_container.dev-ops-course-app-python

### Output of docker terraform

```bash
terraform output
```

container_id = "018548e2f57035b95498a2dbcab465d0b5962aa6a56c04613fffc5ca0cb15db1"
container_name = "dev-ops-course-app-python"

## Deploy to yandex cloud using terraform

### List of terraform nodes

yandex_compute_disk.boot-disk
yandex_compute_image.default
yandex_compute_instance.vm-1
yandex_vpc_network.default
yandex_vpc_subnet.default

### Show state for yandex_compute_instance.vm-1

resource "yandex_compute_instance" "vm-1" {
    created_at                = "2024-02-27T21:17:37Z"
    folder_id                 = "b1gv4t2t9ahap1g9phga"
    fqdn                      = "fhmjr8b2p0rk3k8o18u4.auto.internal"
    id                        = "fhmjr8b2p0rk3k8o18u4"
    metadata                  = {
        "ssh-keys" = <<-EOT
            yc-user:ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIeOUHRHOhVxVtupqO/jlZ72eYpe2VmWF11RQGTg6wcm yaroslav@xiaomao
        EOT
    }
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhmue0uulgordfnct909"
        disk_id     = "fhmue0uulgordfnct909"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd84p55lgujrfj1t5qcv"
            name       = "boot-disk"
            size       = 50
            type       = "network-ssd"
        }
    }

    metadata_options {
        aws_v1_http_endpoint = 1
        aws_v1_http_token    = 2
        gce_http_endpoint    = 1
        gce_http_token       = 1
    }

    network_interface {
        index              = 0
        ip_address         = "192.168.10.10"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:13:da:16:2c"
        nat                = true
        nat_ip_address     = "84.201.133.126"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b90c5dgk6geivt2lg5"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 4
    }

    scheduling_policy {
        preemptible = false
    }

    timeouts {
        create = "10m"
        delete = "10m"
    }
}

### Output of deployed vm

internal_ip_address_vm_1 = "192.168.10.10"
external_ip_address_vm_1= "84.201.133.126"

Eventually, I connected to the vm using the following command

```bash
ssh ubuntu@84.201.133.126 -i ~/.ssh/yandex_cloud
```

```bash
yaroslav@xiaomao ~/S/D/d/t/github (lab4)> terraform import "github_repository.repo" "dev-ops-course"
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Importing from ID "dev-ops-course"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=dev-ops-course]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

```bash
yaroslav@xiaomao ~/S/D/d/t/github (lab4)> terraform apply
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Refreshing state... [id=dev-ops-terraform-exercize]
github_branch_default.main: Refreshing state... [id=dev-ops-terraform-exercize]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "dev-ops-terraform-exercize"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLNy-5s4C0xYw]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

## Best practises

- Using git for controlling infrastructure
- Using `terraform plan` before `terraform apply`

