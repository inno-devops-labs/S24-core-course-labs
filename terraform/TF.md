# Terraform lab

As I used a MacOs, I installed ```brew install terraform```

## Best practicies

#### Separate Configuration Files
Using separate files for outputs.tf and variables.tf is a good practice to organize the terraform code and make it more maintainable.

#### Export for envinroment variables
There is a security constraint to include PAT, tokens and access keys into code, therefore, I used ```export NAME=``` command.

#### Code reusability
Look for opportunities to reuse code by creating modules for common configurations or resources that can be used across multiple projects.

### Version Constraints
Use version constraints for both Terraform and provider versions to ensure compatibility and stability. In this code, version constraints are specified for the AWS and Docker providers.


## Docker

I used a guide from the lab, and created main.tf, outputs.tf and variables.tf. Next, I used ```terrafrom init``` with VPN to build infrastructure.
Next, I launch the following commands:

```
terraform state list
 ```

```    
docker_container.nginx
docker_image.nginx
```
```
terraform state show docker_container.nginx
```

```
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
    hostname                                    = "b38ee238427e"
    id                                          = "b38ee238427e37bcf3d5fd14d9dc080a395dc33f39f31da3ab0d330d539cd098"
    image                                       = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676"
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
        external = 8000
        internal = 80
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```

```
terraform state show docker_image.nginx  
```

```
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676nginx:latest"
    image_id     = "sha256:760b7cbba31e196288effd2af6924c42637ac5e0d67db4de6309f24518844676"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}

```
## AWS (Amazon Web Services)
I created the directory named ```/terraform/cloud``` and add ```main.tf, outputs.tf, variables.tf```

```
terraform apply
```

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # aws_instance.app_server will be created
  + resource "aws_instance" "app_server" {
      + ami                                  = "ami-0a8b4f1d2c3e5a679"
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
aws_instance.app_server: Still creating... [8s elapsed]
aws_instance.app_server: Still creating... [22s elapsed]
aws_instance.app_server: Still creating... [21s elapsed]
aws_instance.app_server: Creation complete after 37s [id=i-0b3d8c6eae2b77f5d]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

instance_id = "i-0b3d8c6eae2b77f5d"
instance_public_ip = "34.241.17.32"
```

```
terraform state show aws_instance.app_server
```

```
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-0a8b4f1d2c3e5a679"
    arn                                  = "arn:aws:ec2:var.region:730335420348:instance/i-0b3d8c6eae2b77f5d"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2b"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0b3d8c6eae2b77f5d"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-0b8c6d2e4f1a7b3c5"
    private_dns                          = "ip-172-25-35-212.us-west-2.compute.internal"
    private_ip                           = "172.25.35.212"
    public_dns                           = "ec2-34-206-31-22.us-west-2.compute.amazonaws.com"
    public_ip                            = "34.206.31.22"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0f8a7e2d6c3b9a1d"
    tags                                 = {
        "Name" = "ExampleAppServerInstance"
    }
    tags_all                             = {
        "Name" = "ExampleAppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-0e0f3d2b1c4a5d6f",
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
        volume_id             = "vol-0e9f1a8c632b7d4e"
        volume_size           = 8
        volume_type           = "gp3"
    }
}
```

## Github

I created the directory named ```/terraform/github``` and add ```main.tf, outputs.tf, variables.tf, provider.tf```.  
Also, I add access token ```export PAT_github_token=<token>```

```
terraform apply
```

```
github_repository.DevOps-Engineering-Labs: Refreshing state... [id=DevOps-Engineering-Labs]
github_branch_default.main: Refreshing state... [id=DevOps-Engineering-Labs]
github_branch_protection.default: Refreshing state... [id=BPR_kwDOLY1cOM4C0vjq]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # github_repository.DevOps-Engineering-Labs will be updated in-place
  ~ resource "github_repository" "DevOps-Engineering-Labs" {
      ~ auto_init                   = false -> true
        id                          = "DevOps-Engineering-Labs"
      + license_template            = "mit"
        name                        = "DevOps-Engineering-Labs"
        # (33 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

github_repository.DevOps-Engineering-Labs: Modifying... [id=DevOps-Engineering-Labs]
github_repository.DevOps-Engineering-Labs: Modifications complete after 3s [id=DevOps-Engineering-Labs]
```

```
terraform state show github_repository.DevOps-Engineering-Labs
```

```
# github_repository.DevOps-Engineering-Labs:
resource "github_repository" "DevOps-Engineering-Labs" {
    allow_auto_merge            = false
    allow_merge_commit          = true
    allow_rebase_merge          = true
    allow_squash_merge          = true
    allow_update_branch         = false
    archived                    = false
    auto_init                   = true
    default_branch              = "main"
    delete_branch_on_merge      = false
    description                 = "DevOps lab"
    etag                        = "W/\"2fa0bf37957e323ea6e3851097754c3aa8625317d575c91bbb6dec414194d8ee\""
    full_name                   = "Bavpnet/DevOps-Engineering-Labs"
    git_clone_url               = "git://github.com/Bavpnet/DevOps-Engineering-Labs.git"
    has_discussions             = false
    has_downloads               = false
    has_issues                  = true
    has_projects                = false
    has_wiki                    = true
    html_url                    = "https://github.com/Bavpnet/DevOps-Engineering-Labs"
    http_clone_url              = "https://github.com/Bavpnet/DevOps-Engineering-Labs.git"
    id                          = "DevOps-Engineering-Labs"
    is_template                 = false
    license_template            = "mit"
    merge_commit_message        = "PR_TITLE"
    merge_commit_title          = "MERGE_MESSAGE"
    name                        = "DevOps-Engineering-Labs"
    node_id                     = "R_kgDOLY1cOA"
    private                     = false
    repo_id                     = 764238904
    squash_merge_commit_message = "COMMIT_MESSAGES"
    squash_merge_commit_title   = "COMMIT_OR_PR_TITLE"
    ssh_clone_url               = "git@github.com:Bavpnet/DevOps-Engineering-Labs.git"
    svn_url                     = "https://github.com/Bavpnet/DevOps-Engineering-Labs"
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