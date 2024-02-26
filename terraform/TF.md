# Terraform lab

## Best practises

1. Version Control: Store your Terraform configurations in version control (e.g., Git) to track changes, collaborate with others, and rollback changes if needed.

2. Variables and Outputs: Define variables to parameterize your configurations and outputs to expose important information for other resources or users.

3. Resource Naming: Follow a consistent naming convention for your resources to make it easier to identify and manage them.

4. Environment Separation: Use workspaces or separate directories for different environments (e.g., dev, staging, production) to prevent accidental changes in production.

## Outputs: 

### 1. Docker

Output for `terraform state list` and `terraform state show`

```
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/docker (lab3) $ terraform state list
docker_container.devops-app
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/docker (lab3) $ terraform state show docker_container.devops-app
# docker_container.devops-app:
resource "docker_container" "devops-app" {
    attach                                      = false
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "fc82c4c89d8a"
    id                                          = "fc82c4c89d8a6d009af98b809403fec3b62d7b505cfc80f1cc7053649b445326"
    image                                       = "sha256:58aa10cd902efb1fb312abde9a66af6f51a2e6f2c3c7cac6a84da44f57057eab"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "devops-app"
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
    user                                        = "nonroot"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8080
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/docker (lab3) $ 

```

For `terraform output`:

```
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/docker (lab3) $ terraform output
container_id = "fc82c4c89d8a6d009af98b809403fec3b62d7b505cfc80f1cc7053649b445326"
container_name = "devops-app"
```


### 2. AWS

```
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/aws (lab3) $ terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.app_server will be created
  + resource "aws_instance" "app_server" {
      + ami                                  = "ami-052c9ea013e6e3567"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = (known after apply)
      + availability_zone                    = (known after apply)
      + cpu_core_count                       = (known after apply)
      + cpu_threads_per_core                 = (known after apply)
      + disable_api_stop                     = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + host_resource_group_arn              = (known after apply)
      + iam_instance_profile                 = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t2.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = (known after apply)
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + source_dest_check                    = true
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "Name" = "ExampleAppServerInstance"
        }
      + tags_all                             = {
          + "Name" = "ExampleAppServerInstance"
        }
      + tenancy                              = (known after apply)
      + user_data                            = (known after apply)
      + user_data_base64                     = (known after apply)
      + user_data_replace_on_change          = false
      + vpc_security_group_ids               = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + instance_id        = (known after apply)
  + instance_public_ip = (known after apply)

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_instance.app_server: Creating...
aws_instance.app_server: Still creating... [10s elapsed]
aws_instance.app_server: Still creating... [20s elapsed]
aws_instance.app_server: Still creating... [30s elapsed]
aws_instance.app_server: Creation complete after 34s [id=i-0a4faab7ad1a88e0c]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

instance_id = "i-0a4faab7ad1a88e0c"
instance_public_ip = "34.212.41.26"
```

```
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/aws (lab3) $ terraform state list
aws_instance.app_server
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/aws (lab3) $ terraform state show aws_instance.app_server
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-052c9ea013e6e3567"
    arn                                  = "arn:aws:ec2:us-west-2:730335420348:instance/i-0a4faab7ad1a88e0c"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2b"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0a4faab7ad1a88e0c"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-09717a4130ff83a34"
    private_dns                          = "ip-172-31-30-206.us-west-2.compute.internal"
    private_ip                           = "172.31.30.206"
    public_dns                           = "ec2-34-212-41-26.us-west-2.compute.amazonaws.com"
    public_ip                            = "34.212.41.26"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0cd541c69bf34e5ff"
    tags                                 = {
        "Name" = "ExampleAppServerInstance"
    }
    tags_all                             = {
        "Name" = "ExampleAppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-0cdd8fd1a2b726160",
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
        http_put_response_hop_limit = 2
        http_tokens                 = "required"
        instance_metadata_tags      = "disabled"
    }

    private_dns_name_options {
        enable_resource_name_dns_a_record    = false
        enable_resource_name_dns_aaaa_record = false
        hostname_type                        = "ip-name"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/xvda"
        encrypted             = false
        iops                  = 3000
        tags                  = {}
        throughput            = 125
        volume_id             = "vol-0c6b927f745464b36"
        volume_size           = 8
        volume_type           = "gp3"
    }
}
```

