# Terraform
* ## Docker
### Outputs
* #### Before utilizing input variables to rename your Docker container
   1. #### To prepare my terraform I filled the main.tf with configuration info and applied following commands
    ```bash
    terraform init
    terraform fmt
    terraform validate  
    ```
   2. #### Terraform apply usage
    `terraform apply`
   3. #### Get list of states
    #### Input
    `terraform state list`
    #### Output
    ```text
    docker_container.moscow-time-app
    docker_image.moscow-time-app
    ```
   4. #### Get details of each state
    #### Input
    `for i in $(terraform state list); do echo "--State ${i}--" && terraform state show $i; echo; done`
    #### Output
    ```text
    --State docker_container.moscow-time-app--
  # docker_container.moscow-time-app: docker
  resource "docker_container" "moscow-time-app" {
      attach                                      = false
      command                                     = []
      container_read_refresh_timeout_milliseconds = 15000
      cpu_shares                                  = 0
      entrypoint                                  = [
          "uvicorn",
          "app_python.main:app",
          "--host",
          "0.0.0.0",
          "--port",
          "80",
      ]
      env                                         = []
      hostname                                    = "2c8882a7c8fb"
      id                                          = "2c8882a7c8fb2deb2c2ff9ed30a67f947a626d3e30f9e92f1f98fe47c301c6aa"
      image                                       = "sha256:fb124f12af9d6649662026e11e8e0fbfbaf51fc620e40bace869b6424a63a780"
      init                                        = false
      ipc_mode                                    = "private"
      log_driver                                  = "json-file"
      logs                                        = false
      max_retry_count                             = 0
      memory                                      = 0
      memory_swap                                 = 0
      must_run                                    = true
      name                                        = "moscow-time-app"
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
      working_dir                                 = "/code"
  
      ports {
          external = 8000
          internal = 80
          ip       = "0.0.0.0"
          protocol = "tcp"
      }
  }
  
  --State docker_image.moscow-time-app--
  # docker_image.moscow-time-app:
  resource "docker_image" "moscow-time-app" {
      id           = "sha256:fb124f12af9d6649662026e11e8e0fbfbaf51fc620e40bace869b6424a63a780zaqbez39me/moscow-time-app:latest"
      image_id     = "sha256:fb124f12af9d6649662026e11e8e0fbfbaf51fc620e40bace869b6424a63a780"
      keep_locally = true
      name         = "zaqbez39me/moscow-time-app:latest"
      repo_digest  = "zaqbez39me/moscow-time-app@sha256:34118954c51968a7f98661e3be96e7803c41f8c1a2be702032c65ca74a4c5f30"
  }
  ```
* ### Part of output after application
  ```text
  Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

  Terraform will perform the following actions:

  # docker_container.moscow-time-app will be created
  + resource "docker_container" "moscow-time-app" {
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
      + name                                        = "moscow-time-app"
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

  # docker_image.moscow-time-app will be created
  + resource "docker_image" "moscow-time-app" {
      + id           = (known after apply)
      + image_id     = (known after apply)
      + keep_locally = true
      + name         = "zaqbez39me/moscow-time-app:latest"
      + repo_digest  = (known after apply)
    }

  Plan: 2 to add, 0 to change, 0 to destroy.

  Changes to Outputs:
      + container_id = (known after apply)

  Do you want to perform these actions?
    Terraform will perform the actions described above.
    Only 'yes' will be accepted to approve.
  
    Enter a value: yes

  docker_image.moscow-time-app: Creating...
  docker_image.moscow-time-app: Creation complete after 0s [id=sha256:fb124f12af9d6649662026e11e8e0fbfbaf51fc620e40bace869b6424a63a780zaqbez39me/moscow-time-app:latest]
  docker_container.moscow-time-app: Creating...
  docker_container.moscow-time-app: Creation complete after 0s [id=402285d9cfe6c4fabd525ad7084510d8bb93ea29695f3d40041f88d51f0746fc]
  
  Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
  
  Outputs:

  container_id = "402285d9cfe6c4fabd525ad7084510d8bb93ea29695f3d40041f88d51f0746fc"

  ```
