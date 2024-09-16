# Terraform

## Docker Provider

Outputs for `terraform state list` and `terraform state show docker_container.devops-lab-python-app`


```bash
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/docker$ terraform state list
docker_container.devops-lab-python-app
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/docker$ terraform state show docker_container.devops-lab-python-app
# docker_container.devops-lab-python-app:
resource "docker_container" "devops-lab-python-app" {
    attach                                      = false
    command                                     = [
        "python",
        "-u",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "0f1931fd5950"
    id                                          = "0f1931fd595077fe56486fbb7728ef93acf461a0cabc5c8c33f3c4c6b0fdd78f"
    image                                       = "sha256:0cce169121ddaf11aa84ae6958c38a075e6d0ec4fbebcccb204b86417ad2920f"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devops-lab-python-app"
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
    user                                        = "lab_user"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/home/lab_user/app"

    healthcheck {
        interval     = "30s"
        retries      = 3
        start_period = "5s"
        test         = [
            "CMD-SHELL",
            "python -c \"import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(1); s.connect(('localhost', 5000))\" || exit 1",
        ]
        timeout      = "10s"
    }

    ports {
        external = 8080
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/docker$ terraform output
container_id = "e72444e5ad9b0f1c0608ad4b672b5fdde2b964d9af342174be3149e39eaedbc6"
container_name = "devops-lab-python-app"
```

## Yandex-cloud Provider

Export variable using `export TF_VAR_secret-token=<token>`

