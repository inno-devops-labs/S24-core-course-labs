# Terraform

## Docker
### Outputs for the following commands:

```bash
terraform state show
terraform state list
```

```bash
# docker_container.python-app:
resource "docker_container" "python-app" {
    attach                                      = false
    command                                     = [
        "uvicorn",
        "app_python.app:app",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "3de7b2c51f4e"
    id                                          = "3de7b2c51f4e0b4aca4d8bf3203bab53c3b5220cdf69eee431d6bd0563dc5438"
    image                                       = "sha256:297b206bb4f0cfec23a8744a686b7c4d72aeb93c5f2d1f2d2649360e02f3254b"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python-app"
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
    working_dir                                 = "/app"

    ports {
        external = 8080
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```
# docker_container.rust-app:
resource "docker_container" "rust-app" {
    attach                                      = false
    command                                     = []
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "./learning-rust",
    ]
    env                                         = []
    hostname                                    = "eb42d671a817"
    id                                          = "eb42d671a817beaf6e9913f606a29819d83fb1ab85f114b888f1d68f80fccb1a"
    image                                       = "sha256:de5bc88c3eb19b3e20dbd323ed2b61809902f6bcc941cbd20d5113f2c4732f42"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "rust-app"
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
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8081
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

### Outputs for the following commands:

```bash
terraform output
```

```bash
python_container_id = "3de7b2c51f4e0b4aca4d8bf3203bab53c3b5220cdf69eee431d6bd0563dc5438"
python_container_name = "python-app"
rust_container_id = "eb42d671a817beaf6e9913f606a29819d83fb1ab85f114b888f1d68f80fccb1a"
rust_container_name = "rust-app"
```

## Amazon Web Services

### Outputs for the following commands:

```bash
terraform state show
terraform state list
```

```bash# aws_instance.application_server:
resource "aws_instance" "application_server" {
    ami                                  = "ami-0faab6bdbac9486fb"
    arn                                  = "arn:aws:ec2:eu-central-1:282160524889:instance/i-0c87d039556d746d0"
    associate_public_ip_address          = true
    availability_zone                    = "eu-central-1a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0c87d039556d746d0"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-00ab946aed1832421"
    private_dns                          = "ip-172-31-22-239.eu-central-1.compute.internal"
    private_ip                           = "172.31.22.239"
    public_dns                           = "ec2-18-157-158-58.eu-central-1.compute.amazonaws.com"
    public_ip                            = "18.157.158.58"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0626d7c68fc9f281b"
    tags                                 = {
        "Name" = "app-server"
    }
    tags_all                             = {
        "Name" = "app-server"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-0c522df23a8429e2d",
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
        volume_id             = "vol-0f8972c54d091f5d5"
        volume_size           = 8
        volume_type           = "gp2"
    }
}
```

### Outputs for the following commands:
```bash
terraform output
```

```bash
public-ip-for-aws_instance = "18.157.158.58"
```

## Github

### Outputs for the following commands:

```bash
terraform state show
terraform state list
```

```bash
# github_branch_default.main:
resource "github_branch_default" "main" {
    branch     = "main"
    etag       = "W/\"58f244a06a5f6bdf4e7f4f50ef25eb676d3c85e2a4fb603a2216541b3092d1b3\""
    id         = "iac_lab"
    rename     = false
    repository = "iac_lab"
}

# github_branch_protection.default:
resource "github_branch_protection" "default" {
    allows_deletions                = false
    allows_force_pushes             = false
    enforce_admins                  = true
    id                              = "BPR_kwDOLYji284C0qqc"
    lock_branch                     = false
    pattern                         = "main"
    repository_id                   = "iac_lab"
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

# github_repository.S24-core-course-labs:
resource "github_repository" "S24-core-course-labs" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = false
    default_branch              = "main"
    delete_branch_on_merge      = false
    etag                        = "W/\"ace60832f4fe7230246e3887ebae5cde5fbf2937ba03ae9a07ca472757393746\""
    full_name                   = "Ejedavy/S24-core-course-labs"
    git_clone_url               = "git://github.com/Ejedavy/S24-core-course-labs.git"
    has_discussions             = false
    has_downloads               = true
    has_issues                  = false
    has_projects                = true
    has_wiki                    = true
    html_url                    = "https://github.com/Ejedavy/S24-core-course-labs"
    http_clone_url              = "https://github.com/Ejedavy/S24-core-course-labs.git"
    id                          = "S24-core-course-labs"
    is_template                 = false
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "S24-core-course-labs"
    node_id                     = "R_kgDOLOYssA"
    private                     = false
    repo_id                     = 753282224
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Ejedavy/S24-core-course-labs.git"
    svn_url                     = "https://github.com/Ejedavy/S24-core-course-labs"
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

# github_repository.iac_lab:
resource "github_repository" "iac_lab" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "Test github repository"
    etag                        = "W/\"58f244a06a5f6bdf4e7f4f50ef25eb676d3c85e2a4fb603a2216541b3092d1b3\""
    full_name                   = "Ejedavy/iac_lab"
    git_clone_url               = "git://github.com/Ejedavy/iac_lab.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/Ejedavy/iac_lab"
    http_clone_url              = "https://github.com/Ejedavy/iac_lab.git"
    id                          = "iac_lab"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "iac_lab"
    node_id                     = "R_kgDOLYji2w"
    private                     = false
    repo_id                     = 763945691
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Ejedavy/iac_lab.git"
    svn_url                     = "https://github.com/Ejedavy/iac_lab"
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

### Outputs for the following commands:

```bash
terraform output
```

```bash
branch = "main"
id = "iac_lab"
name = "iac_lab"
```

### Importing an existing repository
[![image.png](https://i.postimg.cc/9QrDSCHm/image.png)](https://postimg.cc/87gkf8C9)

### Best Practices followed
- Files were named according to the resources they were associated with or the tasks they performed. For example, `main.tf` included versioning and provider information, while `variable.tf` and `outputs.tf` were designated for variables and outputs, respectively. Additional files were named according to the resources they managed or created.
- A naming convention was adhered to, as recommended by terraform-best-practices.
- Secrets were not embedded directly in the code but were instead handled through environment variables.
- The commands `terraform fmt` and `terraform validate` were utilized for code formatting and validation.
- Before applying changes, `terraform plan` was consistently used for a preliminary review. Furthermore, commands like `terraform state list` and `terraform state show` were employed for due diligence prior to the deletion of any resources.
- The target flag was strategically used to apply modifications to specific resources as necessary.
- For integrating pre-existing resources, terraform import was leveraged to incorporate those resources into the state file.