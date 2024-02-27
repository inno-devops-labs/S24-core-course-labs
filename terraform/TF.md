# Docker

Output of the `terraform show` command:

```bash
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "python",
        "time_zone.py",
    ]
    env                                         = []
    hostname                                    = "6ae1008a2c5a"
    id                                          = "6ae1008a2c5ac30cfd11e41bc0bad38d339d35bdc4ab3da8ffd61f2be3d0b3c9"
    image                                       = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdec"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "app_python"
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
    user                                        = "app_python"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/home/app_python"

    ports {
        external = 8000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest"
    image_id     = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdec"
    keep_locally = false
    name         = "nikitagrigorenko/app_python:latest"
    repo_digest  = "nikitagrigorenko/app_python@sha256:7ed4ccf4d20cd45f938f60d9f8e2c3eede216b0d0a64c25c3010e2d297d9cbc3"
}


Outputs:

container_id = "6ae1008a2c5ac30cfd11e41bc0bad38d339d35bdc4ab3da8ffd61f2be3d0b3c9"
image_id = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest"
```

Output of the `terraform show` command:
```bash
docker_container.app_python
docker_image.app_python
```

Output of the `terraform apply` command:
```bash
docker_image.app_python: Refreshing state... [id=sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest]
docker_container.app_python: Refreshing state... [id=03c52d93ac74fd705c149c357288764918208cce6fae677eb556f325b1dd8094]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # docker_container.app_python must be replaced
-/+ resource "docker_container" "app_python" {
      + bridge                                      = (known after apply)
      ~ command                                     = [] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "python",
          - "time_zone.py",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "03c52d93ac74" -> (known after apply)
      ~ id                                          = "03c52d93ac74fd705c149c357288764918208cce6fae677eb556f325b1dd8094" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
        name                                        = "app_python"
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
      - user                                        = "app_python" -> null
      - working_dir                                 = "/home/app_python" -> null
        # (14 unchanged attributes hidden)

      ~ ports {
          ~ internal = 80 -> 5000 # forces replacement
            # (3 unchanged attributes hidden)
        }
    }

Plan: 1 to add, 0 to change, 1 to destroy.

Changes to Outputs:
  ~ container_id = "03c52d93ac74fd705c149c357288764918208cce6fae677eb556f325b1dd8094" -> (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

docker_container.app_python: Destroying... [id=03c52d93ac74fd705c149c357288764918208cce6fae677eb556f325b1dd8094]
docker_container.app_python: Destruction complete after 0s
docker_container.app_python: Creating...
docker_container.app_python: Creation complete after 0s [id=f31bdd5d0c71aa4a9f5a11dd015c1f8d08f73074cf636e8e0d264b18d69e37ef]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.

Outputs:

container_id = "f31bdd5d0c71aa4a9f5a11dd015c1f8d08f73074cf636e8e0d264b18d69e37ef"
image_id = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest"
```

Output of the `terraform output` command:
```bash
container_id = "f31bdd5d0c71aa4a9f5a11dd015c1f8d08f73074cf636e8e0d264b18d69e37ef"
image_id = "sha256:d53bc1efba437c72e441814533df761425156cff065f4882b9c9eb38e807fdecnikitagrigorenko/app_python:latest"
```


# GitHub

Outpur of the `terraform import "github_repository.repo" "sample-repo"`
```bash
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Importing from ID "sample-repo"...
github_repository.repo: Import prepared!
  Prepared github_repository for import
github_repository.repo: Refreshing state... [id=sample-repo]

Import successful!

The resources that were imported are shown above. These resources are now in
your Terraform state and will henceforth be managed by Terraform.
```

Output of the `terraform apply` command:
```bash
var.token
  Specifies the GitHub PAT token or `GITHUB_TOKEN`

  Enter a value: 

github_repository.repo: Refreshing state... [id=sample-repo]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  ~ update in-place

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + etag       = (known after apply)
      + id         = (known after apply)
      + rename     = false
      + repository = "sample-repo"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + lock_branch                     = false
      + pattern                         = "main"
      + repository_id                   = "sample-repo"
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + require_last_push_approval      = false
          + required_approving_review_count = 1
        }
    }

  # github_repository.repo will be updated in-place
  ~ resource "github_repository" "repo" {
      ~ auto_init                   = false -> true
        id                          = "sample-repo"
        name                        = "sample-repo"
        # (33 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 2 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.repo: Modifying... [id=sample-repo]
github_repository.repo: Modifications complete after 2s [id=sample-repo]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=sample-repo]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYp_5c4C0smt]

Apply complete! Resources: 2 added, 1 changed, 0 destroyed.
```

Output of the `terraform show` command:
```bash
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"fab1eaa8ae4fbd70996358bb1c83fc18942f3c08cde6fded64ca8cf4fab98a2b\""
    id         = "sample-repo"
    rename     = false
    repository = "sample-repo"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLYp_5c4C0smt"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "sample-repo"
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

# github_repository.repo:
resource "github_repository" "repo" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Sample Lab4 DevOps"
    etag                        = "W/\"fab1eaa8ae4fbd70996358bb1c83fc18942f3c08cde6fded64ca8cf4fab98a2b\""
    full_name                   = "NikitaGrigorenko/sample-repo"
    git_clone_url               = "git://github.com/NikitaGrigorenko/sample-repo.git"
    has_discussions             = false
    has_downloads               = true
    has_issues                  = true
    has_projects                = true
    has_wiki                    = true
    html_url                    = "https://github.com/NikitaGrigorenko/sample-repo"
    http_clone_url              = "https://github.com/NikitaGrigorenko/sample-repo.git"
    id                          = "sample-repo"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "sample-repo"
    node_id                     = "R_kgDOLYp_5Q"
    private                     = false
    repo_id                     = 764051429
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:NikitaGrigorenko/sample-repo.git"
    svn_url                     = "https://github.com/NikitaGrigorenko/sample-repo"
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
```

Output of the `terraform state list` command:
```bash
github_branch_default.main
github_branch_protection.default
github_repository.repo
```


# GitHub Teams
Output of the `terraform apply` command:
```bash

```


# Best Practices 

- Variables and output were devided into other files. 

- Environment variables were used due to safety reasons.

- The Terraform code has been divided into reusable modules, which encourages code reuse and improves the codebase's readability and maintainability.

- To ensure code quality and readability, the terraform validate command has been used to verify the code for mistakes. Additionally, terraform fmt has been used to automatically format the code in accordance with Terraform's standards.

- Version pinning has been envolved: in order to prevent infrastructure failures caused by provider upgrades, the versions of the Terraform providers have been pinned.
