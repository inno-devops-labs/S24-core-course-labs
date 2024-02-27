# Terraform

## Setup
0. `cd terraform/` from the root of `S24-core-course-labs`
1. As I'm using MacOS, I have installed terraform via `brew install terraform`
2. Created `.terraformrc` provider config (for the further steps - YandexCloud) in home directory, then `terraform init`

## Best practices
1. Use reusable modules (cloud, github) to avoid code duplication
2. Separate terraform project on different levels - directories for each module to keep all structure clear
3. Use `terraform plan` and `terraform validate` to check your work before applying
4. Use `terraform fmt` for formatting your declarations
5. Use **variables** to parametrize your solution
6. Use **outputs** to keep significant values in easy access
7. Do not put validation tokens or credentials/sensitive data inside your declarations
8. Take as less resources as you your solution allows you to reduces cloud spending (cloud could be really expensive for companies)
9. Use only reliable providers and always update the version of modules and machines you are going to use


## Docker infrastructure
1. I have created `docker` folder (module), where store `main.tf`, `variables.tf` and `outputs.tf` files to configure Docker infrastructure
2. I have added `main.tf` and `outputs.tf` files, and setup Docker infrastructure using p.1 above
3. Complete `terraform init` + `terraform aply`

- `terraform apply`

```

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.app_python.docker_container.python_app will be created
  + resource "docker_container" "python_app" {
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
      + name                                        = "python_app"
      + network_data                                = (known after apply)
      + read_only                                   = false
      + remove_volumes                              = true
      + restart                                     = "no"
      + rm                                          = true
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
          + external = 5000
          + internal = 8000
          + ip       = "0.0.0.0"
          + protocol = "tcp"
        }
    }

  # module.app_python.docker_image.img will be created
  + resource "docker_image" "img" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = false
      + name         = "adarika/devops-lab-02-python"
      + repo_digest  = (known after apply)
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + python_container_id = (known after apply)
╷
│ Warning: Redundant empty provider block
│ 
│   on docker/main.tf line 10:
│   10: provider "docker" {}
│ 
│ Earlier versions of Terraform used empty provider blocks ("proxy provider configurations") for child modules to declare their need to be passed a provider
│ configuration by their callers. That approach was ambiguous and is now deprecated.
│ 
│ If you control this module, you can migrate to the new declaration syntax by removing all of the empty provider "docker" blocks and then adding or updating
│ an entry like the following to the required_providers block of module.app_python:
│     docker = {
│       source = "kreuzwerker/docker"
│     }
╵

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

module.app_python.docker_image.img: Creating...
module.app_python.docker_image.img: Creation complete after 0s [id=sha256:fec22b03a2921d5de22e4862160413e6e65908b9b7295ef52e419d9ea9a61bb0adarika/devops-lab-02-python]
module.app_python.docker_container.python_app: Creating...
module.app_python.docker_container.python_app: Creation complete after 1s [id=2bb9652cbe04d5604f6ec75ef4cb2fd139bf6f65ceef5195bba575df4f14431e]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

python_container_id = "2bb9652cbe04d5604f6ec75ef4cb2fd139bf6f65ceef5195bba575df4f14431e"
```