```
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/yandex-cloud$ terraform state list
yandex_compute_disk.boot-drive-1
yandex_compute_instance.devops-lab-machine
yandex_vpc_network.network-devops-lab
yandex_vpc_subnet.subnet-devops-lab
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/yandex-cloud$ terraform state show yandex_compute_disk.boot-drive-1
# yandex_compute_disk.boot-drive-1:
resource "yandex_compute_disk" "boot-drive-1" {
    block_size  = 4096
    created_at  = "2024-02-25T17:10:58Z"
    folder_id   = "b1gg65k13122o9pouqi4"
    id          = "fhm5jobpkf2npi1rh2cq"
    image_id    = "fd8t8vqitgjou20saanq"
    name        = "boot-drive-1"
    product_ids = [
        "f2ectu5pkit47tfmaev0",
    ]
    size        = 10
    status      = "ready"
    type        = "network-hdd"
    zone        = "ru-central1-a"

    disk_placement_policy {}
}
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/yandex-cloud$ terraform state show yandex_compute_instance.devops-lab-machine
# yandex_compute_instance.devops-lab-machine:
resource "yandex_compute_instance" "devops-lab-machine" {
    created_at                = "2024-02-25T17:11:07Z"
    folder_id                 = "b1gg65k13122o9pouqi4"
    fqdn                      = "fhm8g7ctmpu94j8sjnf0.auto.internal"
    id                        = "fhm8g7ctmpu94j8sjnf0"
    metadata                  = {
        "ssh-keys" = <<-EOT
            ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDwsAOcndyOht/SX3EZUphvS+wHZ+nA40KmLL6qKFf406S9M/Z+nbK27HZASSEm8PVvvnaO/b9rB0Om6nQoNRcv8ZYPqwJMMuKcS+86T0ACL4AiuNS98MFwnVw/Ei1rhbwC56H4IwA2WIesX9kZ1x91Uj4vBvhMOXeMXWci3EcP1nhnKe9F68Grb4aqJPzRVqAwy4l9cuj7uLDAxuus0h9cJM2LkME34/4yo8d7z1oOCbHuUXlKeUaAlgRVz3A9ew8kKC5LU4V+lwszYJwS8woF6mKQvGYQATWD9ha82AwgxEETvc/qYD0TXhsORE/XeaG7QhdAY0Ga0lp4PztvdaiZMPaepcK7i2sqWyDJpaFXSld+I/DW17+d4Mp/twlxpT6K5lLYzqyNznzerJKmlydReHixVZR6O14nTR0SdIWk6RsZPNFG+lcv1Buory/ctvXZUE0gtwCXcznISTlBuf6etMLu7doEgbVMBeYG2uIsQDKr0wqegVyRL6XC9hghRhM= fatm1nd@fatm1nd-IdeaPad-5-14ARE05
        EOT
    }
    name                      = "devops-lab-machine"
    network_acceleration_type = "standard"
    platform_id               = "standard-v1"
    status                    = "running"
    zone                      = "ru-central1-a"

    boot_disk {
        auto_delete = true
        device_name = "fhm5jobpkf2npi1rh2cq"
        disk_id     = "fhm5jobpkf2npi1rh2cq"
        mode        = "READ_WRITE"

        initialize_params {
            block_size = 4096
            image_id   = "fd8t8vqitgjou20saanq"
            name       = "boot-drive-1"
            size       = 10
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
        ip_address         = "192.168.40.32"
        ipv4               = true
        ipv6               = false
        mac_address        = "d0:0d:88:1d:9d:b6"
        nat                = true
        nat_ip_address     = "158.160.117.143"
        nat_ip_version     = "IPV4"
        security_group_ids = []
        subnet_id          = "e9b22p8h61qtpraladq4"
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
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/yandex-cloud$ terraform state show yandex_vpc_network.network-devops-lab
# yandex_vpc_network.network-devops-lab:
resource "yandex_vpc_network" "network-devops-lab" {
    created_at                = "2024-02-25T17:10:58Z"
    default_security_group_id = "enpjrqj1e59iif06oro3"
    folder_id                 = "b1gg65k13122o9pouqi4"
    id                        = "enplrm4njvkbqftmqv41"
    labels                    = {}
    name                      = "network-devops-lab"
    subnet_ids                = []
}
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/yandex-cloud$ terraform state show yandex_vpc_subnet.subnet-devops-lab
# yandex_vpc_subnet.subnet-devops-lab:
resource "yandex_vpc_subnet" "subnet-devops-lab" {
    created_at     = "2024-02-25T17:11:01Z"
    folder_id      = "b1gg65k13122o9pouqi4"
    id             = "e9b22p8h61qtpraladq4"
    labels         = {}
    name           = "subnet-devops-lab"
    network_id     = "enplrm4njvkbqftmqv41"
    v4_cidr_blocks = [
        "192.168.40.0/24",
    ]
    v6_cidr_blocks = []
    zone           = "ru-central1-a"
}
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/yandex-cloud$ terraform output
instance_ip = "192.168.40.32"
instance_ssh_key = <<EOT
ubuntu:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDwsAOcndyOht/SX3EZUphvS+wHZ+nA40KmLL6qKFf406S9M/Z+nbK27HZASSEm8PVvvnaO/b9rB0Om6nQoNRcv8ZYPqwJMMuKcS+86T0ACL4AiuNS98MFwnVw/Ei1rhbwC56H4IwA2WIesX9kZ1x91Uj4vBvhMOXeMXWci3EcP1nhnKe9F68Grb4aqJPzRVqAwy4l9cuj7uLDAxuus0h9cJM2LkME34/4yo8d7z1oOCbHuUXlKeUaAlgRVz3A9ew8kKC5LU4V+lwszYJwS8woF6mKQvGYQATWD9ha82AwgxEETvc/qYD0TXhsORE/XeaG7QhdAY0Ga0lp4PztvdaiZMPaepcK7i2sqWyDJpaFXSld+I/DW17+d4Mp/twlxpT6K5lLYzqyNznzerJKmlydReHixVZR6O14nTR0SdIWk6RsZPNFG+lcv1Buory/ctvXZUE0gtwCXcznISTlBuf6etMLu7doEgbVMBeYG2uIsQDKr0wqegVyRL6XC9hghRhM= fatm1nd@fatm1nd-IdeaPad-5-14ARE05

EOT
subnet_id = "e9b22p8h61qtpraladq4"
```

## GitHub Provider

Make `export TF_VAR_github_token="<your token"` before execution

