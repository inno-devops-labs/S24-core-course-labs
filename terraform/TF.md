# Terraform

## Terraform Docker

### `terraform state show` output

```terraform
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
    hostname                                    = "6d0099924874"
    id                                          = "6d0099924874f43037e710c3e46aeac5cbdaca6c82339aef88b42164d3ff9192"
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

### `terraform state list` output

```bash
docker_container.nginx
docker_image.nginx
```

### Docker container renaming
To rename a docker container in Terraform using input variables, you can use the following code:

```terraform
# variables.tf
variable "docker_container_name" {
  description = "Name of the container"
  type        = string
  default     = "nginx"
}

# main.tf
resource "docker_container" "nginx" {
  ...
  name  = var.docker_container_name
  ...
}
```

Then we can create a `terraform.tfvars` file with the following content:

```terraform
docker_container_name = "s24-devops-labs"
```

Now, let's apply the changes:
```bash
terraform destroy -var-file="terraform.tfvars"
```

Now, let's check container name by running `docker ps`:

```bash
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                  NAMES
842ec6a75aa6   e4720093a3c1   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8000->80/tcp   s24-devops-labs
```

### Adding terraform outputs
To add terraform outputs, you can use the following code:

```terraform
# outputs.tf
output "container_id" {
  description = "ID of the Docker container"
  value       = docker_container.nginx.id
}

output "image_id" {
  description = "ID of the Docker image"
  value       = docker_image.nginx.id
}
```

Now, let's run `terraform apply` to apply the changes.

### `terraform output` output

```terraform
container_id = "9620ee30607054724419812faf1fdce289c40b4bc68f904c92bee163ea23b514"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
```

## Terraform AWS

### `terraform state show` output

```terraform
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-830c94e3"
    arn                                  = "arn:aws:ec2:us-west-2:851725596066:instance/i-0bd22aaed913ba65a"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0bd22aaed913ba65a"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-01d45d40bcb565e75"
    private_dns                          = "ip-172-31-27-226.us-west-2.compute.internal"
    private_ip                           = "172.31.27.226"
    public_dns                           = "ec2-54-213-235-215.us-west-2.compute.amazonaws.com"
    public_ip                            = "54.213.235.215"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0693511cf8c80932f"
    tags                                 = {
        "Name" = "ExampleAppServerInstance"
    }
    tags_all                             = {
        "Name" = "ExampleAppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-040a841abab0def28",
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
        iops                  = 0
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-0d207cdec8d161dfc"
        volume_size           = 8
        volume_type           = "standard"
    }
}
```

### `terraform state list` output

```bash
aws_instance.app_server
```

### AWS instance renaming
To rename an AWS instance in Terraform using input variables, you can use the following code:

```terraform
# variables.tf
variable "instance_name" {
  description = "Name of the instance"
  type        = string
  default     = "ExampleAppServerInstance"
}

# main.tf
resource "aws_instance" "app_server" {
  ...
  tags = {
    Name = var.instance_name
  }
  ...
}
```

Then we can create a `terraform.tfvars` file with the following content:

```terraform
instance_name = "s24-devops-labs"
```

Now, let's apply the changes:
```bash
terraform apply -var-file="terraform.tfvars"
```

### Adding terraform outputs
To add terraform outputs, you can use the following code:

```terraform
# outputs.tf
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}
```

Now, let's run `terraform apply` to apply the changes.

### `terraform output` output

```terraform
instance_id = "i-0bd22aaed913ba65a"
instance_public_ip = "54.213.235.215"
```

## Terraform Github Repository, Teams and Organizations (bonus)
Teams with corresponding permissions are stored in the `teams.csv`
and created using for-each syntax in the terraform

```terraform
# Create a team for each row in the CSV file
resource "github_team" "all" {
  for_each = {
    for team in csvdecode(file("teams.csv")) : team.name => team
  }

  name                      = each.value.name
  description               = each.value.description
  privacy                   = each.value.privacy
  create_default_maintainer = true
}

# Add each team to the repository with the permissions specified in the CSV file
resource "github_team_repository" "all" {
  for_each = {
    for team in csvdecode(file("teams.csv")) : team.name => team
  }

  team_id    = github_team.all[each.key].id
  repository = github_repository.repo.name
  permission = each.value.permission
}
```
Each team has different permissions

You can check results at [my organization](https://github.com/s24-devops-organization)


## Terraform Github Best Practices

- **Environment variables**: Use environment variables to store sensitive information such as access keys, secret keys, and other credentials. This will help you avoid hardcoding sensitive information in your code.

- **Use specific versions**: Always use specific versions of the provider to avoid any breaking changes in the future. You can specify the version in the `required_providers` block in your Terraform configuration file.

- **Set Github Branch Protection**: Use Terraform to set up branch protection rules in your Github repositories. This will help you enforce code review and other quality checks before merging changes into the main branch.
