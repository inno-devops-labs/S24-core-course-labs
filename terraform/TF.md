## Docker

### Building
The following commands were used for building:
```
terraform init
terraform fmt
terraform validate
terraform apply -var "container_name=app" 
```

### Terraform state list
By running `terraform state list` command, I got the following output:

```
docker_container.app_python
docker_image.app_python
```

### Terraform show

This is the output of the `terraform show` command:

```
# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "python",
        "/app_python/app.py",
        "--host",
        "0.0.0.0",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "d6d21d4ca4cf"
    id                                          = "d6d21d4ca4cf8ec9eca59bcfd30e5019c1121c4e6c4ab2edd7eddbe88e24c0d9"
    image                                       = "sha256:ec852bb874df9ab07a6f3376e9590d3e547a80e8563064cf86ade8a3e3cda171"
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
    user                                        = "myuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:ec852bb874df9ab07a6f3376e9590d3e547a80e8563064cf86ade8a3e3cda171mostafakira/app_python:latest"
    image_id     = "sha256:ec852bb874df9ab07a6f3376e9590d3e547a80e8563064cf86ade8a3e3cda171"
    keep_locally = false
    name         = "mostafakira/app_python:latest"
    repo_digest  = "mostafakira/app_python@sha256:9bb626323f20c71d21d10d85631748b1e3639c63d1a1f8b367e049b6189236f6"
}
```

### Output
By running `terraform output` command, I got the following output:

```
container-id = "d6d21d4ca4cf8ec9eca59bcfd30e5019c1121c4e6c4ab2edd7eddbe88e24c0d9"
```

## AWS

### Building
The following commands were used for building:
```
terraform init
terraform validate
terraform apply -var "aws_tag_name=AppServerInstance" 
```

### Terraform State List

By running `terraform state list` command, I got the following output:

```
aws_instance.app_server
```

### Terraform show
This is the output of the `terraform show` command:
```
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-830c94e3"
    arn                                  = "arn:aws:ec2:us-west-2:195079873263:instance/i-0dc6c4d8479fe4b45"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2b"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0dc6c4d8479fe4b45"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-0e49e4bbecb78d201"
    private_dns                          = "ip-172-31-23-68.us-west-2.compute.internal"
    private_ip                           = "172.31.23.68"
    public_dns                           = "ec2-34-213-83-71.us-west-2.compute.amazonaws.com"
    public_ip                            = "34.213.83.71"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-09cfe4f959ea1bac6"
    tags                                 = {
        "Name" = "AppServerInstance"
    }
    tags_all                             = {
        "Name" = "AppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-09e6f3a95edee0aee",
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
        volume_id             = "vol-0819cad23a781de85"
        volume_size           = 8
        volume_type           = "standard"
    }
}
```

### Output
By running `terraform output` command, I got the following output:

```
aws-public-ip = "34.213.83.71"
```

## Github

### Building
The following commands were used for building:
```
terraform init
terraform validate
terraform apply
```

### Terraform State List

By running `terraform state list` command, I got the following output:

```
github_branch_default.main
github_branch_protection.devops
github_branch_protection.repo
github_repository.S24-devops-labs
github_repository.repo
```

### Terraform Show
This is the output of the `terraform show` command:
```
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"8276086385241728bf5c456b01217a7c94c4d547b917e513806c1bcae275cff5\""
    id         = "Terraform-Initialized-Repo"
    rename     = false
    repository = "Terraform-Initialized-Repo"
}

# github_branch_protection.devops:
resource "github_branch_protection" "devops" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLY2jX84C0v5o"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "S24-devops-labs"
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

# github_branch_protection.repo:
resource "github_branch_protection" "repo" {
    allows_deletions                = false
    allows_force_pushes             = false
    blocks_creations                = false
    enforce_admins                  = true
    force_push_bypassers            = []
    id                              = "BPR_kwDOLY2fQ84C0v4t"
    lock_branch                     = false
    pattern                         = "main"
    push_restrictions               = []
    repository_id                   = "Terraform-Initialized-Repo"
    require_conversation_resolution = true
    require_signed_commits          = false
    required_linear_history         = false

    required_pull_request_reviews {
        dismiss_stale_reviews           = false
        dismissal_restrictions          = []
        pull_request_bypassers          = []
        require_code_owner_reviews      = false
        require_last_push_approval      = false
        required_approving_review_count = 1
        restrict_dismissals             = false
    }
}

# github_repository.S24-devops-labs:
resource "github_repository" "S24-devops-labs" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    default_branch              = "main"
    delete_branch_on_merge      = false
    etag                        = "W/\"f3c2dface46661c2ff783ce018c44fd35df9d13848c58260d5ef72ec75e90618\""
    full_name                   = "MostafaKhaled2017/S24-devops-labs"
    git_clone_url               = "git://github.com/MostafaKhaled2017/S24-devops-labs.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/MostafaKhaled2017/S24-devops-labs"
    http_clone_url              = "https://github.com/MostafaKhaled2017/S24-devops-labs.git"
    id                          = "S24-devops-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S24-devops-labs"
    node_id                     = "R_kgDOLY2jXw"
    private                     = false
    repo_id                     = 764257119
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:MostafaKhaled2017/S24-devops-labs.git"
    svn_url                     = "https://github.com/MostafaKhaled2017/S24-devops-labs"
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
    description                 = "Test repository created by Terraform for IU S24 DevOps course."
    etag                        = "W/\"8276086385241728bf5c456b01217a7c94c4d547b917e513806c1bcae275cff5\""
    full_name                   = "MostafaKhaled2017/Terraform-Initialized-Repo"
    git_clone_url               = "git://github.com/MostafaKhaled2017/Terraform-Initialized-Repo.git"
    gitignore_template          = "Python"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = false
    has_projects                = false
    has_wiki                    = false
    html_url                    = "https://github.com/MostafaKhaled2017/Terraform-Initialized-Repo"
    http_clone_url              = "https://github.com/MostafaKhaled2017/Terraform-Initialized-Repo.git"
    id                          = "Terraform-Initialized-Repo"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "Terraform-Initialized-Repo"
    node_id                     = "R_kgDOLY2fQw"
    private                     = false
    repo_id                     = 764256067
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:MostafaKhaled2017/Terraform-Initialized-Repo.git"
    svn_url                     = "https://github.com/MostafaKhaled2017/Terraform-Initialized-Repo"
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

## Best Practices
- The secrets are not hardcoded and used as environment variables.
- Naming convention followed terraform-best-practices.
- `terraform fmt` and `terraform validate` were used to format and validate the code.