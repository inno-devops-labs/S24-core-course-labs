# Best Practices

1. Use `terraform` validate in order to check if config is correct
2. Use `terraform plan` in order to check what s going to happen
3. Use variables

# Docker

`$ terraform state show docker_image.app`

```
# docker_image.app:
resource "docker_image" "app" {
    id           = "sha256:0963708f9d4e5429832e5a3067b661347c99218113d064f970b51ae64c07f29cbrutaljesus/devops_lab_2"
    image_id     = "sha256:0963708f9d4e5429832e5a3067b661347c99218113d064f970b51ae64c07f29c"
    keep_locally = false
    name         = "brutaljesus/devops_lab_2"
    repo_digest  = "brutaljesus/devops_lab_2@sha256:d4cab0b3de6d35953b076884c4f097adaf4a68f0063971c3acdc9703f5463e01"
```

`$ terraform state show docker_container.app`

```
# docker_container.app:
resource "docker_container" "app" {
    attach                                      = false
    command                                     = [
        "python",
        "-m",
        "poetry",
        "run",
        "uvicorn",
        "src.app:app",
        "--host",
        "0.0.0.0",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "caa68049dba8"
    id                                          = "caa68049dba8368def69efa69abb4f4dff64ac958bbffc67f7501ba07b93e4ab"
    image                                       = "sha256:0963708f9d4e5429832e5a3067b661347c99218113d064f970b51ae64c07f29c"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app"
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
    working_dir                                 = "/code"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

`$ terraform state list`

```
docker_container.app
docker_image.app
```

`$ terraform output`

```
container_id = "7c3a3bcba6aa34b72ce251493f8377214320d8895423f2449226fe22a747cada"
image_id = "sha256:0963708f9d4e5429832e5a3067b661347c99218113d064f970b51ae64c07f29cbrutaljesus/devops_lab_2"
```

# Yandex Cloud

`$ terraform apply`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated
with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.boot-disk-1 will be created
  + resource "yandex_compute_disk" "boot-disk-1" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd83s8u085j3mq231ago"
      + name        = "boot-disk-1"
      + product_ids = (known after apply)
      + size        = 8
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = (known after apply)
    }

  # yandex_compute_instance.vm-1 will be created
  + resource "yandex_compute_instance" "vm-1" {
      + allow_stopping_for_update = true
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + metadata                  = {
          + "ssh-keys" = <<-EOT
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHiIw9hS85eVJcTCJ2C8AQe/4ixe05oFRxHLk4OzVJ4479wdaNCCToPVvcC2QZcsM+W2pT9UkvialZtvm41z1ssS1KNm3dPAisCW9448YHyWOdXSPiR1c+JFZ7f13+mAe8Z7BUYwtO0L9gp8I/Zx7s2xl2M/lptK2uEwC6Kt6yksK6GSpLlqDyDkXpVkFNkpXGPNyAdgrjAIpHqIgM6yarI1Vu7k7jRDVYhUXSh39QoIOVSdEARc+yzEueeRbsUCxh7fNtmQbWonYEE9DGkfd2Cc91TzrwcW/aH/QZbN0IivkxLKJ3vRYOVJUyL3yD/Tf4UNtPFbPXuGG7RH1zt+ujyWpqw/7IyV/c8ouXjnGey536Y+3wt+kdYnA5tD/UVfnw4ETiaJRbVOCG3Kp2o88/IgnQx6H+j0Zo6rHW1MWZ2JCK+B/8BZ7jugEaJdod/UnncKRtn0V3MFnhx/F4yUPNJUFmdzp+PnBS0Kfgqdz9T7oT6KtJDGbqWWwFbAmP9EE= ilnarkhasanov@Ilnars-MacBook-Pro.local
            EOT
        }
      + name                      = "terraform1"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v3"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = (known after apply)

      + boot_disk {
          + auto_delete = true
          + device_name = (known after apply)
          + disk_id     = (known after apply)
          + mode        = (known after apply)
        }

      + network_interface {
          + index              = (known after apply)
          + ip_address         = (known after apply)
          + ipv4               = true
          + ipv6               = (known after apply)
          + ipv6_address       = (known after apply)
          + mac_address        = (known after apply)
          + nat                = true
          + nat_ip_address     = (known after apply)
          + nat_ip_version     = (known after apply)
          + security_group_ids = (known after apply)
          + subnet_id          = (known after apply)
        }

      + resources {
          + core_fraction = 20
          + cores         = 2
          + memory        = 1
        }

      + scheduling_policy {
          + preemptible = true
        }
    }

  # yandex_vpc_network.network-1 will be created
  + resource "yandex_vpc_network" "network-1" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network1"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.subnet-1 will be created
  + resource "yandex_vpc_subnet" "subnet-1" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "subnet1"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.10.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + external_ip_address = (known after apply)
  + internal_ip_address = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-1: Creating...
yandex_compute_disk.boot-disk-1: Creating...
yandex_vpc_network.network-1: Creation complete after 4s [id=enppbgr60tq7gvs77unc]
yandex_vpc_subnet.subnet-1: Creating...
yandex_vpc_subnet.subnet-1: Creation complete after 1s [id=e9bmbho0t7irqur5n1rd]
yandex_compute_disk.boot-disk-1: Still creating... [10s elapsed]
yandex_compute_disk.boot-disk-1: Creation complete after 11s [id=fhmhk2tlhlslnsoidh36]
yandex_compute_instance.vm-1: Creating...
yandex_compute_instance.vm-1: Still creating... [10s elapsed]
yandex_compute_instance.vm-1: Still creating... [20s elapsed]
yandex_compute_instance.vm-1: Creation complete after 28s [id=fhmi02a322s56048q1jo]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

external_ip_address = "51.250.3.192"
internal_ip_address = "192.168.10.7"
```