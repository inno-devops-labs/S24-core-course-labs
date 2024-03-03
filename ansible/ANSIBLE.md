# Ansible

## Table of Contents

- [Ansible](#ansible)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Inventory](#inventory)
    - [Output](#output)
  - [Using imported docker role](#using-imported-docker-role)
  - [Custom Docker Role](#custom-docker-role)
    - [Output (Custom)](#output-custom)
  - [Best Practices](#best-practices)

## Prerequisites

For this assingment, I needed two AWS EC2 instances running that could be accessed using SSH. I also needed to have `ansible` installed on my local machine.

For quick setup, I modified my terraform script to create two `t2.micro` instances in the `eu-central-1` region. The servers are tagged as `server-python` and `server-bun` respectively. I also added the following security group rules to allow SSH access from my IP address and HTTP access from anywhere. The changes can be found [here](../terraform/aws.tf).

## Installation

I had to install `docker` role and `aws` collection from `ansible-galaxy` using the following commands:

```bash
ansible-galaxy role install geerlingguy.docker
ansible-galaxy collection install amazon.aws
```

Apart from that, I needed to install `boto3` and `botocore` using the following command as a dependency for the `amazon.aws` collection:

```bash
pip install boto3 botocore
```

For `ansible.cfg`, I used the following configuration:

```ini
inventory=./inventory
roles_path=./roles
host_key_checking=False
```

The first two were to specify the directory for the inventory and roles. The `host_key_checking` was set to `False` to avoid the prompt for adding the host to the `known_hosts` file.

## Inventory

I used dynamic inventory to fetch the EC2 instances from AWS. I created a file `default_aws_ec2.yml` in the `invetory` directory and looked for `server-python` and `server-bun` tags to fetch the instances. The `ansible-user` was set to `ubuntu` as a compose key-value. `compose` was also instructed to use the IP address of the instances.

### Output

Running `ansible-inventory -i inventory/default_aws_ec2.yml --graph` gives me the following output:

```json
{
    "_meta": {
        "hostvars": {
            "ec2-3-64-148-254.eu-central-1.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "ansible_host": "3.64.148.254",
                "ansible_user": "ubuntu",
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2024-02-29T21:55:45+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-00e79db5bb149e82b"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "terraform-20240229215544503000000001",
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
                "image_id": "ami-0faab6bdbac9486fb",
                "instance_id": "i-03c4493be7d3daf93",
                "instance_type": "t2.micro",
                "key_name": "deployer",
                "launch_time": "2024-02-29T21:55:45+00:00",
                "maintenance_options": {
                    "auto_recovery": "default"
                },
                "metadata_options": {
                    "http_endpoint": "enabled",
                    "http_protocol_ipv6": "disabled",
                    "http_put_response_hop_limit": 1,
                    "http_tokens": "optional",
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
                            "public_dns_name": "ec2-3-64-148-254.eu-central-1.compute.amazonaws.com",
                            "public_ip": "3.64.148.254"
                        },
                        "attachment": {
                            "attach_time": "2024-02-29T21:55:45+00:00",
                            "attachment_id": "eni-attach-0e2ca59c051a5a310",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-0130789c057cc9586",
                                "group_name": "allow_ssh_http"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "02:ad:e5:c2:32:bd",
                        "network_interface_id": "eni-0d582b8f5a685681f",
                        "owner_id": "338171648102",
                        "private_dns_name": "ip-172-31-29-237.eu-central-1.compute.internal",
                        "private_ip_address": "172.31.29.237",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-3-64-148-254.eu-central-1.compute.amazonaws.com",
                                    "public_ip": "3.64.148.254"
                                },
                                "primary": true,
                                "private_dns_name": "ip-172-31-29-237.eu-central-1.compute.internal",
                                "private_ip_address": "172.31.29.237"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-0ebf661e4a4cf59ff",
                        "vpc_id": "vpc-0f6744c21f9f1a7a1"
                    }
                ],
                "owner_id": "338171648102",
                "placement": {
                    "availability_zone": "eu-central-1a",
                    "group_name": "",
                    "region": "eu-central-1",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "ip-172-31-29-237.eu-central-1.compute.internal",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": false,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "172.31.29.237",
                "product_codes": [],
                "public_dns_name": "ec2-3-64-148-254.eu-central-1.compute.amazonaws.com",
                "public_ip_address": "3.64.148.254",
                "requester_id": "",
                "reservation_id": "r-02e857142a8d74edf",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-0130789c057cc9586",
                        "group_name": "allow_ssh_http"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-0ebf661e4a4cf59ff",
                "tags": {
                    "Name": "server-bun"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2024-02-29T21:55:45+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-0f6744c21f9f1a7a1"
            },
            "ec2-3-64-217-245.eu-central-1.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "ansible_host": "3.64.217.245",
                "ansible_user": "ubuntu",
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2024-02-29T21:55:46+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0c8ff6526084657cc"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "terraform-20240229215544503600000002",
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
                "image_id": "ami-0faab6bdbac9486fb",
                "instance_id": "i-0e7860d3afde02f0d",
                "instance_type": "t2.micro",
                "key_name": "deployer",
                "launch_time": "2024-02-29T21:55:45+00:00",
                "maintenance_options": {
                    "auto_recovery": "default"
                },
                "metadata_options": {
                    "http_endpoint": "enabled",
                    "http_protocol_ipv6": "disabled",
                    "http_put_response_hop_limit": 1,
                    "http_tokens": "optional",
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
                            "public_dns_name": "ec2-3-64-217-245.eu-central-1.compute.amazonaws.com",
                            "public_ip": "3.64.217.245"
                        },
                        "attachment": {
                            "attach_time": "2024-02-29T21:55:45+00:00",
                            "attachment_id": "eni-attach-060393b31acf372df",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-0130789c057cc9586",
                                "group_name": "allow_ssh_http"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "02:a1:ad:7a:ca:61",
                        "network_interface_id": "eni-0fe596ed77bfe4cda",
                        "owner_id": "338171648102",
                        "private_dns_name": "ip-172-31-20-68.eu-central-1.compute.internal",
                        "private_ip_address": "172.31.20.68",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-3-64-217-245.eu-central-1.compute.amazonaws.com",
                                    "public_ip": "3.64.217.245"
                                },
                                "primary": true,
                                "private_dns_name": "ip-172-31-20-68.eu-central-1.compute.internal",
                                "private_ip_address": "172.31.20.68"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-0ebf661e4a4cf59ff",
                        "vpc_id": "vpc-0f6744c21f9f1a7a1"
                    }
                ],
                "owner_id": "338171648102",
                "placement": {
                    "availability_zone": "eu-central-1a",
                    "group_name": "",
                    "region": "eu-central-1",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "ip-172-31-20-68.eu-central-1.compute.internal",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": false,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "172.31.20.68",
                "product_codes": [],
                "public_dns_name": "ec2-3-64-217-245.eu-central-1.compute.amazonaws.com",
                "public_ip_address": "3.64.217.245",
                "requester_id": "",
                "reservation_id": "r-0855059230bc82701",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-0130789c057cc9586",
                        "group_name": "allow_ssh_http"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-0ebf661e4a4cf59ff",
                "tags": {
                    "Name": "server-python"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2024-02-29T21:55:45+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-0f6744c21f9f1a7a1"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "aws_ec2"
        ]
    },
    "aws_ec2": {
        "hosts": [
            "ec2-3-64-148-254.eu-central-1.compute.amazonaws.com",
            "ec2-3-64-217-245.eu-central-1.compute.amazonaws.com"
        ]
    }
}
```

Here, we have 2 hosts under the `aws_ec2` group. Inside `_meta`, we have the details of each hosts. For example, `hostvars` key have variables related to ansible. The `ansible_host` is the IP address of the instance and `ansible_user` is the user to be used for SSH. Then, we can find AWS related information like `instance_id`, `image_id`, `public_dns_name`, `public_ip_address`, etc. The `"client_token": "terraform-20240229215544503000000001"` shows us that the instance was created using terraform. Similarly, we can have other information like `cpu_options`, `network_interfaces`, `security_groups`, etc provided by AWS.

## Using imported docker role

I used the `geerlingguy.docker` role to install `docker` and `docker-compose` on the EC2 instances. The role is already available in the `roles` directory. I also created a playbook `main.yml` in the `playbooks/dev` directory to use the role. The playbook looks like this:

```yaml
- name: Install Docker and Docker Compose
  hosts: aws_ec2
  roles:
    - { role: geerlingguy.docker, tags: docker, become: true }
```

## Custom Docker Role

I created a custom role `docker` to install `docker` and `docker-compose` on the EC2 instances. The role is available in the `roles` directory. The tasks install/upgrade `docker` (docker.io) and `docker-compose` (using pip) and add the `ubuntu` user to the `docker` group. The `docker` service is also (re)started.

Tasks were used for installation and handlers were used for restarting the `docker` service and adding the `ubuntu` user to the `docker` group.

The playbook `main.yml` in the `playbooks/dev` directory to use the role looks like this:

```yaml
- name: Install Docker and Docker Compose
  hosts: aws_ec2
  roles:
    - role: docker
      become: true
```

### Output (Custom)

Running `ansible-playbook playbooks/dev/main.yml --diff` gives me the following output:

```ansible

PLAY [Install Docker and Docker Compose] **************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************
ok: [ec2-3-64-148-254.eu-central-1.compute.amazonaws.com]
ok: [ec2-3-64-217-245.eu-central-1.compute.amazonaws.com]

TASK [docker : Update apt packages] *******************************************************************************************************************************************************************************
ok: [ec2-3-64-148-254.eu-central-1.compute.amazonaws.com]
ok: [ec2-3-64-217-245.eu-central-1.compute.amazonaws.com]

TASK [docker : Remove old versions of Docker] *********************************************************************************************************************************************************************
ok: [ec2-3-64-148-254.eu-central-1.compute.amazonaws.com]
ok: [ec2-3-64-217-245.eu-central-1.compute.amazonaws.com]

TASK [docker : Install Docker using docker.io] ********************************************************************************************************************************************************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 78 not upgraded.
changed: [ec2-3-64-148-254.eu-central-1.compute.amazonaws.com]
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 78 not upgraded.
changed: [ec2-3-64-217-245.eu-central-1.compute.amazonaws.com]

TASK [docker : Install docker-compose] ****************************************************************************************************************************************************************************
changed: [ec2-3-64-217-245.eu-central-1.compute.amazonaws.com]
changed: [ec2-3-64-148-254.eu-central-1.compute.amazonaws.com]

RUNNING HANDLER [docker : Add ubuntu to the docker group] *********************************************************************************************************************************************************
changed: [ec2-3-64-148-254.eu-central-1.compute.amazonaws.com]
changed: [ec2-3-64-217-245.eu-central-1.compute.amazonaws.com]

RUNNING HANDLER [docker : Start docker] ***************************************************************************************************************************************************************************
changed: [ec2-3-64-217-245.eu-central-1.compute.amazonaws.com]
changed: [ec2-3-64-148-254.eu-central-1.compute.amazonaws.com]

PLAY RECAP ********************************************************************************************************************************************************************************************************
ec2-3-64-148-254.eu-central-1.compute.amazonaws.com : ok=7    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ec2-3-64-217-245.eu-central-1.compute.amazonaws.com : ok=7    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## Best Practices

- A proper folder structure was used to organize the files.
- `ansible.cfg` was used for global settings.
- `ansible-galaxy init` was used to create the role with the correct directory structure.
- Virtual environment was maintained
- `--syntax-check` was used before running the playbook to check for syntax errors.
- Dynamic inventory to fetch the EC2 instances from AWS. This way, I don't have to manually add the hosts to the inventory file.
- `ansible-lint` was used to check for best practices.
