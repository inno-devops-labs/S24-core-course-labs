## Docker Infrastructure Using Terraform

### Install Terraform
```bash
$ choco install terraform
```

### Build the Infrastructure

For Docker, in the docker directory, run the following commands:

```bash
$ terraform init
$ terraform apply
```

### Results

After running `terraform state list`, the following resources are listed:

```bash
$ terraform state list
docker_container.nginx
docker_image.nginx
```

On the browser: http://localhost:8000, 

![Welcome to Nginx](https://i.imgur.com/VG8seVC.png)

```bash
$ terraform state show docker_image.nginx
# docker_image.nginx:
resource "docker_image" "nginx" {
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}
```

```bash
$ terraform state show docker_container.nginx
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
    hostname                                    = "5de582b2c2aa"
    id                                          = "5de582b2c2aadbd6c23539c078fc696fd7eb5fc3394eb7cd1e3c3d2ce6934604"
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
```

### Log with Applied Changes

```bash
docker_container.nginx: Destroying... [id=5de582b2c2aadbd6c23539c078fc696fd7eb5fc3394eb7cd1e3c3d2ce6934604]
docker_container.nginx: Destruction complete after 1s
docker_image.nginx: Destroying... [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx]
docker_image.nginx: Destruction complete after 0s
docker_image.nginx: Creating...
docker_image.nginx: Still creating... [10s elapsed]
docker_image.nginx: Creation complete after 15s [id=sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest]
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=06cd66015598edbab9fa1cd4f21f0427efa3a7bb69c753cc89d637811872f2dc]
```

As shown in the log, the Docker container and image were destroyed and recreated.

### Utilize Input Variables to Rename Your Docker Container

In the `variables.tf` file, add the following:

```hcl
variable "container_name" {
  description = "Value of the name for the Docker container"
  type        = string
  default     = "ExampleNginxContainer"
}
```

After the changes, run the following commands:

```bash
$ terraform apply
docker_container.nginx: Destroying... [id=06cd66015598edbab9fa1cd4f21f0427efa3a7bb69c753cc89d637811872f2dc]
docker_container.nginx: Destruction complete after 1s
docker_container.nginx: Creating...
docker_container.nginx: Creation complete after 1s [id=ed5c751a25077ddfd76ed653c3b2d622e6e71b44e74c9a1e4f93f35e6f8c004c]

Apply complete! Resources: 1 added, 0 changed, 1 destroyed.
```

The Docker container was destroyed and recreated with the new name. It is now named `ExampleNginxContainer`.

<img src="https://i.imgur.com/k2IyvwL.png" alt="ExampleNginxContainer"/>

### Outputs
Uses the `outputs.tf` file to display the container ID and image ID.

```bash
$ terraform output
container_id = "ed5c751a25077ddfd76ed653c3b2d622e6e71b44e74c9a1e4f93f35e6f8c004c"
image_id = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
```


### AWS Infrastructure Using Terraform

```bash
$ terraform state show aws_instance.app_server
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-0171207a7acd2a570"
    arn                                  = "arn:aws:ec2:eu-west-2:654654563150:instance/i-04633992734ffd20e"
    associate_public_ip_address          = true
    availability_zone                    = "eu-west-2a"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-04633992734ffd20e"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-0f7c27655a97cc473"
    private_dns                          = "ip-172-31-20-239.eu-west-2.compute.internal"
    private_ip                           = "172.31.20.239"
    public_dns                           = "ec2-3-8-101-74.eu-west-2.compute.amazonaws.com"
    public_ip                            = "3.8.101.74"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0e24b74da1d798544"
    tags                                 = {
        "Name" = "ExampleAppServerInstance"
    }
    tags_all                             = {
        "Name" = "ExampleAppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-0a810dd8d38fb70c2",
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
        volume_id             = "vol-030c8c8bed96b0ff9"
        volume_size           = 8
        volume_type           = "gp3"
    }
}
```

```bash
$ terraform output
app_server_id = "i-0fc1f8b41accd726e"
```


### GitHub Task
Deploying: 
```bash
$ terraform apply "deploy.tfplan"
github_repository.repo: Creating...
github_repository.repo: Creation complete after 5s [id=DevOps-Lab04-TF]
github_branch_default.main: Creating...
github_branch_default.main: Creation complete after 2s [id=DevOps-Lab04-TF]
github_branch_protection.default: Creating...
github_branch_protection.default: Creation complete after 4s [id=BPR_kwDOLYqsAM4C0s1V]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```
Destroying:
```bash
$ terraform apply "destroy.tfplan"
github_branch_protection.default: Destroying... [id=BPR_kwDOLYqsAM4C0s1V]
github_branch_protection.default: Destruction complete after 1s
github_branch_default.main: Destroying... [id=DevOps-Lab04-TF]
github_branch_default.main: Destruction complete after 1s
github_repository.repo: Destroying... [id=DevOps-Lab04-TF]
github_repository.repo: Destruction complete after 1s

Apply complete! Resources: 0 added, 0 changed, 3 destroyed.
```

### Overall Best Practices

* Use the `terraform plan` command to preview the changes before applying them.
* Use the `terraform apply` command to apply the changes.
* Handle sensitive data with care. Use environment variables or a `.tfvars` file to store sensitive data.
* Utilize `terraform output` to display the outputs instead of using the state file.
* Follow the guidelines from HashiCorp. 