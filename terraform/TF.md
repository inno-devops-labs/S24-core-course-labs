# Infrastructure as Code Lab

## Docker
After following the [Docker tutorial](https://learn.hashicorp.com/collections/terraform/docker-get-started) and building the infrastructure, I had the following output for `terraform show`:

```hcl
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
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "dedcb4e2a2b6"
    id                                          = "dedcb4e2a2b66153b89428879d50f85edfa7bb947918217b5cce130f2bf5b020"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60

    ports {
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

And for `terraform state list`:

```hcl
docker_container.nginx
docker_image.nginx
```

`terraform show` after changing the port to 8080:
    
```hcl
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
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "5da207c8cc87"
    id                                          = "5da207c8cc87ea9b19fd46053a0890a50a4c76a07022b39fa623a0d0984d2dc5"
    image                                       = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "ExampleNginxContainer"
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
    stop_signal                                 = "SIGQUIT"
    stop_timeout                                = 0
    tty                                         = false
    wait                                        = false
    wait_timeout                                = 60

    ports {
        external = 8080
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

`terraform output`:

```hcl
container_id = "5da207c8cc87ea9b19fd46053a0890a50a4c76a07022b39fa623a0d0984d2dc5"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
```
## AWS 
After following the [Docker tutorial](https://learn.hashicorp.com/collections/terraform/docker-get-started) and building the infrastructure, I had the following output for `terraform show`:

```hcl
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-830c94e3"
    arn                                  = "arn:aws:ec2:us-west-2:593575877314:instance/i-02683bf6829002f15"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-02683bf6829002f15"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-0ac44420cef4de847"
    private_dns                          = "ip-172-31-24-219.us-west-2.compute.internal"
    private_ip                           = "172.31.24.219"
    public_dns                           = "ec2-54-213-142-9.us-west-2.compute.amazonaws.com"
    public_ip                            = "54.213.142.9"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-06323ab0510cd563e"
    tags                                 = {
        "Name" = "ExampleAppServerInstance"
    }
    tags_all                             = {
        "Name" = "ExampleAppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-08c893e8f08418fc7",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    cpu_options {
        core_count       = 1
        threads_per_core = 1
    }

    credit_specification {
        cpu_credits = "standard"
    }

    enclave_options {
        enabled = false
    }

    maintenance_options {
        auto_recovery = "default"
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_protocol_ipv6          = "disabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = false
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/sda1"
        encrypted             = false
        iops                  = 0
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-0b350a051d110d312"
        volume_size           = 8
        volume_type           = "standard"
    }
}
```

And for `terraform state list`:

```hcl
aws_instance.app_server
```

`terraform show` after changing the `aws_instance.app_server` resource under the provider block in main.tf by replacing the current AMI ID with a new one.

```hcl
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-08d70e59c07c61a3a"
    arn                                  = "arn:aws:ec2:us-west-2:593575877314:instance/i-0fa78c968b5dbd56b"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0fa78c968b5dbd56b"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-0f7240d4dcbf0b741"
    private_dns                          = "ip-172-31-18-112.us-west-2.compute.internal"
    private_ip                           = "172.31.18.112"
    public_dns                           = "ec2-52-10-66-206.us-west-2.compute.amazonaws.com"
    public_ip                            = "52.10.66.206"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-06323ab0510cd563e"
    tags                                 = {
        "Name" = "ExampleAppServerInstance"
    }
    tags_all                             = {
        "Name" = "ExampleAppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-08c893e8f08418fc7",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    cpu_options {
        core_count       = 1
        threads_per_core = 1
    }

    credit_specification {
        cpu_credits = "standard"
    }

    enclave_options {
        enabled = false
    }

    maintenance_options {
        auto_recovery = "default"
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_protocol_ipv6          = "disabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = false
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/sda1"
        encrypted             = false
        iops                  = 100
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-0f39e862f6d03b6bf"
        volume_size           = 8
        volume_type           = "gp2"
    }
}
```

`terraform output`:

```hcl
instance_id = "i-0fa78c968b5dbd56b"
instance_public_ip = "52.10.66.206"
```


# GitHub
After following the [GitHub tutorial](https://dev.to/pwd9000/manage-and-maintain-github-with-terraform-2k86) and building the infrastructure, I had the following output for `terraform show`:

```hcl
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"43df9489cf3ed3339c6c4487c1d32bfc6328221d7db50bda98d447f3707de541\""
    id         = "example-repo"
    rename     = false
    repository = "example-repo"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLZE9V84C00Ox"
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
    description                 = "An example repository managed by Terraform"
    etag                        = "W/\"43df9489cf3ed3339c6c4487c1d32bfc6328221d7db50bda98d447f3707de541\""
    full_name                   = "ahmedXDR/example-repo"
    git_clone_url               = "git://github.com/ahmedXDR/example-repo.git"
    gitignore_template          = "VisualStudio"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/ahmedXDR/example-repo"
    http_clone_url              = "https://github.com/ahmedXDR/example-repo.git"
    id                          = "example-repo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "example-repo"
    node_id                     = "R_kgDOLZE9Vw"
    private                     = false
    repo_id                     = 764493143
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:ahmedXDR/example-repo.git"
    svn_url                     = "https://github.com/ahmedXDR/example-repo"
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

And for `terraform state list`:


```hcl
github_branch_default.main
github_branch_protection.default
github_repository.example_repo
```

## Github-teams

`terraform show` output:

```hcl
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
    description                 = "An example repository managed by Terraform"
    etag                        = "W/\"41feefda7dee0b873af9057f78956f2ec1526db8041da4c32d1a1f320036a85f\""
    full_name                   = "example-org-123/example-repo"
    git_clone_url               = "git://github.com/example-org-123/example-repo.git"
    gitignore_template          = "VisualStudio"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/example-org-123/example-repo"
    http_clone_url              = "https://github.com/example-org-123/example-repo.git"
    id                          = "example-repo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "example-repo"
    node_id                     = "R_kgDOLZFXew"
    private                     = false
    repo_id                     = 764499835
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:example-org-123/example-repo.git"
    svn_url                     = "https://github.com/example-org-123/example-repo"
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

# github_team.dev_team:
resource "github_team" "dev_team" {
    create_default_maintainer = false
    description               = "Development team with write access to repositories"
    etag                      = "W/\"85db0a24fa91669b6a265e275de89ea2a10a8d5c9e5245519d7e31937641f01a\""
    id                        = "9574965"
    members_count             = 0
    name                      = "Dev Team"
    node_id                   = "T_kwDOCaFd8s4Akho1"
    privacy                   = "closed"
    slug                      = "dev-team"
}

# github_team.ops_team:
resource "github_team" "ops_team" {
    create_default_maintainer = false
    description               = "Operations team with admin access to repositories"
    etag                      = "W/\"50ff866f637e9b516c1a2743cbe9af35b391295e6c6bc8ce8ddfb38edbeeea17\""
    id                        = "9574963"
    members_count             = 0
    name                      = "Ops Team"
    node_id                   = "T_kwDOCaFd8s4Akhoz"
    privacy                   = "closed"
    slug                      = "ops-team"
}

# github_team.qa_team:
resource "github_team" "qa_team" {
    create_default_maintainer = false
    description               = "QA team with read access to repositories"
    etag                      = "W/\"70bf89f21d99eb1fb0916d52f19a8721a1cc60eae4f5b1f9b65f0380249f2cbd\""
    id                        = "9574964"
    members_count             = 0
    name                      = "QA Team"
    node_id                   = "T_kwDOCaFd8s4Akho0"
    privacy                   = "closed"
    slug                      = "qa-team"
}

# github_team_repository.dev_team_repo:
resource "github_team_repository" "dev_team_repo" {
    etag       = "W/\"b93919bc20fb9cce4c3c9fd2e2c540251de3b6f102365eb4271a17409a3a8de6\""
    id         = "9574965:example-repo"
    permission = "push"
    repository = "example-repo"
    team_id    = "9574965"
}

# github_team_repository.ops_team_repo:
resource "github_team_repository" "ops_team_repo" {
    etag       = "W/\"d0d0a53ae55b51164f0fe3f98bc09ecf07830d9db63b44c12e8b2ddc96c43427\""
    id         = "9574963:example-repo"
    permission = "admin"
    repository = "example-repo"
    team_id    = "9574963"
}

# github_team_repository.qa_team_repo:
resource "github_team_repository" "qa_team_repo" {
    etag       = "W/\"f168da44565e79fa81f2c5081c45bd6715005387a3cfcd8476fcd9e3ea42ef16\""
    id         = "9574964:example-repo"
    permission = "pull"
    repository = "example-repo"
    team_id    = "9574964"
}
```

And for `terraform state list`:

```hcl
github_repository.example_repo
github_team.dev_team
github_team.ops_team
github_team.qa_team
github_team_repository.dev_team_repo
github_team_repository.ops_team_repo
github_team_repository.qa_team_repo
```

## Best Practices

1. **Use Environment Variables for Sensitive Data**: Never hardcode sensitive information like tokens or passwords. Utilize environment variables (`GITHUB_TOKEN`) to secure API tokens or secrets.

2. **Version Pinning**: Specify versions for your providers (e.g., `version = "~> 5.0"` for the GitHub provider) to avoid unexpected changes when new versions are released.

3. **Resource Naming Conventions**: Use clear, consistent naming conventions for resources and variables to improve readability and manageability.

4. **Organize Resources**: Group related resources into separate files to make your infrastructure as code (IaC) easier to navigate and maintain.

5. **Review Terraform Plans**: Always review the plan Terraform generates before applying it to understand the changes Terraform will make to your infrastructure.

6. **Use .gitignore**: Include a `.gitignore` file in your Terraform directories to exclude sensitive files or directories (like `.terraform/` and `.tfstate` files) from version control.

7. **Regularly Review and Update**: Periodically review and update your Terraform configurations and dependencies to leverage improvements and address any deprecated features or security issues.
