# Terraform

## Table of Contents

- [Terraform](#terraform)
  - [Table of Contents](#table-of-contents)
  - [Docker](#docker)
    - [Building the infrastructure](#building-the-infrastructure)
    - [List of states](#list-of-states)
    - [Details of states](#details-of-states)
    - [Part of the log](#part-of-the-log)
    - [Outputs](#outputs)
  - [AWS](#aws)
    - [Building](#building)
    - [State Details](#state-details)
    - [Partial Log](#partial-log)
    - [Output](#output)
  - [Github](#github)
  - [Github Teams](#github-teams)
  - [Best Practices](#best-practices)

![Output](https://i.postimg.cc/QxStknwW/image.png)

## Docker

### Building the infrastructure

In general I had to do the following before I could use the outputs in the next step:

```bash
terraform init
terraform fmt
terraform validate
terraform apply -var "bun_container_name=test-bun-name" 
```

### List of states

To see the list of states-

```bash
terraform state list
```

The output of the above command is:

```plaintest
docker_container.app_bun
docker_container.app_python
docker_image.app_bun
docker_image.app_python
```

### Details of states

I used the following command to get the details of the states:

```bash
for i in $(terraform state list); do terraform state show $i; echo; done
```

This got me the following output:

```terraform
# docker_container.app_bun:
resource "docker_container" "app_bun" {
    attach                                      = false
    command                                     = [
        "bun",
        "run",
        "entry.js",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "/usr/local/bin/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "068ed1d875a8"
    id                                          = "068ed1d875a861373ce39cd5226bad258d06809f8acdf156860495185fe27741"
    image                                       = "sha256:fcc4e59dccd158b06acc9089e041625530495253e22b4f1b50586e899696e86c"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "test-bun-name"
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
    user                                        = "newuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app/app_bun"

    ports {
        external = 3000
        internal = 3000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "gunicorn",
        "app_python.app:app",
        "-w 4",
        "-b 0.0.0.0:5000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "2adb3f5d9c55"
    id                                          = "2adb3f5d9c5541f4fdfc6499a1775006992d1a5f691144c9e4d7e61b3d025267"
    image                                       = "sha256:5678144561e191cdf37177b4e3c6dda827b5148f4734c2cd440537e8c6124056"
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
    user                                        = "newuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 5000
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_bun:
resource "docker_image" "app_bun" {
    id           = "sha256:fcc4e59dccd158b06acc9089e041625530495253e22b4f1b50586e899696e86cpptx704/app_bun:latest"
    image_id     = "sha256:fcc4e59dccd158b06acc9089e041625530495253e22b4f1b50586e899696e86c"
    keep_locally = true
    name         = "pptx704/app_bun:latest"
    repo_digest  = "pptx704/app_bun@sha256:76ea752b2499f6789b7251693e79408a7111272f17e906f97b06e2fd955fab04"
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:5678144561e191cdf37177b4e3c6dda827b5148f4734c2cd440537e8c6124056pptx704/app_python:latest"
    image_id     = "sha256:5678144561e191cdf37177b4e3c6dda827b5148f4734c2cd440537e8c6124056"
    keep_locally = true
    name         = "pptx704/app_python:latest"
    repo_digest  = "pptx704/app_python@sha256:32478912fd43294c223d608437041c167109cf5cdd9ebbaadebf8a749301ce1c"
}

```

### Part of the log

I changed the bun container name and applied the changes-

```bash
terraform apply -var "bun_container_name=bun-app"
```

Part of the output log-

```terraform
Terraform will perform the following actions:

  # docker_container.app_bun must be replaced
-/+ resource "docker_container" "app_bun" {
      + bridge                                      = (known after apply)
      ~ command                                     = [
          - "bun",
          - "run",
          - "entry.js",
        ] -> (known after apply)
      + container_logs                              = (known after apply)
      - cpu_shares                                  = 0 -> null
      - dns                                         = [] -> null
      - dns_opts                                    = [] -> null
      - dns_search                                  = [] -> null
      ~ entrypoint                                  = [
          - "/usr/local/bin/docker-entrypoint.sh",
        ] -> (known after apply)
      ~ env                                         = [] -> (known after apply)
      + exit_code                                   = (known after apply)
      - group_add                                   = [] -> null
      ~ hostname                                    = "8233a91fb386" -> (known after apply)
      ~ id                                          = "8233a91fb386dab95db5f23b607b2074b73987341661952996d739d7dc29cb19" -> (known after apply)
      ~ init                                        = false -> (known after apply)
      ~ ipc_mode                                    = "private" -> (known after apply)
      ~ log_driver                                  = "json-file" -> (known after apply)
      - log_opts                                    = {} -> null
      - max_retry_count                             = 0 -> null
      - memory                                      = 0 -> null
      - memory_swap                                 = 0 -> null
      ~ name                                        = "test-bun-name" -> "bun-app" # forces replacement
```

Here we can see that the name is being changed from `test-bun-name` to `bun-app` and it is forcing a replacement.

### Outputs

```bash
terraform output
```

The output was following-

```terraform
bun-container-id = "2e069cab42d128f9d628320afbec9ad478a0d2a9629857845367d854be5386e9"
python-container-id = "ff291f1fa252e67bb966271f8d82fa5af042b59b43d66279f507be347c9b4827"
```

## AWS

### Building

Since, the previous infrastructure had docker only, I had to add AWS provider and do the following after changing the `.tf` files-

```bash
terraform init -upgrade
terraform fmt
terraform validate
```

Before I could use AWS resources, I needed to have my IAM credentials set up. So I modified the `~/.aws/config` and wrote the following in it-

```plaintext
[profile rfd]
output = json
aws_access_key_id=<redacted>
aws_secret_access_key=<redacted>
```

To build the AWS resources only, I used `target` flag-

```bash
AWS_PROFILE=rfd terraform apply -target aws_instance.app_server
```

### State Details

There was only one state as `target` flag was used. The details of the state could be checked using the following command-

```bash
terraform state show aws_instance.app_server
```

The output of the above command was-

```terraform
resource "aws_instance" "app_server" {
    ami                                  = "ami-0faab6bdbac9486fb"
    arn                                  = "arn:aws:ec2:eu-central-1:338171648102:instance/i-05981e6e0d4b2c594"
    associate_public_ip_address          = true
    availability_zone                    = "eu-central-1a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-05981e6e0d4b2c594"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-0e049b86102f1cf0d"
    private_dns                          = "ip-172-31-25-94.eu-central-1.compute.internal"
    private_ip                           = "172.31.25.94"
    public_dns                           = "ec2-54-93-186-176.eu-central-1.compute.amazonaws.com"
    public_ip                            = "54.93.186.176"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0ebf661e4a4cf59ff"
    tags                                 = {
        "Name" = "app-server"
    }
    tags_all                             = {
        "Name" = "app-server"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-0c805e49cc530bdd0",
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
        volume_id             = "vol-06621ba32f9bff20d"
        volume_size           = 8
        volume_type           = "gp2"
    }
}
```

### Partial Log

```terraform
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.app_server will be created
  + resource "aws_instance" "app_server" {
      + ami                                  = "ami-0faab6bdbac9486fb"
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
```

This is a part of the log which shows the creation of the `aws_instance.app_server`. We can see that for some of the fields, the value is `known after apply` since the resource is not yet created.

### Output

```bash
terraform output
```

The output was following-

```terraform
aws-public-ip = "54.93.186.176"
```

## Github

Apart from following [this tutorial](https://dev.to/pwd9000/manage-and-maintain-github-with-terraform-2k86), I imported `S24-devops-labs` repository and added branch protection to the `main` branch.

Since the repository already existed, I had to import it first-

```bash
GITHUB_TOKEN=<redacted> terraform import "github_repository.S24-devops-labs" "S24-devops-labs"
```

Afterwards, I running `plan` command, applied the changes using the following command-

```bash
GITHUB_TOKEN=<redacted> terraform apply
```

As I didn't want the repository to be deleted, I removed the states related to the repository using the following command-

```bash
terraform state rm github_repository.S24-devops-labs
terraform state rm github_branch_protection.devops-default
```

Additionally, "lifecycle.prevent_destroy" was set to `true`. This made running `terraform destroy` safe.

## Github Teams

I already had an organization [TeamOmukk](https://github.com/TeamOmukk) with my friends before. So. I decided to use that organization to create teams and add members to it. For PoC, I created 2 repos and 3 teams.

3 Teams were created-
- `reader` that has read access to repositories
- `writer` that has write access to repositories
- `mixed` that has read access for one repository and write access for another repository

Apart from the `reader` team, the other teams are secret teams.

![tf-mock](https://i.postimg.cc/VvYFfJcd/image.png)

![reader](https://i.postimg.cc/4xhpT6hW/image.png)

![all](https://i.postimg.cc/3xp0q3P6/image.png)

## Best Practices

- The files were named based on the resources or their tasks. `main.tf` contained version and providers. `variable.tf` and `outputs.tf` contained the variables and outputs respectively. The other files were named based on the resources they were creating or managing.
- Naming convention followed [terraform-best-practices](https://www.terraform-best-practices.com/naming).
- The secrets are not hardcoded and used as environment variables.
- `terraform fmt` and `terraform validate` were used to format and validate the code.
- `terraform plan` was always used to verify the changes before applying them. Also, `terraform state list` and `terraform state show` were used before destroying any resource.
- `target` flag was used to apply changes to a specific resource when needed.
- For existing resources, `terraform import` was used to import the resources to the state file.