### 3. Github

Insert your token in the ENV `export TF_VAR_github_PAtoken="<token>"`

```
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/github (lab3) $ terraform apply
github_repository.devops-test-repo: Refreshing state... [id=devops-test-repo]
github_branch_default.main: Refreshing state... [id=devops-test-repo]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
  - destroy
-/+ destroy and then create replacement

Terraform will perform the following actions:

  # github_branch_default.main must be replaced
-/+ resource "github_branch_default" "main" {
      ~ etag       = "W/\"405481d9ff074e1286f0ffc220c60accb12e38531a02e665f77427a903815d72\"" -> (known after apply)
      ~ id         = "devops-test-repo" -> (known after apply)
      ~ repository = "devops-test-repo" -> "devops-test" # forces replacement
        # (2 unchanged attributes hidden)
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

  # github_repository.devops-test will be created
  + resource "github_repository" "devops-test" {
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
      + name                        = "devops-test"
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

  # github_repository.devops-test-repo will be destroyed
  # (because github_repository.devops-test-repo is not in configuration)
  - resource "github_repository" "devops-test-repo" {
      - allow_auto_merge            = false -> null
      - allow_merge_commit          = true -> null
      - allow_rebase_merge          = true -> null
      - allow_squash_merge          = true -> null
      - allow_update_branch         = false -> null
      - archived                    = false -> null
      - auto_init                   = true -> null
      - default_branch              = "main" -> null
      - delete_branch_on_merge      = false -> null
      - description                 = "Test terraform for devops lab" -> null
      - etag                        = "W/\"405481d9ff074e1286f0ffc220c60accb12e38531a02e665f77427a903815d72\"" -> null
      - full_name                   = "blinikar/devops-test-repo" -> null
      - git_clone_url               = "git://github.com/blinikar/devops-test-repo.git" -> null
      - has_discussions             = false -> null
      - has_downloads               = false -> null
      - has_issues                  = true -> null
      - has_projects                = false -> null
      - has_wiki                    = true -> null
      - html_url                    = "https://github.com/blinikar/devops-test-repo" -> null
      - http_clone_url              = "https://github.com/blinikar/devops-test-repo.git" -> null
      - id                          = "devops-test-repo" -> null
      - is_template                 = false -> null
      - license_template            = "mit" -> null
      - merge_commit_message        = "PR_TITLE" -> null
      - merge_commit_title          = "MERGE_MESSAGE" -> null
      - name                        = "devops-test-repo" -> null
      - node_id                     = "R_kgDOLYUZOA" -> null
      - private                     = false -> null
      - repo_id                     = 763697464 -> null
      - squash_merge_commit_message = "COMMIT_MESSAGES" -> null
      - squash_merge_commit_title   = "COMMIT_OR_PR_TITLE" -> null
      - ssh_clone_url               = "git@github.com:blinikar/devops-test-repo.git" -> null
      - svn_url                     = "https://github.com/blinikar/devops-test-repo" -> null
      - topics                      = [] -> null
      - visibility                  = "public" -> null
      - vulnerability_alerts        = false -> null
      - web_commit_signoff_required = false -> null

      - security_and_analysis {
          - secret_scanning {
              - status = "disabled" -> null
            }
          - secret_scanning_push_protection {
              - status = "disabled" -> null
            }
        }
    }

Plan: 3 to add, 0 to change, 2 to destroy.

Changes to Outputs:
  ~ repository_id   = "devops-test" -> (known after apply)
  ~ repository_name = "devops-test-repo" -> "devops-test"

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_branch_default.main: Destroying... [id=devops-test-repo]
github_branch_default.main: Destruction complete after 0s
github_repository.devops-test-repo: Destroying... [id=devops-test-repo]
github_repository.devops-test: Creating...
github_repository.devops-test-repo: Destruction complete after 1s
github_repository.devops-test: Creation complete after 7s [id=devops-test]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 1s [id=devops-test]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYUh5c4C0mJq]

Apply complete! Resources: 3 added, 0 changed, 2 destroyed.

Outputs:

default_branch = "main"
repository_id = "devops-test"
repository_name = "devops-test"
@blinikar ➜ /workspaces/S24-core-course-labs/terraform/github (lab3) $ 
```