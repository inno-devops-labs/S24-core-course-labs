**Output of `ansible-playbook playbooks/dev/main.yaml` deploying docker**

```
PLAY [Install Docker on Ubuntu] *************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************
ok: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Update apt package cache] ****************************************************************************************************************
changed: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Install pip3] ****************************************************************************************************************************
changed: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Install Python3] *************************************************************************************************************************
ok: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Update apt package cache] ****************************************************************************************************************
changed: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Install dependencies for Docker] *********************************************************************************************************
ok: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Add Docker GPG key] **********************************************************************************************************************
changed: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Add Docker Repository] *******************************************************************************************************************
changed: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Update apt package cache (again with Docker repository)] *********************************************************************************
changed: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Install Docker] **************************************************************************************************************************
changed: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Start and enable Docker service] *********************************************************************************************************
ok: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

TASK [docker : Install Docker Compose using pip] ********************************************************************************************************
changed: [ec2-13-51-56-99.eu-north-1.compute.amazonaws.com]

PLAY RECAP **********************************************************************************************************************************************
ec2-13-51-56-99.eu-north-1.compute.amazonaws.com : ok=12   changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

**Output of `ansible-inventory -i default_aws_ec2.yml --list`**

```json
{
    "_meta": {
        "hostvars": {
            "ec2-13-51-56-99.eu-north-1.compute.amazonaws.com": {
                "ansible_ssh_private_key_file": "~/.ssh/aws",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "aws"
        ]
    },
    "aws": {
        "hosts": [
            "ec2-13-51-56-99.eu-north-1.compute.amazonaws.com"
        ]
    }
}
```

## Bonus task: 
Output of the `ansible % ansible-inventory -i inventory/dynamic.aws_ec2.yml --list` after adding dynamic inventory file 
```
{
    "_meta": {
        "hostvars": {
            "ec2-13-51-109-30.eu-north-1.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2024-03-03T12:25:01+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0b0670e65bc43c200"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "terraform-20240303122500116400000001",
                "cpu_options": {
                    "core_count": 1,
                    "threads_per_core": 2
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
                "image_id": "ami-00381a880aa48c6c6",
                "instance_id": "i-094d04dab698ac8f9",
                "instance_type": "t3.micro",
                "key_name": "aws",
                "launch_time": "2024-03-03T12:25:01+00:00",
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
                            "public_dns_name": "ec2-13-51-109-30.eu-north-1.compute.amazonaws.com",
                            "public_ip": "13.51.109.30"
                        },
                        "attachment": {
                            "attach_time": "2024-03-03T12:25:01+00:00",
                            "attachment_id": "eni-attach-038f974c1b560db20",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-07f5fa85c60d33ef3",
                                "group_name": "sg_ec2"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "0a:b7:34:1d:36:5f",
                        "network_interface_id": "eni-03f19a496320e7d43",
                        "owner_id": "637423257153",
                        "private_dns_name": "ip-172-31-40-153.eu-north-1.compute.internal",
                        "private_ip_address": "172.31.40.153",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-13-51-109-30.eu-north-1.compute.amazonaws.com",
                                    "public_ip": "13.51.109.30"
                                },
                                "primary": true,
                                "private_dns_name": "ip-172-31-40-153.eu-north-1.compute.internal",
                                "private_ip_address": "172.31.40.153"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-00b8bf81095562afa",
                        "vpc_id": "vpc-0e3f78e948c10d6de"
                    }
                ],
                "owner_id": "637423257153",
                "placement": {
                    "availability_zone": "eu-north-1b",
                    "group_name": "",
                    "region": "eu-north-1",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "ip-172-31-40-153.eu-north-1.compute.internal",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": false,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "172.31.40.153",
                "product_codes": [],
                "public_dns_name": "ec2-13-51-109-30.eu-north-1.compute.amazonaws.com",
                "public_ip_address": "13.51.109.30",
                "requester_id": "",
                "reservation_id": "r-092e0540f4ea64062",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-07f5fa85c60d33ef3",
                        "group_name": "sg_ec2"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-00b8bf81095562afa",
                "tags": {
                    "Name": "DevOps-S24"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2024-03-03T12:25:01+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-0e3f78e948c10d6de"
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
            "ec2-13-51-109-30.eu-north-1.compute.amazonaws.com"
        ]
    }
}
```


And here is the output of `ansible-inventory -i inventory/default_aws_ec2.yml --list`

```
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped",
            "aws"
        ]
    },
    "aws": {
        "children": [
            "aws_ec2"
        ]
    }
}
```