* ### After utilizing input variables to rename your Docker container
  1. #### Terraform apply usage
     `terraform apply -var "container_name=special_app"`
  2. #### Terraform output
     #### Input
     `terraform output`
     #### Output
     ```
     container_id = "7588ada51c7b0337b20e53064267810ba98aaae98bf674b65273724efc980879"
     ```
* ## TWC (Time Web Cloud provider)
* #### Configuration
  Before the starting with terraform, I set the TWC_TOKEN using `export TWC_TOKEN=eyJhbGciOiJSUz...`.
  Then I configured the TWC settings in the twc.tf file using guide on the GitHub page.
  To avoid server name collisions I added `server_name` variable.
* #### Initialization of terraform
  To initialize and verify terraform I used the commands
  ```bash
  terraform init
  terraform validate
  terraform plan
  ```
  #### Application of plan
  To apply the plan I used the command with `server_name` variable
  ```bash
  terraform apply -var "server_name=SERVER_NAME"
  ```
  #### State outputs
  * Output command
  #### Input
  ```bash
  terraform state output
  ```
  #### Output
  ```text
  availability_zone = "spb-2"

  ```
  * State list
  #### Input
  ```bash
  terraform state list
  ```
  #### Output
  ```text
  data.twc_configurator.configurator
  data.twc_os.os
  twc_server.lab-4-serv

  ```
  * States details
  #### Input
  ```bash
  for i in $(terraform state list); do echo "--State ${i}--" && terraform state show $i; echo; done
  ```
  #### Output
  ```text
  --State data.twc_configurator.configurator--
  # data.twc_configurator.configurator:
  data "twc_configurator" "configurator" {
      cpu_frequency = "3.3"
      disk_type     = "nvme"
      id            = "11"
      location      = "ru-1"
  
      requirements {
          cpu_max                = 104
          cpu_min                = 1
          cpu_step               = 1
          disk_max               = 2048000
          disk_min               = 10240
          disk_step              = 5120
          network_bandwidth_max  = 1000
          network_bandwidth_min  = 200
          network_bandwidth_step = 100
          ram_max                = 747520
          ram_min                = 1024
          ram_step               = 1024
      }
  }
  
  --State data.twc_os.os--
  # data.twc_os.os:
  data "twc_os" "os" {
      family           = "linux"
      id               = "79"
      name             = "ubuntu"
      version          = "22.04"
      version_codename = "jammy"
  
      requirements {
          bandwidth_min = 0
          cpu_min       = 0
          disk_min      = 0
          ram_min       = 0
      }
  }
  
  --State twc_server.lab-4-serv--
  # twc_server.lab-4-serv:
  resource "twc_server" "lab-4-serv" {
      availability_zone = "spb-2"
      boot_mode         = "std"
      configurator_id   = 11
      cpu               = 1
      cpu_frequency     = "3.3"
      disks             = [
          {
              id          = 16775213
              is_mounted  = true
              is_system   = true
              size        = 10240
              status      = "done"
              system_name = "vda"
              type        = "nvme"
              used        = 0
          },
      ]
      id                = "2600809"
      is_ddos_guard     = false
      location          = "ru-1"
      main_ipv4         = "92.255.76.90"
      name              = "SERVER_NAME"
      networks          = [
          {
              bandwidth     = 200
              ips           = [
                  {
                      ip      = "2a03:6f00:5:1::e7c"
                      is_main = true
                      ptr     = ""
                      type    = "ipv6"
                  },
                  {
                      ip      = "92.255.76.90"
                      is_main = true
                      ptr     = ""
                      type    = "ipv4"
                  },
              ]
              is_ddos_guard = false
              nat_mode      = ""
              type          = "public"
          },
      ]
      os                = [
          {
              id      = 79
              name    = "ubuntu"
              version = "22.04"
          },
      ]
      os_id             = 79
      preset_id         = 0
      project_id        = 707407
      ram               = 1024
      software          = []
      status            = "installing"
  
      configuration {
          configurator_id = 11
          cpu             = 1
          disk            = 10240
          ram             = 1024
      }
  }


  ```
