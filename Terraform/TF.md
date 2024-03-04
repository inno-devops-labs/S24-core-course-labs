# Terraform

## Docker Terraform Tutorial

- After following the tutorial from [Docker](https://developer.hashicorp.com/terraform/tutorials/docker-get-started/), I have created a Terraform configuration to deploy a simple Docker container.

```bash
    terraform show
```

- The output of the above command:

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
    entrypoint                                  = [
        "/docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "9a22417ce714"
    id                                          = "9a22417ce714d5f3d1832142bcd6b2d71139b726423ce5f4ffa6b7fb343870dd"
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
    id           = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666anginx:latest"
    image_id     = "sha256:e4720093a3c1381245b53a5a51b417963b3c4472d3f47fc301930a4f3b17666a"
    keep_locally = false
    name         = "nginx:latest"
    repo_digest  = "nginx@sha256:c26ae7472d624ba1fafd296e73cecc4f93f853088e6a9c13c0d52f6ca5865107"
}


Outputs:

docker_container_external_port = 8000
```

- About the state list

```bash
    terraform state list
```

- The output of the above command:

```bash
    docker_container.nginx
    docker_image.nginx
```

## Verify the Deployed Docker Container

![Command outputs](./screenshots/terraform-docker.png)

## Use `-var` to Rename the Docker Container

![alt text](./screenshots/docker-rename.png)

## AWS Terraform Tutorial

- After following the tutorial from [AWS](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/aws-build?in=terraform%2Faws-get-started), I have created a Terraform configuration to deploy a simple AWS EC2 instance.

```bash
    terraform show
```

- The output of the above command:

```bash
# aws_instance.app_server:
resource "aws_instance" "app_server" {
    ami                                  = "ami-830c94e3"
    arn                                  = "arn:aws:ec2:us-west-2:058264266933:instance/i-0048eb7045b2e82ad"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2b"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    id                                   = "i-0048eb7045b2e82ad"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    monitoring                           = false
    primary_network_interface_id         = "eni-0c868b627997f4819"
    private_dns                          = "ip-172-31-27-103.us-west-2.compute.internal"
    private_ip                           = "172.31.27.103"
    public_dns                           = "ec2-54-203-51-181.us-west-2.compute.amazonaws.com"
    public_ip                            = "54.203.51.181"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0926272d181f1589a"
    tags                                 = {
        "Name" = "example-instance"
    }
    tags_all                             = {
        "Name" = "example-instance"
    }
    tenancy                              = "default"
    vpc_security_group_ids               = [
        "sg-02ef03b380832a5bc",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    credit_specification {
        cpu_credits = "standard"
    }

    enclave_options {
        enabled = false
    }

    metadata_options {
        http_endpoint               = "enabled"
        http_put_response_hop_limit = 1
        http_tokens                 = "optional"
        instance_metadata_tags      = "disabled"
    }

    root_block_device {
        delete_on_termination = true
        device_name           = "/dev/sda1"
        encrypted             = false
        iops                  = 0
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-076be94ff5fa7fc0f"
        volume_size           = 8
        volume_type           = "standard"
    }
}


Outputs:

public_ip = "54.203.51.181"

```

- About the state list

```bash
    terraform state list
```

- The output of the above command:

```bash
    aws_instance.app_server
```

![Command outputs](./screenshots/terraform-aws.png)

## Create Terraform for the Python and Python Apps

- Based on the created apps in the previous labs, I have created a Terraform configuration to deploy a simple Python app.

- Inside the `apps` directory, I have created the terraform configuration files.

```bash
    terraform show
```

```bash
# docker_container.app_javascript:
resource "docker_container" "app_javascript" {
    attach                                      = false
    command                                     = [
        "node",
        "app.js",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = [
        "docker-entrypoint.sh",
    ]
    env                                         = []
    hostname                                    = "f0ad1e1e1e2a"
    id                                          = "f0ad1e1e1e2ab4b826ca0d4f362f279afd5189ab098ec21794019f0df2db301a"
    image                                       = "sha256:edd816dd43f846b1e9022049fdb30a027e8070e9afaa83c307887dd2397facfc"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow_tz_js"
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
    user                                        = "appuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8081
        internal = 3000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_container.app_python:
resource "docker_container" "app_python" {
    attach                                      = false
    command                                     = [
        "python",
        "app.py",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_shares                                  = 0
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "d47911c7d0af"
    id                                          = "d47911c7d0af7bc8395fb76778f956cefacb5a92edb8eeba29ff286103240d17"
    image                                       = "sha256:b4a2fbbba8bfa63e718f5b1c0df4e9297244d9b81f1a935b6a890357d7cbeefb"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "moscow_tz"
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
    user                                        = "appuser"
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app"

    ports {
        external = 8001
        internal = 5000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}

# docker_image.app_javascript:
resource "docker_image" "app_javascript" {
    id           = "sha256:edd816dd43f846b1e9022049fdb30a027e8070e9afaa83c307887dd2397facfcwesamnaseer/mtz_js:latest"
    image_id     = "sha256:edd816dd43f846b1e9022049fdb30a027e8070e9afaa83c307887dd2397facfc"
    keep_locally = true
    name         = "wesamnaseer/mtz_js:latest"
    repo_digest  = "wesamnaseer/mtz_js@sha256:6ef71019982e792b0bf7bfb3d794cbbb2f95ae7e809615ebeeae9755f769ad8c"
}

# docker_image.app_python:
resource "docker_image" "app_python" {
    id           = "sha256:b4a2fbbba8bfa63e718f5b1c0df4e9297244d9b81f1a935b6a890357d7cbeefbwesamnaseer/mtz:v1.0"
    image_id     = "sha256:b4a2fbbba8bfa63e718f5b1c0df4e9297244d9b81f1a935b6a890357d7cbeefb"
    keep_locally = true
    name         = "wesamnaseer/mtz:v1.0"
    repo_digest  = "wesamnaseer/mtz@sha256:7ce56927e24c75d258709f0dedb68436f94f497b00d725d914d77e90a3be655d"
}


Outputs:

js_app_external_port = 8081
js_app_internal_port = 3000
python_app_external_port = 8001
python_app_internal_port = 5000
```

- About the state list

```bash
    terraform state list
```

- The output of the above command:

```bash
    docker_container.app_javascript
    docker_container.app_python
    docker_image.app_javascript
    docker_image.app_python
```

![Command outputs](./screenshots/apps-1.png)

### Verify the Deployed Apps

![Python and JavaScript Apps](./screenshots/apps-2.png)
![Python and JavaScript Apps](./screenshots/apps-3.png)

## Best Practices Followed

1. **Modular Structure**: Configuration files are organized within separate directories for Docker and AWS, improving maintainability and clarity.

2. **Provider Declaration**: Providers are declared explicitly within each main.tf file, ensuring clear dependency management.

3. **Resource Declarations**: Resources are defined appropriately inside the corresponding resources.tf file, enhancing readability and maintainability. Moreover, resources are named meaningfully, ensuring clarity and consistency.

4. **Variable Usage**: Variables are utilized to parameterize configuration, enhancing flexibility and reusability.

5. **Output Usage**: Outputs are defined to expose the results of the infrastructure deployment, ensuring clarity and consistency.

6. **Secrets Management**: Sensitive information is managed securely using environment variables.
