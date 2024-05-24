# Best practices

- Use variables for container name
- Use environment variables for sensitive information such as aws and github keys
- Use terraform fmt and validate

# Docker

## terraform state list
docker_container.python-test-app_python
docker_image.python-test-app_python

## terraform state show docker_container.python-test-app_python

```
# docker_container.python-test-app_python:
resource "docker_container" "python-test-app_python" {
    attach                                      = false
    bridge                                      = [90mnull[0m[0m
    command                                     = [
        "/home/myuser/.local/bin/uvicorn",
        "main:app",
        "--proxy-headers",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    ]
    container_read_refresh_timeout_milliseconds = 15000
    cpu_set                                     = [90mnull[0m[0m
    cpu_shares                                  = 0
    domainname                                  = [90mnull[0m[0m
    entrypoint                                  = []
    env                                         = []
    hostname                                    = "7ff0b9d0eb0f"
    id                                          = "7ff0b9d0eb0f29732b7ab96dcd8492f0678b34908c7d8d47434638c0f293ace3"
    image                                       = "sha256:8c2c365974597bdea6e0cec2481e74af47cdf573b889dcb67541370604acdd16"
    init                                        = false
    ipc_mode                                    = "private"
    log_driver                                  = "json-file"
    logs                                        = false
    max_retry_count                             = 0
    memory                                      = 0
    memory_swap                                 = 0
    must_run                                    = true
    name                                        = "python-test-app_python"
    network_data                                = [
        {
            gateway                   = "172.17.0.1"
            global_ipv6_address       = [90mnull[0m[0m
            global_ipv6_prefix_length = 0
            ip_address                = "172.17.0.2"
            ip_prefix_length          = 16
            ipv6_gateway              = [90mnull[0m[0m
            mac_address               = "02:42:ac:11:00:02"
            network_name              = "bridge"
        },
    ]
    network_mode                                = "bridge"
    pid_mode                                    = [90mnull[0m[0m
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
    stop_signal                                 = [90mnull[0m[0m
    stop_timeout                                = 0
    tty                                         = false
    user                                        = "myuser"
    userns_mode                                 = [90mnull[0m[0m
    wait                                        = false
    wait_timeout                                = 60
    working_dir                                 = "/app_python"

    ports {
        external = 8000
        internal = 8000
        ip       = "0.0.0.0"
        protocol = "tcp"
    }
}
```
# AWS

## terraform state show aws_instance.app_server
```
resource "aws_instance" "app_server" {
    ami                                  = "ami-830c94e3"
    arn                                  = "arn:aws:ec2:us-west-2:767398147144:instance/i-03a3720031fb1f3eb"
    associate_public_ip_address          = true
    availability_zone                    = "us-west-2b"
    cpu_core_count                       = 1
    cpu_threads_per_core                 = 1
    disable_api_stop                     = false
    disable_api_termination              = false
    ebs_optimized                        = false
    get_password_data                    = false
    hibernation                          = false
    host_id                              = [90mnull[0m[0m
    iam_instance_profile                 = [90mnull[0m[0m
    id                                   = "i-03a3720031fb1f3eb"
    instance_initiated_shutdown_behavior = "stop"
    instance_state                       = "running"
    instance_type                        = "t2.micro"
    ipv6_address_count                   = 0
    ipv6_addresses                       = []
    key_name                             = [90mnull[0m[0m
    monitoring                           = false
    outpost_arn                          = [90mnull[0m[0m
    password_data                        = [90mnull[0m[0m
    placement_group                      = [90mnull[0m[0m
    placement_partition_number           = 0
    primary_network_interface_id         = "eni-0413afa117dc9d323"
    private_dns                          = "ip-172-31-30-220.us-west-2.compute.internal"
    private_ip                           = "172.31.30.220"
    public_dns                           = "ec2-35-87-84-98.us-west-2.compute.amazonaws.com"
    public_ip                            = "35.87.84.98"
    secondary_private_ips                = []
    security_groups                      = [
        "default",
    ]
    source_dest_check                    = true
    subnet_id                            = "subnet-0c2829830fd10978f"
    tags                                 = {
        "Name" = "ExampleAppServerInstance"
    }
    tags_all                             = {
        "Name" = "ExampleAppServerInstance"
    }
    tenancy                              = "default"
    user_data_replace_on_change          = false
    vpc_security_group_ids               = [
        "sg-0f3bb3a4c686f99c6",
    ]

    capacity_reservation_specification {
        capacity_reservation_preference = "open"
    }

    cpu_options {
        amd_sev_snp      = [90mnull[0m[0m
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
        kms_key_id            = [90mnull[0m[0m
        tags                  = {}
        throughput            = 0
        volume_id             = "vol-013b621eae5b56190"
        volume_size           = 8
        volume_type           = "standard"
    }
}
```
