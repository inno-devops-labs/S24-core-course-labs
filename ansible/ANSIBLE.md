# Ansible Documentation

This document describes the Ansible setup and usage for deploying Docker.

## Setup

- The Ansible setup includes a dynamic inventory for AWS EC2 instances and a Docker role.

```sh
$ pip install ansible
```

- Then I had to install the docker and aws roles.

```sh
$ ansible-galaxy role install geerlingguy.docker
$ ansible-galaxy collection install amazon.aws
```

- The `ansible.cfg` file is used to configure the default settings for Ansible.

```sh
[defaults]
inventory = ./inventory
remote_user = ubuntu
private_key_file = ~/.ssh/devops-key.pem
host_key_checking = False
```

- Since I am using WSL, I had to export the `ANSIBLE_CONFIG` environment variable.

```sh
$ export ANSIBLE_INVENTORY=./inventory
$ export ANSIBLE_PRIVATE_KEY_FILE=~/.ssh/devops-key.pem
$ export ANSIBLE_HOST_KEY_CHECKING=False
```

- Then I faced an issue with parsing the inventory file. I had to install the `boto` package.

```sh
$ pip install boto3 botocore
```

- Then I exported the AWS credentials. Create a new profile in the `~/.aws/credentials` file.

```sh
$ export AWS_PROFILES=devops-key
```

## Usage

### Deployment: Output

```sh
ansible-playbook playbooks/dev/main.yaml --diff
```

**Please note: I have re run the playbook to show the output.**