- `terraform state list`:
```
adari_ka@MacBookPro terraform % terraform state list                                  
module.app_python.docker_container.python_app
module.app_python.docker_image.img
```
- `terraform state show module.app_python.docker_container.python_app`:
```
adari_ka@MacBookPro terraform % terraform state show module.app_python.docker_container.python_app
# module.app_python.docker_container.python_app:
resource "docker_container" "python_app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "bash",
        "start.sh",
    ]
    env                                         = []
    hostname                                    = "6b83cca23ec8"
    id                                          = "6b83cca23ec82dc6341c22779a7d7ca36776ab41b56af8f75e403827bcc1adcd"
    image                                       = "sha256:fec22b03a2921d5de22e4862160413e6e65908b9b7295ef52e419d9ea9a61bb0"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python_app"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = ""
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.3"
            ip_prefix_length          = 16
            ipv6_gateway              = ""
            mac_address               = "02:42:ac:11:00:03"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "default"
    privileged                                  = false
    publish_all_ports                           = false
    read_only                                   = false
    remove_volumes                              = true
    restart                                     = "no"
    rm                                          = true
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
    working_dir                                 = "/usr/src/app"

    ports {
        external = 5000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
- `terraform state show module.app_python.docker_image.img`:
```
adari_ka@MacBookPro terraform % terraform state show module.app_python.docker_image.img      
# module.app_python.docker_image.img:
resource "docker_image" "img" {
    id           = "sha256:fec22b03a2921d5de22e4862160413e6e65908b9b7295ef52e419d9ea9a61bb0adarika/devops-lab-02-python"
    image_id     = "sha256:fec22b03a2921d5de22e4862160413e6e65908b9b7295ef52e419d9ea9a61bb0"
    keep_locally = false
    name         = "adarika/devops-lab-02-python"
    repo_digest  = "adarika/devops-lab-02-python@sha256:00aaea6f6d1a61f0e2519ea5d950d18017a538ca9f0b29b9fd1ace6cbfbbb88a"
}
```
- `terraform output`:
```
adari_ka@MacBookPro terraform % terraform output    
python_container_id = "6b83cca23ec82dc6341c22779a7d7ca36776ab41b56af8f75e403827bcc1adcd"
```

## Cloud infrastructure
> I have used Yandex Cloud, [manual link](https://cloud.yandex.ru/ru/docs/tutorials/infrastructure-management/terraform-quickstart#macos_1)
>

1. As I mentoined above, I have setup provider config in `.terraformrc` for Yandex Cloud
2. Created a `yandex_cloud` folder with files `main.tf` (here I setup provider also), `variables.tf` and `outputs.tf`.
3. I have added Cloud module in the general `main.tf` and  modify `outputs.tf` files, then setup Cloud infrastructure using p.2 above; `terraform init`

- `terraform apply`:
```
module.app_python.docker_image.img: Refreshing state... [id=sha256:fec22b03a2921d5de22e4862160413e6e65908b9b7295ef52e419d9ea9a61bb0adarika/devops-lab-02-python]
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts: Reading...
module.app_python.docker_container.python_app: Refreshing state... [id=2bb9652cbe04d5604f6ec75ef4cb2fd139bf6f65ceef5195bba575df4f14431e]
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts: Read complete after 0s [id=fd8hnnsnfn3v88bk0k1o]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.yandex_cloud.yandex_compute_instance.default will be created
  + resource "yandex_compute_instance" "default" {
      + allow_stopping_for_update = true
      + created_at                = (known after apply)
      + folder_id                 = (known after apply)
      + fqdn                      = (known after apply)
      + gpu_cluster_id            = (known after apply)
      + hostname                  = (known after apply)
      + id                        = (known after apply)
      + maintenance_grace_period  = (known after apply)
      + maintenance_policy        = (known after apply)
      + name                      = "devops-lab"
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

          + initialize_params {
              + block_size  = (known after apply)
              + description = (known after apply)
              + image_id    = "fd8hnnsnfn3v88bk0k1o"
              + name        = (known after apply)
              + size        = (known after apply)
              + snapshot_id = (known after apply)
              + type        = "network-hdd"
            }
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
          + memory        = 4
        }

      + scheduling_policy {
          + preemptible = true
        }
    }

  # module.yandex_cloud.yandex_vpc_address.vm1 will be created
  + resource "yandex_vpc_address" "vm1" {
      + created_at          = (known after apply)
      + deletion_protection = (known after apply)
      + folder_id           = (known after apply)
      + id                  = (known after apply)
      + labels              = (known after apply)
      + name                = "terraform1"
      + reserved            = (known after apply)
      + used                = (known after apply)

      + external_ipv4_address {
          + address                  = (known after apply)
          + ddos_protection_provider = (known after apply)
          + outgoing_smtp_capability = (known after apply)
          + zone_id                  = "ru-central1-a"
        }
    }

  # module.yandex_cloud.yandex_vpc_network.networklab will be created
  + resource "yandex_vpc_network" "networklab" {
      + created_at                = (known after apply)
      + default_security_group_id = (known after apply)
      + folder_id                 = (known after apply)
      + id                        = (known after apply)
      + labels                    = (known after apply)
      + name                      = (known after apply)
      + subnet_ids                = (known after apply)
    }

  # module.yandex_cloud.yandex_vpc_subnet.networklab will be created
  + resource "yandex_vpc_subnet" "networklab" {
      + created_at     = (known after apply)
      + folder_id      = (known after apply)
      + id             = (known after apply)
      + labels         = (known after apply)
      + name           = (known after apply)
      + network_id     = (known after apply)
      + v4_cidr_blocks = [
          + "10.228.0.0/24",
        ]
      + v6_cidr_blocks = (known after apply)
      + zone           = "ru-central1-a"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + vm_external_ip      = (known after apply)
╷
│ Warning: Redundant empty provider block
│ 
│   on docker/main.tf line 10:
│   10: provider "docker" {}
│ 
│ Earlier versions of Terraform used empty provider blocks ("proxy provider configurations") for child modules to declare their need to be passed a provider
│ configuration by their callers. That approach was ambiguous and is now deprecated.
│ 
│ If you control this module, you can migrate to the new declaration syntax by removing all of the empty provider "docker" blocks and then adding or updating
│ an entry like the following to the required_providers block of module.app_python:
│     docker = {
│       source = "kreuzwerker/docker"
│     }
╵

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

module.yandex_cloud.yandex_vpc_network.networklab: Creating...
module.yandex_cloud.yandex_vpc_address.vm1: Creating...
module.yandex_cloud.yandex_vpc_network.networklab: Creation complete after 3s [id=enp2bfv1hmuvll6v3e5q]
module.yandex_cloud.yandex_vpc_subnet.networklab: Creating...
module.yandex_cloud.yandex_vpc_subnet.networklab: Creation complete after 1s [id=e9bhla8e6nrhd83qmh4c]
module.yandex_cloud.yandex_vpc_address.vm1: Creating...
module.yandex_cloud.yandex_vpc_address.vm1: Creation complete after 1s [id=e9bs9llj2t9jvijjpblh]
module.yandex_cloud.yandex_compute_instance.default: Creating...
module.yandex_cloud.yandex_compute_instance.default: Still creating... [10s elapsed]
module.yandex_cloud.yandex_compute_instance.default: Still creating... [20s elapsed]
module.yandex_cloud.yandex_compute_instance.default: Still creating... [30s elapsed]
module.yandex_cloud.yandex_compute_instance.default: Creation complete after 38s [id=fhmt2ll1p9235apbsu5i]

Apply complete! Resources: 5 added, 0 changed, 0 destroyed.

Outputs:

python_container_id = "2bb9652cbe04d5604f6ec75ef4cb2fd139bf6f65ceef5195bba575df4f14431e"
vm_external_ip = "62.84.117.83"
```


- `terraform state list`:
```
adari_ka@MacBookPro terraform % terraform state list                                   
module.app_python.docker_container.python_app
module.app_python.docker_image.img
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts
module.yandex_cloud.yandex_compute_instance.default
module.yandex_cloud.yandex_vpc_address.vm1
module.yandex_cloud.yandex_vpc_network.networklab
module.yandex_cloud.yandex_vpc_subnet.networklab
```
- `terraform state show module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts`
```
adari_ka@MacBookPro terraform % terraform state show module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts
# module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts:
data "yandex_compute_image" "ubuntu-2204-lts" {
    created_at    = "2024-02-26T10:56:26Z"
    description   = "ubuntu 22.04 lts"
    family        = "ubuntu-2204-lts"
    folder_id     = "standard-images"
    id            = "fd8hnnsnfn3v88bk0k1o"
    image_id      = "fd8hnnsnfn3v88bk0k1o"
    labels        = {}
    min_disk_size = 8
    name          = "ubuntu-22-04-lts-v20240226"
    os_type       = "linux"
    pooled        = true
    product_ids   = [
        "f2ej6hk1qmuqu40ku14r",
    ]
    size          = 7
    status        = "ready"
}
```
- `terraform state show module.yandex_cloud.yandex_compute_instance.default`
```
adari_ka@MacBookPro terraform % terraform state show module.yandex_cloud.yandex_compute_instance.default          
# module.yandex_cloud.yandex_compute_instance.default:
resource "yandex_compute_instance" "default" {
    allow_stopping_for_update = true
    created_at                = "2024-02-26T19:50:07Z"
    folder_id                 = "b1gig8rbrvamd4b31tul"
    fqdn                      = "fhm6usooe62r633ioq6o.auto.internal"
    id                        = "fhm6usooe62r633ioq6o"
    labels                    = {}
    metadata                  = {}
    name                      = "devops-lab"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm67dn2q0qv1hj3fr65"
        disk_id     = "fhm67dn2q0qv1hj3fr65"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8hnnsnfn3v88bk0k1o"
            size       = 8
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
        ip_address         = "10.228.0.25"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:6f:73:18:71"
        nat                = true
        nat_ip_address     = "158.160.43.220"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b7t34s1o6u7a9lhd4k"
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
        preemptible = true
    }
}
```
- `terraform state show module.yandex_cloud.yandex_vpc_address.vm1`
```
adari_ka@MacBookPro terraform % terraform state show module.yandex_cloud.yandex_vpc_address.vm1
# module.yandex_cloud.yandex_vpc_address.vm1:
resource "yandex_vpc_address" "vm1" {
    created_at          = "2024-02-26T19:33:44Z"
    deletion_protection = false
    folder_id           = "b1gig8rbrvamd4b31tul"
    id                  = "e9bph8l0n61h83nhu078"
    labels              = {}
    name                = "terraform1"
    reserved            = true
    used                = true

    external_ipv4_address {
        address = "158.160.43.220"
        zone_id = "ru-central1-a"
    }
}
```
- `terraform state show module.yandex_cloud.yandex_vpc_network.networklab`
```
adari_ka@MacBookPro terraform % terraform state show module.yandex_cloud.yandex_vpc_network.networklab
# module.yandex_cloud.yandex_vpc_network.networklab:
resource "yandex_vpc_network" "networklab" {
    created_at                = "2024-02-26T19:33:44Z"
    default_security_group_id = "enpcqcpqkubvtj4dpp70"
    folder_id                 = "b1gig8rbrvamd4b31tul"
    id                        = "enp87rmd8ejpl9rj8esq"
    labels                    = {}
    subnet_ids                = [
        "e9b7t34s1o6u7a9lhd4k",
    ]
}
```
- `terraform state show module.yandex_cloud.yandex_vpc_subnet.networklab`
```
adari_ka@MacBookPro terraform % terraform state show module.yandex_cloud.yandex_vpc_subnet.networklab
# module.yandex_cloud.yandex_vpc_subnet.networklab:
resource "yandex_vpc_subnet" "networklab" {
    created_at     = "2024-02-26T19:33:45Z"
    folder_id      = "b1gig8rbrvamd4b31tul"
    id             = "e9b7t34s1o6u7a9lhd4k"
    labels         = {}
    network_id     = "enp87rmd8ejpl9rj8esq"
    v4_cidr_blocks = [
        "10.228.0.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
```

## Terrafoem for GitHub

1. Created a `github` folder (module) with files `main.tf` (here I setup provider also), `variables.tf` and `outputs.tf`.
2. Added github module in the general `main.tf` + modify `outputs.tf` files, and setup github infrastructure
3. `terraform init`, `terraform apply`

- `terraform apply`
> output is too long, so I have desided to cut it to main part, more detailed info about states is below
```
...
Enter a value: yes

module.github.github_repository.core: Creating...
module.github.github_repository.repo: Creating...
module.github.github_repository.repo: Still creating... [10s elapsed]
module.github.github_repository.core: Still creating... [10s elapsed]
module.github.github_repository.repo: Creation complete after 10s [id=devops-repo]
module.github.github_branch_default.main: Creating...
module.github.github_repository.core: Creation complete after 10s [id=devops-test]
module.github.github_branch_default.core_main: Creating...
module.github.github_branch_default.main: Creation complete after 3s [id=devops-repo]
module.github.github_branch_protection.default: Creating...
module.github.github_branch_default.core_main: Creation complete after 4s [id=devops-test]
module.github.github_branch_protection.default: Creation complete after 5s [id=BPR_kwDOLYYDKs4C0nI6]

Apply complete! Resources: 5 added, 0 changed, 0 destroyed.

Outputs:

github_repo_name = "adarika/devops-repo"
python_container_id = "2bb9652cbe04d5604f6ec75ef4cb2fd139bf6f65ceef5195bba575df4f14431e"
vm_external_ip = "62.84.117.83"
```

- `terraform state list`
```
adari_ka@MacBookPro terraform % terraform state list                                          
module.app_python.docker_container.python_app
module.app_python.docker_image.img
module.github.github_branch_default.core_main
module.github.github_branch_default.main
module.github.github_branch_protection.default
module.github.github_repository.core
module.github.github_repository.repo
module.yandex_cloud.data.yandex_compute_image.ubuntu-2204-lts
module.yandex_cloud.yandex_compute_instance.default
module.yandex_cloud.yandex_vpc_address.vm1
module.yandex_cloud.yandex_vpc_network.networklab
module.yandex_cloud.yandex_vpc_subnet.networklab
```

- as an example `terraform state show module.github.github_repository.repo`
```
# module.github.github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = false
    allow_squash_merge          = false
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "devops lab repo"
    etag                        = "W/\"a4b9e663b8f95e58f54e80143ec26cb0767eef42e68de3b8997e3567e8921eb0\""
    full_name                   = "adarika/devops-repo"
    git_clone_url               = "git://github.com/adarika/devops-repo.git"
    gitignore_template          = "VisualStudio"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/adarika/devops-repo"
    http_clone_url              = "https://github.com/adarika/devops-repo.git"
    id                          = "devops-repo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "devops-repo"
    node_id                     = "R_kgDOLYXKwA"
    private                     = false
    repo_id                     = 763742912
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:adarika/devops-repo.git"
    svn_url                     = "https://github.com/adarika/devops-repo"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false

    security_and_analysis {
        secret_scanning {
            status = "disabled"
        }
        secret_scanning_push_protection {
            status = "disabled"
        }
    }
}
```

## GitHub Teams infrastructure
> https://github.com/intaby/devops-repo
> all premissions have been applied (I have checked it in settigs - devs group with maintain role)

- `terraform apply`
> I have cut out log a little
```
...

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.github_teams.github_repository.example_repo will be created
  + resource "github_repository" "example_repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "example"
      + etag                        = (known after apply)
      + full_name                   = (known after apply)
      + git_clone_url               = (known after apply)
      + html_url                    = (known after apply)
      + http_clone_url              = (known after apply)
      + id                          = (known after apply)
      + merge_commit_message        = "PR_TITLE"
      + merge_commit_title          = "MERGE_MESSAGE"
      + name                        = "devops-repo"
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
    }

  # module.github_teams.github_team_repository.developers will be created
  + resource "github_team_repository" "developers" {
      + etag       = (known after apply)
      + id         = (known after apply)
      + permission = "maintain"
      + repository = "devops-repo"
      + team_id    = "9570382"
    }

Plan: 2 to add, 0 to change, 0 to destroy.
╷
│ Warning: Redundant empty provider block
│ 
│   on docker/main.tf line 10:
│   10: provider "docker" {}
│ 
│ Earlier versions of Terraform used empty provider blocks ("proxy provider configurations") for child modules to declare their need to be passed a provider
│ configuration by their callers. That approach was ambiguous and is now deprecated.
│ 
│ If you control this module, you can migrate to the new declaration syntax by removing all of the empty provider "docker" blocks and then adding or updating
│ an entry like the following to the required_providers block of module.app_python:
│     docker = {
│       source = "kreuzwerker/docker"
│     }
╵

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

module.github_teams.github_repository.example_repo: Creating...
module.github_teams.github_repository.example_repo: Creation complete after 5s [id=devops-repo]
module.github_teams.github_team_repository.developers: Creating...
module.github_teams.github_team_repository.developers: Creation complete after 2s [id=9570382:devops-repo]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```