# Terraform

## Docker Terraform infrastructure

### Output of the commands of given tutorial

#### `terraform state show`


```bash
# docker_container.nginx:
resource "docker_container" "nginx" {
    attach                                      = false
    command                                     = [
        "nginx",
        "-g",
        "daemon off;",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    dns                                         = []
    dns_opts                                    = []
    dns_search                                  = []
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    group_add                                   = []
    hostname                                    = "5ef862a5de52"
    id                                          = "5ef862a5de5223851c63bf540c5e46104bcd2ebeb98ed7699386a3ebd76b4428"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    log_opts                                    = {}
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
    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```
#### `terraform state list`
```bash
docker_container.nginx
docker_image.nginx        
```

### Docker container renaming

Commands that I add to implement needed features

#### Created new variable 

```terraform
variable "container_name" {
  description = "New name for the Docker container"
  default     = "new_container_name"
}
```

#### Add reference to new container name var

```terraform
resource "docker_container" "nginx" {
...
  name  = var.container_name
...
}
```

#### Add output commands

```terraform
output "nginx_container_id" {
  value = docker_container.nginx.id
}

output "nginx_image_id" {
  value = docker_image.nginx.id
}

output "nginx_container_name" {
  value = var.container_name
}
```

#### `terraform output`

```terraform
nginx_container_id = "5ac53bcffdbdebcb53492c4f165146a99e3ca69b0d0401368fa42a20c60d6318"
nginx_container_name = "new_container_name"
nginx_image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```

## Github

```bash
github_repository.terraform_repo: Refreshing state... [id=Terraform-Project]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply" which may have affected this plan:

  # github_repository.terraform_repo has changed
  ~ resource "github_repository" "terraform_repo" {
        id                          = "Terraform-Project"
      ~ name                        = "Terraform Project" -> "Terraform-Project"
        # (16 unchanged attributes hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following plan may include actions to undo or respond to    
these changes.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # github_branch_default.main will be created
  + resource "github_branch_default" "main" {
      + branch     = "main"
      + id         = (known after apply)
      + repository = "terraform-project-for-devops-course"
    }

  # github_branch_protection.default will be created
  + resource "github_branch_protection" "default" {
      + allows_deletions                = false
      + allows_force_pushes             = false
      + blocks_creations                = false
      + enforce_admins                  = true
      + id                              = (known after apply)
      + pattern                         = "main"
      + repository_id                   = (known after apply)
      + require_conversation_resolution = true
      + require_signed_commits          = false
      + required_linear_history         = false

      + required_pull_request_reviews {
          + required_approving_review_count = 1
        }
    }

  # github_repository.terraform_repo is tainted, so must be replaced
-/+ resource "github_repository" "terraform_repo" {
      ~ branches                    = [
          - {
              - name      = "main"
              - protected = false
            },
        ] -> (known after apply)
      ~ default_branch              = "main" -> (known after apply)
      ~ etag                        = "W/\"a71cfec853d918a72a5c4015180cca39e917077bd0d8dd6ee9b452c7a89f57f4\"" -> (known after apply)
      ~ full_name                   = "doechon/Terraform-Project" -> (known after apply)
      ~ git_clone_url               = "git://github.com/doechon/Terraform-Project.git" -> (known after apply)
      - has_downloads               = true -> null
      - has_projects                = false -> null
      ~ html_url                    = "https://github.com/doechon/Terraform-Project" -> (known after apply)
      ~ http_clone_url              = "https://github.com/doechon/Terraform-Project.git" -> (known after apply)
      ~ id                          = "Terraform-Project" -> (known after apply)
      - is_template                 = false -> null
      ~ name                        = "Terraform-Project" -> "terraform-project-for-devops-course"
      ~ node_id                     = "R_kgDOLYEyng" -> (known after apply)
      ~ private                     = false -> (known after apply)
      ~ repo_id                     = 763441822 -> (known after apply)

github_repository.terraform_repo: Destroying... [id=Terraform-Project]
github_repository.terraform_repo: Destruction complete after 0s
github_repository.terraform_repo: Creating...
github_repository.terraform_repo: Creation complete after 7s [id=terraform-project-for-devops-course]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=terraform-project-for-devops-course]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYE1Nc4C0iX2]

Apply complete! Resources: 3 added, 0 changed, 1 destroyed.
```
You can check [repo](https://github.com/doechon/terraform-project-for-devops-course) and [branch protection rules](https://github.com/doechon/terraform-project-for-devops-course/settings/branches)

## Best Practises

### Modularization

Each directory (docker and github) contains separate Terraform configurations for different purposes (Docker and GitHub, respectively). This modular approach makes it easier to manage and understand the infrastructure code.

### File Naming 
I've used descriptive filenames such as main.tf, variables.tf, and outputs.tf, which helps in quickly understanding the purpose of each file.

### Provider Configuration
I've declared provider configurations separately in each main.tf file, ensuring clarity and separation of concerns.

### Variable Definitions
Variables are defined in dedicated variables.tf files, providing a clear overview of input parameters and their descriptions.

### Output Definitions
Outputs are defined in outputs.tf files, making it clear what information will be available after the Terraform execution.

### Resource Configuration
Resource configurations are logically organized within each main.tf file, following the Terraform syntax and structure.

### Version Control
I're utilizing version control (assuming Git) to manage your Terraform configurations. This enables collaboration, change tracking, and rollback capabilities.

### Secrets Management
I've marked sensitive variables (like the GitHub token) with sensitive = true in the variables.tf file, indicating that they should be treated securely.

### Documentation 
I've provided descriptions for variables, helping other users understand their purpose and usage.

### Resource Naming 
I've used meaningful names for resources (docker_image.nginx, github_repository.terraform_repo), enhancing readability and maintainability.

### GitHub Branch Protection 
I've implemented a branch protection rule for the default branch in the GitHub configuration, enforcing code review practices and protecting the main branch.
