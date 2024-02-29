# Terraform

### Docker
```
(base) yanapavlova@MacBook-Air-Ana app_python % cd ..
(base) yanapavlova@MacBook-Air-Ana S24-core-course-labs % cd terraform/docker 
(base) yanapavlova@MacBook-Air-Ana docker % terraform init

Initializing the backend...

Initializing provider plugins...
- Finding kreuzwerker/docker versions matching "~> 3.0.1"...
- Installing kreuzwerker/docker v3.0.2...
- Installed kreuzwerker/docker v3.0.2 (self-signed, key ID BD080C4571C6104C)

Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
(base) yanapavlova@MacBook-Air-Ana docker % terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.devops-lab will be created
  + resource "docker_container" "devops-lab" {
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
      + image                                       = "nytakoe115/flask-moscow-app"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "devops-lab-task"
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
          + external = 8081
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
(base) yanapavlova@MacBook-Air-Ana docker % terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # docker_container.devops-lab will be created
  + resource "docker_container" "devops-lab" {
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
      + image                                       = "nytakoe115/flask-moscow-app"
      + init                                        = (known after apply)
      + ipc_mode                                    = (known after apply)
      + log_driver                                  = (known after apply)
      + logs                                        = false
      + must_run                                    = true
      + name                                        = "devops-lab-task"
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
          + external = 8081
          + internal = 5000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.devops-lab: Creating...
docker_container.devops-lab: Creation complete after 5s [id=4ed6fa55fe17e084eecd26b1728291f969dbf1637df558310cf75ec31bdc4726]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
(base) yanapavlova@MacBook-Air-Ana docker % terraform state list
docker_container.devops-lab
(base) yanapavlova@MacBook-Air-Ana docker % terraform state show
Exactly one argument expected.
Usage: terraform [global options] state show [options] ADDRESS

  Shows the attributes of a resource in the Terraform state.

  This command shows the attributes of a single resource in the Terraform
  state. The address argument must be used to specify a single resource.
  You can view the list of available resources with "terraform state list".

Options:

  -state=statefile    Path to a Terraform state file to use to look
                      up Terraform-managed resources. By default it will
                      use the state "terraform.tfstate" if it exists.
(base) yanapavlova@MacBook-Air-Ana docker % terraform state show docker_container.devops-lab
# docker_container.devops-lab:
resource "docker_container" "devops-lab" {
    attach                                      = false
    command                                     = [
        "flask",
        "run",
        "--host=0.0.0.0",
        "--port=80",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "4ed6fa55fe17"
    id                                          = "4ed6fa55fe17e084eecd26b1728291f969dbf1637df558310cf75ec31bdc4726"
    image                                       = "sha256:60d903e9f6c7169329ffb098ca416cd82230969e5a676f0ed3b14d15893b6a4a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devops-lab-task"
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
    working_dir                                 = "/app"

    ports {
        external = 8081
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
(base) yanapavlova@MacBook-Air-Ana docker % terraform apply
docker_container.devops-lab: Refreshing state... [id=4ed6fa55fe17e084eecd26b1728291f969dbf1637df558310cf75ec31bdc4726]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.devops-lab must be replaced
-/+ resource "docker_container" "devops-lab" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "flask",
          - "run",
          - "--host=0.0.0.0",
          - "--port=80",
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
      ~ hostname                                    = "4ed6fa55fe17" -> (known after apply)
      ~ id                                          = "4ed6fa55fe17e084eecd26b1728291f969dbf1637df558310cf75ec31bdc4726" -> (known after apply)
      ~ image                                       = "sha256:60d903e9f6c7169329ffb098ca416cd82230969e5a676f0ed3b14d15893b6a4a" -> "nytakoe115/flask-moscow-app" # forces replacement
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "devops-lab-task"
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
      - working_dir                                 = "/app" -> null
        # (13 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  + id   = (known after apply)
  + name = "devops-lab-task"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.devops-lab: Destroying... [id=4ed6fa55fe17e084eecd26b1728291f969dbf1637df558310cf75ec31bdc4726]
docker_container.devops-lab: Destruction complete after 0s
docker_container.devops-lab: Creating...
docker_container.devops-lab: Creation complete after 1s [id=9f7a0026b33e5ef146818084e842deb075bf8d560c3b4261440f816369b9265d]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

id = "9f7a0026b33e5ef146818084e842deb075bf8d560c3b4261440f816369b9265d"
name = "devops-lab-task"
(base) yanapavlova@MacBook-Air-Ana docker % terraform output
id = "9f7a0026b33e5ef146818084e842deb075bf8d560c3b4261440f816369b9265d"
name = "devops-lab-task"
(base) yanapavlova@MacBook-Air-Ana docker % 
```