```
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "test-devops-terraform-repo"
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

  # github_repository.test-devops-terraform-repo will be created
  + resource "github_repository" "test-devops-terraform-repo" {
      + allow_auto_merge            = false
      + allow_merge_commit          = true
      + allow_rebase_merge          = true
      + allow_squash_merge          = true
      + archived                    = false
      + auto_init                   = true
      + default_branch              = (known after apply)
      + delete_branch_on_merge      = false
      + description                 = "Test terraform for devops lab"
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
      + name                        = "test-devops-terraform-repo"
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

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.test-devops-terraform-repo: Creating...
github_repository.test-devops-terraform-repo: Creation complete after 5s [id=test-devops-terraform-repo]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=test-devops-terraform-repo]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYR2F84C0lWf]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform state show
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
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform state list
github_branch_default.main
github_branch_protection.default
github_repository.test-devops-terraform-repo
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform state show github_repository.test-devops-terraform-repo
# github_repository.test-devops-terraform-repo:
resource "github_repository" "test-devops-terraform-repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Test terraform for devops lab"
    etag                        = "W/\"b1d00f16c0fd0b0937a430fdb074b5c3101930b52774410ec1ff4b2e9fa59235\""
    full_name                   = "fatm1nd/test-devops-terraform-repo"
    git_clone_url               = "git://github.com/fatm1nd/test-devops-terraform-repo.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/fatm1nd/test-devops-terraform-repo"
    http_clone_url              = "https://github.com/fatm1nd/test-devops-terraform-repo.git"
    id                          = "test-devops-terraform-repo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "test-devops-terraform-repo"
    node_id                     = "R_kgDOLYR2Fw"
    private                     = false
    repo_id                     = 763655703
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:fatm1nd/test-devops-terraform-repo.git"
    svn_url                     = "https://github.com/fatm1nd/test-devops-terraform-repo"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
    web_commit_signoff_required = false

    security_and_analysis {
        secret_scanning {
            status = "disabled"
        }
        secret_scanning_push_protection {
            status = "disabled"
        }
    }
}
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform state show github_branch_protection.default
# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLYR2F84C0lWf"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "test-devops-terraform-repo"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform state show github_repository.test-devops-terraform-repo
# github_repository.test-devops-terraform-repo:
resource "github_repository" "test-devops-terraform-repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Test terraform for devops lab"
    etag                        = "W/\"b1d00f16c0fd0b0937a430fdb074b5c3101930b52774410ec1ff4b2e9fa59235\""
    full_name                   = "fatm1nd/test-devops-terraform-repo"
    git_clone_url               = "git://github.com/fatm1nd/test-devops-terraform-repo.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/fatm1nd/test-devops-terraform-repo"
    http_clone_url              = "https://github.com/fatm1nd/test-devops-terraform-repo.git"
    id                          = "test-devops-terraform-repo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "test-devops-terraform-repo"
    node_id                     = "R_kgDOLYR2Fw"
    private                     = false
    repo_id                     = 763655703
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:fatm1nd/test-devops-terraform-repo.git"
    svn_url                     = "https://github.com/fatm1nd/test-devops-terraform-repo"
    topics                      = []
    visibility                  = "public"
    vulnerability_alerts        = false
    web_commit_signoff_required = false

    security_and_analysis {
        secret_scanning {
            status = "disabled"
        }
        secret_scanning_push_protection {
            status = "disabled"
        }
    }
}
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform apply
github_repository.test-devops-terraform-repo: Refreshing state... [id=test-devops-terraform-repo]
github_branch_default.main: Refreshing state... [id=test-devops-terraform-repo]
github_branch_protection.default: Refreshing state... [id=BPR_kwDOLYR2F84C0lWf]

Changes to Outputs:
  + default_branch  = "main"
  + repository_id   = "test-devops-terraform-repo"
  + repository_name = "test-devops-terraform-repo"

You can apply this plan to save these new output values to the Terraform state, without changing any real infrastructure.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes


Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

Outputs:

default_branch = "main"
repository_id = "test-devops-terraform-repo"
repository_name = "test-devops-terraform-repo"
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform output
default_branch = "main"
repository_id = "test-devops-terraform-repo"
repository_name = "test-devops-terraform-repo"
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/terraform/github$ terraform import "github_repository.test-devops-terraform-repo" "beerCoinToken"
github_repository.test-devops-terraform-repo: Importing from ID "beerCoinToken"...
github_repository.test-devops-terraform-repo: Import prepared!
  Prepared github_repository for import
github_repository.test-devops-terraform-repo: Refreshing state... [id=beerCoinToken]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.

```