```sh
PLAY [Install Docker and Docker Compose] *************************************************************

TASK [Gathering Facts] *******************************************************************************
ok: [ec2-54-201-47-114.us-west-2.compute.amazonaws.com]

TASK [docker : Update apt packages] ******************************************************************
ok: [ec2-54-201-47-114.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Update docker.io package] *****************************************************
ok: [ec2-54-201-47-114.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Upgrade python3-pip] **********************************************************
ok: [ec2-54-201-47-114.us-west-2.compute.amazonaws.com]

TASK [docker : Upgrade pip] **************************************************************************
ok: [ec2-54-201-47-114.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker sdk] *******************************************************************
ok: [ec2-54-201-47-114.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker-compose] ***************************************************************
ok: [ec2-54-201-47-114.us-west-2.compute.amazonaws.com]

PLAY RECAP *******************************************************************************************
ec2-54-201-47-114.us-west-2.compute.amazonaws.com : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Inventory: Output

```sh
ansible-inventory inventory/default_aws_ec2.yml --list
```

```json
{
  "_meta": {
    "hostvars": {
      "ec2-54-201-47-114.us-west-2.compute.amazonaws.com": {
        "ami_launch_index": 0,
        "ansible_host": "54.201.47.114",
        "ansible_user": "ubuntu",
        "architecture": "x86_64",
        "block_device_mappings": [
          {
            "device_name": "/dev/sda1",
            "ebs": {
              "attach_time": "2024-03-05T21:37:47+00:00",
              "delete_on_termination": true,
              "status": "attached",
              "volume_id": "vol-03ad2e6e28dff04d7"
            }
          }
        ],
        "capacity_reservation_specification": {
          "capacity_reservation_preference": "open"
        },
        "client_token": "983d57ee-f7e9-4445-b92d-780e1c9b7097",
        "cpu_options": {
          "core_count": 1,
          "threads_per_core": 1
        },
        "current_instance_boot_mode": "legacy-bios",
        "ebs_optimized": false,
        "ena_support": true,
        "enclave_options": {
          "enabled": false
        },
        "hibernation_options": {
          "configured": false
        },
        "hypervisor": "xen",
        "image_id": "ami-08f7912c15ca96832",
        "instance_id": "i-0619e188f04c61998",
        "instance_type": "t2.micro",
        "key_name": "devops-key",
        "launch_time": "2024-03-05T21:37:47+00:00",
        "maintenance_options": {
          "auto_recovery": "default"
        },
        "metadata_options": {
          "http_endpoint": "enabled",
          "http_protocol_ipv6": "disabled",
          "http_put_response_hop_limit": 2,
          "http_tokens": "required",
          "instance_metadata_tags": "disabled",
          "state": "applied"
        },
        "monitoring": {
          "state": "disabled"
        },
        "network_interfaces": [
          {
            "association": {
              "ip_owner_id": "amazon",
              "public_dns_name": "ec2-54-201-47-114.us-west-2.compute.amazonaws.com",
              "public_ip": "54.201.47.114"
            },
            "attachment": {
              "attach_time": "2024-03-05T21:37:47+00:00",
              "attachment_id": "eni-attach-019c0487a45d4bd1f",
              "delete_on_termination": true,
              "device_index": 0,
              "network_card_index": 0,
              "status": "attached"
            },
            "description": "",
            "groups": [
              {
                "group_id": "sg-02567754d7d2568c2",
                "group_name": "launch-wizard-1"
              }
            ],
            "interface_type": "interface",
            "ipv6_addresses": [],
            "mac_address": "02:ac:0d:59:a9:c5",
            "network_interface_id": "eni-064a5563539f29742",
            "owner_id": "195079873263",
            "private_dns_name": "ip-172-31-24-135.us-west-2.compute.internal",
            "private_ip_address": "172.31.24.135",
            "private_ip_addresses": [
              {
                "association": {
                  "ip_owner_id": "amazon",
                  "public_dns_name": "ec2-54-201-47-114.us-west-2.compute.amazonaws.com",
                  "public_ip": "54.201.47.114"
                },
                "primary": true,
                "private_dns_name": "ip-172-31-24-135.us-west-2.compute.internal",
                "private_ip_address": "172.31.24.135"
              }
            ],
            "source_dest_check": true,
            "status": "in-use",
            "subnet_id": "subnet-09cfe4f959ea1bac6",
            "vpc_id": "vpc-011c6f37b738e34b8"
          }
        ],
        "owner_id": "195079873263",
        "placement": {
          "availability_zone": "us-west-2b",
          "group_name": "",
          "region": "us-west-2",
          "tenancy": "default"
        },
        "platform_details": "Linux/UNIX",
        "private_dns_name": "ip-172-31-24-135.us-west-2.compute.internal",
        "private_dns_name_options": {
          "enable_resource_name_dns_a_record": true,
          "enable_resource_name_dns_aaaa_record": false,
          "hostname_type": "ip-name"
        },
        "private_ip_address": "172.31.24.135",
        "product_codes": [],
        "public_dns_name": "ec2-54-201-47-114.us-west-2.compute.amazonaws.com",
        "public_ip_address": "54.201.47.114",
        "requester_id": "",
        "reservation_id": "r-0f49c25ffb4c6fcb9",
        "root_device_name": "/dev/sda1",
        "root_device_type": "ebs",
        "security_groups": [
          {
            "group_id": "sg-02567754d7d2568c2",
            "group_name": "launch-wizard-1"
          }
        ],
        "source_dest_check": true,
        "state": {
          "code": 16,
          "name": "running"
        },
        "state_transition_reason": "",
        "subnet_id": "subnet-09cfe4f959ea1bac6",
        "tags": {
          "Name": "javascript_timezon_app"
        },
        "usage_operation": "RunInstances",
        "usage_operation_update_time": "2024-03-05T21:37:47+00:00",
        "virtualization_type": "hvm",
        "vpc_id": "vpc-011c6f37b738e34b8"
      }
    }
  },
  "all": {
    "children": ["ungrouped", "aws_ec2"]
  },
  "aws_ec2": {
    "hosts": ["ec2-54-201-47-114.us-west-2.compute.amazonaws.com"]
  }
}
```

## Best Practices

- The Ansible playbook is idempotent and can be run multiple times without any issues.
- The playbook is well documented and easy to understand.
- The playbook is modular and can be reused for other projects.
- Dynamic inventory is used to fetch the EC2 instances from AWS.