### Yandex-cloud

```
(base) yanapavlova@MacBook-Air-Ana ya-cloud % terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.drive will be created
  + resource "yandex_compute_disk" "drive" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8t8vqitgjou20saanq"
      + name        = "drive"
      + product_ids = (known after apply)
      + size        = 21
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_instance.virtual-machine will be created
  + resource "yandex_compute_instance" "virtual-machine" {
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
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDchNGxgMkTmR2Z4K9aueY5TGp9KGY3zzl0JVAFWqU7qf4KABontUJbECfqhFnDijPJyM8BDHkB6lxjixmYHJoH2UapwWMentyEABqRdnZ5xeuWxh9W5waybrtn8uub+WEgx17Lhf4z+5N4CioZsEO8dMHGTMkLLUDvtsHfXU127xpGTcwej+Gtgokmrh5cbOipUJInYlxs7YwDoDZlai0YNCh877FIc4cuE9PZCILY5rLWktgKCaYLhJXay9QJOFKEKm8G4XdrogcrBGmEtR/Pbt6gV/p3DAIjDaAve3osmh4nTsguTokKeEYoet+p3klgsmonhk9GpZNGdh+2W/obC/s0a/LGaIDult3JlG1ybJ0YKXXzT44XmhbK+Jd9e+6Ho0fA0ejohU8jhzhHIW6NhUfzasT61FUESu5pvysd0by23I5T/40hXgNzjlcaX67DVPesYy6qQ+xSdnkuKYScvzFTYJu+X4pyJ9f65mMVcyc529ISQsmVkNSGq+FvGT8= yanapavlova@MacBook-Air-Ana.local
            EOT
        }
      + name                      = "virtual-machine"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

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
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

  # yandex_vpc_network.network-lab will be created
  + resource "yandex_vpc_network" "network-lab" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network-lab"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.lab-subnet will be created
  + resource "yandex_vpc_subnet" "lab-subnet" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "lab-subnet"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.50.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + VM_ip            = (known after apply)
  + instance_ssh_key = <<-EOT
        ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDchNGxgMkTmR2Z4K9aueY5TGp9KGY3zzl0JVAFWqU7qf4KABontUJbECfqhFnDijPJyM8BDHkB6lxjixmYHJoH2UapwWMentyEABqRdnZ5xeuWxh9W5waybrtn8uub+WEgx17Lhf4z+5N4CioZsEO8dMHGTMkLLUDvtsHfXU127xpGTcwej+Gtgokmrh5cbOipUJInYlxs7YwDoDZlai0YNCh877FIc4cuE9PZCILY5rLWktgKCaYLhJXay9QJOFKEKm8G4XdrogcrBGmEtR/Pbt6gV/p3DAIjDaAve3osmh4nTsguTokKeEYoet+p3klgsmonhk9GpZNGdh+2W/obC/s0a/LGaIDult3JlG1ybJ0YKXXzT44XmhbK+Jd9e+6Ho0fA0ejohU8jhzhHIW6NhUfzasT61FUESu5pvysd0by23I5T/40hXgNzjlcaX67DVPesYy6qQ+xSdnkuKYScvzFTYJu+X4pyJ9f65mMVcyc529ISQsmVkNSGq+FvGT8= yanapavlova@MacBook-Air-Ana.local
    EOT

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
(base) yanapavlova@MacBook-Air-Ana ya-cloud % terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_disk.drive will be created
  + resource "yandex_compute_disk" "drive" {
      + block_size  = 4096
      + created_at  = (known after apply)
      + folder_id   = (known after apply)
      + id          = (known after apply)
      + image_id    = "fd8t8vqitgjou20saanq"
      + name        = "drive"
      + product_ids = (known after apply)
      + size        = 21
      + status      = (known after apply)
      + type        = "network-hdd"
      + zone        = "ru-central1-a"
    }

  # yandex_compute_instance.virtual-machine will be created
  + resource "yandex_compute_instance" "virtual-machine" {
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
                ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDchNGxgMkTmR2Z4K9aueY5TGp9KGY3zzl0JVAFWqU7qf4KABontUJbECfqhFnDijPJyM8BDHkB6lxjixmYHJoH2UapwWMentyEABqRdnZ5xeuWxh9W5waybrtn8uub+WEgx17Lhf4z+5N4CioZsEO8dMHGTMkLLUDvtsHfXU127xpGTcwej+Gtgokmrh5cbOipUJInYlxs7YwDoDZlai0YNCh877FIc4cuE9PZCILY5rLWktgKCaYLhJXay9QJOFKEKm8G4XdrogcrBGmEtR/Pbt6gV/p3DAIjDaAve3osmh4nTsguTokKeEYoet+p3klgsmonhk9GpZNGdh+2W/obC/s0a/LGaIDult3JlG1ybJ0YKXXzT44XmhbK+Jd9e+6Ho0fA0ejohU8jhzhHIW6NhUfzasT61FUESu5pvysd0by23I5T/40hXgNzjlcaX67DVPesYy6qQ+xSdnkuKYScvzFTYJu+X4pyJ9f65mMVcyc529ISQsmVkNSGq+FvGT8= yanapavlova@MacBook-Air-Ana.local
            EOT
        }
      + name                      = "virtual-machine"
      + network_acceleration_type = "standard"
      + platform_id               = "standard-v1"
      + service_account_id        = (known after apply)
      + status                    = (known after apply)
      + zone                      = "ru-central1-a"

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
          + core_fraction = 100
          + cores         = 2
          + memory        = 2
        }
    }

  # yandex_vpc_network.network-lab will be created
  + resource "yandex_vpc_network" "network-lab" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = "network-lab"
      + subnet_ids                = (known after apply)
    }

  # yandex_vpc_subnet.lab-subnet will be created
  + resource "yandex_vpc_subnet" "lab-subnet" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = "lab-subnet"
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "192.168.50.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + VM_ip            = (known after apply)
  + instance_ssh_key = <<-EOT
        ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDchNGxgMkTmR2Z4K9aueY5TGp9KGY3zzl0JVAFWqU7qf4KABontUJbECfqhFnDijPJyM8BDHkB6lxjixmYHJoH2UapwWMentyEABqRdnZ5xeuWxh9W5waybrtn8uub+WEgx17Lhf4z+5N4CioZsEO8dMHGTMkLLUDvtsHfXU127xpGTcwej+Gtgokmrh5cbOipUJInYlxs7YwDoDZlai0YNCh877FIc4cuE9PZCILY5rLWktgKCaYLhJXay9QJOFKEKm8G4XdrogcrBGmEtR/Pbt6gV/p3DAIjDaAve3osmh4nTsguTokKeEYoet+p3klgsmonhk9GpZNGdh+2W/obC/s0a/LGaIDult3JlG1ybJ0YKXXzT44XmhbK+Jd9e+6Ho0fA0ejohU8jhzhHIW6NhUfzasT61FUESu5pvysd0by23I5T/40hXgNzjlcaX67DVPesYy6qQ+xSdnkuKYScvzFTYJu+X4pyJ9f65mMVcyc529ISQsmVkNSGq+FvGT8= yanapavlova@MacBook-Air-Ana.local
    EOT

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

yandex_vpc_network.network-lab: Creating...
yandex_compute_disk.drive: Creating...
yandex_vpc_network.network-lab: Creation complete after 5s [id=enp4e31ds7sk7g3ke31f]
yandex_vpc_subnet.lab-subnet: Creating...
yandex_vpc_subnet.lab-subnet: Creation complete after 1s [id=e9bcjch5nftpssldi84c]
yandex_compute_disk.drive: Still creating... [10s elapsed]
yandex_compute_disk.drive: Creation complete after 13s [id=fhm7c9k710khocfpsg7e]
yandex_compute_instance.virtual-machine: Creating...
yandex_compute_instance.virtual-machine: Still creating... [10s elapsed]
yandex_compute_instance.virtual-machine: Still creating... [20s elapsed]
yandex_compute_instance.virtual-machine: Still creating... [30s elapsed]
yandex_compute_instance.virtual-machine: Creation complete after 32s [id=fhmc3ni0jtevgmviudlg]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

VM_ip = "192.168.50.32"
instance_ssh_key = <<EOT
ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDchNGxgMkTmR2Z4K9aueY5TGp9KGY3zzl0JVAFWqU7qf4KABontUJbECfqhFnDijPJyM8BDHkB6lxjixmYHJoH2UapwWMentyEABqRdnZ5xeuWxh9W5waybrtn8uub+WEgx17Lhf4z+5N4CioZsEO8dMHGTMkLLUDvtsHfXU127xpGTcwej+Gtgokmrh5cbOipUJInYlxs7YwDoDZlai0YNCh877FIc4cuE9PZCILY5rLWktgKCaYLhJXay9QJOFKEKm8G4XdrogcrBGmEtR/Pbt6gV/p3DAIjDaAve3osmh4nTsguTokKeEYoet+p3klgsmonhk9GpZNGdh+2W/obC/s0a/LGaIDult3JlG1ybJ0YKXXzT44XmhbK+Jd9e+6Ho0fA0ejohU8jhzhHIW6NhUfzasT61FUESu5pvysd0by23I5T/40hXgNzjlcaX67DVPesYy6qQ+xSdnkuKYScvzFTYJu+X4pyJ9f65mMVcyc529ISQsmVkNSGq+FvGT8= yanapavlova@MacBook-Air-Ana.local

EOT
(base) yanapavlova@MacBook-Air-Ana ya-cloud % terraform state list
yandex_compute_disk.drive
yandex_compute_instance.virtual-machine
yandex_vpc_network.network-lab
yandex_vpc_subnet.lab-subnet
(base) yanapavlova@MacBook-Air-Ana ya-cloud % terraform state show yandex_compute_disk.drive
# yandex_compute_disk.drive:
resource "yandex_compute_disk" "drive" {
    block_size  = 4096
    created_at  = "2024-02-29T08:33:20Z"
    folder_id   = "b1gfcj68k9dikl901ak6"
    id          = "fhm7c9k710khocfpsg7e"
    image_id    = "fd8t8vqitgjou20saanq"
    name        = "drive"
    product_ids = [
        "f2ectu5pkit47tfmaev0",
    ]
    size        = 21
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
(base) yanapavlova@MacBook-Air-Ana ya-cloud % terraform state show yandex_compute_instance.virtual-machine
# yandex_compute_instance.virtual-machine:
resource "yandex_compute_instance" "virtual-machine" {
    created_at                = "2024-02-29T08:33:32Z"
    folder_id                 = "b1gfcj68k9dikl901ak6"
    fqdn                      = "fhmc3ni0jtevgmviudlg.auto.internal"
    id                        = "fhmc3ni0jtevgmviudlg"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDchNGxgMkTmR2Z4K9aueY5TGp9KGY3zzl0JVAFWqU7qf4KABontUJbECfqhFnDijPJyM8BDHkB6lxjixmYHJoH2UapwWMentyEABqRdnZ5xeuWxh9W5waybrtn8uub+WEgx17Lhf4z+5N4CioZsEO8dMHGTMkLLUDvtsHfXU127xpGTcwej+Gtgokmrh5cbOipUJInYlxs7YwDoDZlai0YNCh877FIc4cuE9PZCILY5rLWktgKCaYLhJXay9QJOFKEKm8G4XdrogcrBGmEtR/Pbt6gV/p3DAIjDaAve3osmh4nTsguTokKeEYoet+p3klgsmonhk9GpZNGdh+2W/obC/s0a/LGaIDult3JlG1ybJ0YKXXzT44XmhbK+Jd9e+6Ho0fA0ejohU8jhzhHIW6NhUfzasT61FUESu5pvysd0by23I5T/40hXgNzjlcaX67DVPesYy6qQ+xSdnkuKYScvzFTYJu+X4pyJ9f65mMVcyc529ISQsmVkNSGq+FvGT8= yanapavlova@MacBook-Air-Ana.local
        EOT
    }
    name                      = "virtual-machine"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm7c9k710khocfpsg7e"
        disk_id     = "fhm7c9k710khocfpsg7e"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8t8vqitgjou20saanq"
            name       = "drive"
            size       = 21
            type       = "network-hdd"
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
        ip_address         = "192.168.50.32"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:c1:de:40:9f"
        nat                = true
        nat_ip_address     = "158.160.44.159"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9bcjch5nftpssldi84c"
    }

    placement_policy {
        host_affinity_rules       = []
        placement_group_partition = 0
    }

    resources {
        core_fraction = 100
        cores         = 2
        gpus          = 0
        memory        = 2
    }

    scheduling_policy {
        preemptible = false
    }
}
(base) yanapavlova@MacBook-Air-Ana ya-cloud % terraform state show yandex_vpc_network.network-lab         
# yandex_vpc_network.network-lab:
resource "yandex_vpc_network" "network-lab" {
    created_at                = "2024-02-29T08:33:20Z"
    default_security_group_id = "enpcn30qfqu0pflf9apq"
    folder_id                 = "b1gfcj68k9dikl901ak6"
    id                        = "enp4e31ds7sk7g3ke31f"
    labels                    = {}
    name                      = "network-lab"
    subnet_ids                = []
}
(base) yanapavlova@MacBook-Air-Ana ya-cloud % terraform state show yandex_vpc_subnet.lab-subnet  
# yandex_vpc_subnet.lab-subnet:
resource "yandex_vpc_subnet" "lab-subnet" {
    created_at     = "2024-02-29T08:33:23Z"
    folder_id      = "b1gfcj68k9dikl901ak6"
    id             = "e9bcjch5nftpssldi84c"
    labels         = {}
    name           = "lab-subnet"
    network_id     = "enp4e31ds7sk7g3ke31f"
    v4_cidr_blocks = [
        "192.168.50.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
(base) yanapavlova@MacBook-Air-Ana ya-cloud % terraform output
VM_ip = "192.168.50.32"
instance_ssh_key = <<EOT
ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDchNGxgMkTmR2Z4K9aueY5TGp9KGY3zzl0JVAFWqU7qf4KABontUJbECfqhFnDijPJyM8BDHkB6lxjixmYHJoH2UapwWMentyEABqRdnZ5xeuWxh9W5waybrtn8uub+WEgx17Lhf4z+5N4CioZsEO8dMHGTMkLLUDvtsHfXU127xpGTcwej+Gtgokmrh5cbOipUJInYlxs7YwDoDZlai0YNCh877FIc4cuE9PZCILY5rLWktgKCaYLhJXay9QJOFKEKm8G4XdrogcrBGmEtR/Pbt6gV/p3DAIjDaAve3osmh4nTsguTokKeEYoet+p3klgsmonhk9GpZNGdh+2W/obC/s0a/LGaIDult3JlG1ybJ0YKXXzT44XmhbK+Jd9e+6Ho0fA0ejohU8jhzhHIW6NhUfzasT61FUESu5pvysd0by23I5T/40hXgNzjlcaX67DVPesYy6qQ+xSdnkuKYScvzFTYJu+X4pyJ9f65mMVcyc529ISQsmVkNSGq+FvGT8= yanapavlova@MacBook-Air-Ana.local

EOT
```