* ## TWC (Time Web Cloud provider)
* #### Build
  After configuring all the terraform files following example let us build it.
  ```bash
  terraform init
  terraform fmt
  terraform validate  
  terraform plan
  terraform apply
  ```
  As I see everything worked successfully.
* #### Let us check state
  * State list
  #### Input
  ```bash
  terraform state list
  ```
  #### Output
  ```text
  github_branch_default.main
  github_branch_protection.example_branch_protection
  github_repository.example_repo
  ```
  * Each state description
  #### Input
  ```
  for i in $(terraform state list); do echo "--State ${i}--" && terraform state show $i; echo; done
  ```
  #### Output
  ```text
  --State github_branch_default.main--
  # github_branch_default.main:
  resource "github_branch_default" "main" {
      branch     = "main"
      etag       = "W/\"a8b77c00acbab723c161aabb910f4fca1488d9e72e23b246fe937b1d440ab33d\""
      id         = "example-repo"
      rename     = false
      repository = "example-repo"
  }
  
  --State github_branch_protection.example_branch_protection--
  # github_branch_protection.example_branch_protection:
  resource "github_branch_protection" "example_branch_protection" {
      allows_deletions                = false
      allows_force_pushes             = false
      blocks_creations                = false
      enforce_admins                  = true
      id                              = "BPR_kwDOLY60cs4C0xIj"
      lock_branch                     = false
      pattern                         = "main"
      repository_id                   = "example-repo"
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
  
  --State github_repository.example_repo--
  # github_repository.example_repo:
  resource "github_repository" "example_repo" {
      allow_auto_merge            = false
      allow_merge_commit          = true
      allow_rebase_merge          = true
      allow_squash_merge          = true
      allow_update_branch         = false
      archived                    = false
      auto_init                   = true
      default_branch              = "main"
      delete_branch_on_merge      = false
      description                 = "This is an example repository"
      etag                        = "W/\"a8b77c00acbab723c161aabb910f4fca1488d9e72e23b246fe937b1d440ab33d\""
      full_name                   = "zaqbez39me/example-repo"
      git_clone_url               = "git://github.com/zaqbez39me/example-repo.git"
      gitignore_template          = "VisualStudio"
      has_discussions             = false
      has_downloads               = false
      has_issues                  = true
      has_projects                = false
      has_wiki                    = true
      html_url                    = "https://github.com/zaqbez39me/example-repo"
      http_clone_url              = "https://github.com/zaqbez39me/example-repo.git"
      id                          = "example-repo"
      is_template                 = false
      license_template            = "mit"
      merge_commit_message        = "PR_TITLE"
      merge_commit_title          = "MERGE_MESSAGE"
      name                        = "example-repo"
      node_id                     = "R_kgDOLY60cg"
      private                     = false
      repo_id                     = 764327026
      squash_merge_commit_message = "COMMIT_MESSAGES"
      squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
      ssh_clone_url               = "git@github.com:zaqbez39me/example-repo.git"
      svn_url                     = "https://github.com/zaqbez39me/example-repo"
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
* #### Repo importing
  After all, I added the `github_repository` resource with name `S24-DevOps-Labs` and applied
  ```bash
  terraform import "github_repository.S24-DevOps-Labs" "S24-DevOps-Labs"
  ```
  I got no changes because the repo was already existing and the state was already matching requirements.
  
### Best practices
  1. Segregation of .tf configuration file on multiple (main logic, variables and output)
  2. Avoiding of including the secret tokens in the configuration (Using the env variables instead)
  3. Setting the restrictions of providers versions
  4. Splitting not logically connected configurations on different modules (github, docker and twc) 
  5. Avoiding deprecated configuration styles
  6. Avoiding of modifying state manually
  7. Excessively using plan to analyze