### GitHub

```
(base) yanapavlova@MacBook-Air-Ana github % terraform init

Initializing the backend...

Initializing provider plugins...
- Finding latest version of hashicorp/github...
- Installing hashicorp/github v6.0.0...
- Installed hashicorp/github v6.0.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

╷
│ Warning: Additional provider information from registry
│ 
│ The remote registry returned warnings for registry.terraform.io/hashicorp/github:
│ - For users on Terraform 0.13 or greater, this provider has moved to integrations/github. Please update your source in required_providers.
╵

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
(base) yanapavlova@MacBook-Air-Ana github % terraform plan                                              

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "lab-devops-test"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.devops-lab-repo will be created
  + resource "github_repository" "devops-lab-repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Git test repo"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "lab-devops-test"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
      + web_commit_signoff_required = false
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + repo_branch = "main"
  + repo_id     = (known after apply)
  + repo_name   = "lab-devops-test"

───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
(base) yanapavlova@MacBook-Air-Ana github % terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "lab-devops-test"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.devops-lab-repo will be created
  + resource "github_repository" "devops-lab-repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Git test repo"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + has_issues                  = true
      + has_wiki                    = true
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + license_template            = "mit"
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "lab-devops-test"
      + node_id                     = (known after apply)
      + primary_language            = (known after apply)
      + private                     = (known after apply)
      + repo_id                     = (known after apply)
      + squash_merge_commit_message = "COMMIT_MESSAGES"
      + squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      + ssh_clone_url               = (known after apply)
      + svn_url                     = (known after apply)
      + topics                      = (known after apply)
      + visibility                  = "public"
      + web_commit_signoff_required = false
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + repo_branch = "main"
  + repo_id     = (known after apply)
  + repo_name   = "lab-devops-test"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.devops-lab-repo: Creating...
github_repository.devops-lab-repo: Creation complete after 6s [id=lab-devops-test]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=lab-devops-test]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLZpIWc4C0-_E]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

repo_branch = "main"
repo_id = "lab-devops-test"
repo_name = "lab-devops-test"
(base) yanapavlova@MacBook-Air-Ana github % terraform import "github_repository.devops-lab-repo" "S24-core-course-labs"
github_repository.devops-lab-repo: Importing from ID "S24-core-course-labs"...
github_repository.devops-lab-repo: Import prepared!
  Prepared github_repository for import
╷
│ Error: Resource already managed by Terraform
│ 
│ Terraform is already managing a remote object for github_repository.devops-lab-repo. To import to this address you must first remove the existing object from the state.
╵

(base) yanapavlova@MacBook-Air-Ana github % terraform import "github_repository.devops-lab-repo" "S24-core-course-labs"
github_repository.devops-lab-repo: Importing from ID "S24-core-course-labs"...
github_repository.devops-lab-repo: Import prepared!
  Prepared github_repository for import
github_repository.devops-lab-repo: Refreshing state... [id=S24-core-course-labs]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```