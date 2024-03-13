# Ansible lab 5

## I installed ansible, docker role and aws collection using the following commands:
```bash
ansible-galaxy role install geerlingguy.docker
ansible-galaxy collection install amazon.aws 
```

## Inventory details
    ```sh
        $ ansible-inventory inventory/default_aws_ec2.yml --list{
    "_meta": {
        "hostvars": {
            "ec2-3-92-33-42.compute-1.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/xvda",
                        "ebs": {
                            "attach_time": "2024-03-07T00:20:44+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0f8f2680a7976996d"
                        }
                    }
                ],
                "boot_mode": "uefi-preferred",
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "2a78bfd3-ab1c-4362-8e89-d108b6a837a2",
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
                "iam_instance_profile": {
                    "arn": "arn:aws:iam::767398008935:instance-profile/Devops-lab5",
                    "id": "AIPA3FLD4LBTQ35NWC3PT"
                },
                "image_id": "ami-0f403e3180720dd7e",
                "instance_id": "i-0d1c338030fbcfa40",
                "instance_type": "t2.micro",
                "key_name": "a1kuat",
                "launch_time": "2024-03-07T00:20:44+00:00",
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
                            "public_dns_name": "ec2-3-92-33-42.compute-1.amazonaws.com",
                            "public_ip": "3.92.33.42"
                        },
                        "attachment": {
                            "attach_time": "2024-03-07T00:20:44+00:00",
                            "attachment_id": "eni-attach-0518c7dd869e2ac76",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-0b81346f9f0a69f53",
                                "group_name": "launch-wizard-1"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "0e:00:a3:0f:38:69",
                        "network_interface_id": "eni-00007b7559d743953",
                        "owner_id": "767398008935",
                        "private_dns_name": "ip-172-31-44-224.ec2.internal",
                        "private_ip_address": "172.31.44.224",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-3-92-33-42.compute-1.amazonaws.com",
                                    "public_ip": "3.92.33.42"
                                },
                                "primary": true,
                                "private_dns_name": "ip-172-31-44-224.ec2.internal",
                                "private_ip_address": "172.31.44.224"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-059e04d965b5904f3",
                        "vpc_id": "vpc-0cb3535c0d06c3ae8"
                    }
                ],
                "owner_id": "767398008935",
                "placement": {
                    "availability_zone": "us-east-1c",
                    "group_name": "",
                    "region": "us-east-1",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "ip-172-31-44-224.ec2.internal",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": true,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "172.31.44.224",
                "product_codes": [],
                "public_dns_name": "ec2-3-92-33-42.compute-1.amazonaws.com",
                "public_ip_address": "3.92.33.42",
                "requester_id": "",
                "reservation_id": "r-0b1ec0e567b11a695",
                "root_device_name": "/dev/xvda",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-0b81346f9f0a69f53",
                        "group_name": "launch-wizard-1"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-059e04d965b5904f3",
                "tags": {
                    "Name": "Devops"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2024-03-07T00:20:44+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-0cb3535c0d06c3ae8"
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
            "ec2-3-92-33-42.compute-1.amazonaws.com"
        ]
    }
}
    ```

## Playbook output

    ```sh
    $ ansible-playbook playbooks/dev/main.yaml --diff

    PLAY [Deploy Docker] ************************************************************************************************************************************************

    TASK [Gathering Facts] ******************************************************************************************************************************************************************
    ok: [ec2-3-92-33-42.compute-1.amazonaws.com]

    TASK [docker : Apt packages updating] ****************************************************************************************************************************************
    ok: [ec2-3-92-33-42.compute-1.amazonaws.com]

    TASK [docker : Docker.io package updating] *************************************************************************************************************************************************************
    ok: [ec2-3-92-33-42.compute-1.amazonaws.com]

    TASK [docker : Python3-pip upgrading] ****************************************************************************************************************************************************
    ok: [ec2-3-92-33-42.compute-1.amazonaws.com]

    TASK [docker : Pip upgrading] ************************************************************************************************************************************************
    ok: [ec2-3-92-33-42.compute-1.amazonaws.com]

    TASK [docker : Docker sdk installing] **********************************************************************************************************************************************************
    ok: [ec2-3-92-33-42.compute-1.amazonaws.com]

    TASK [docker : Docker-compose installing] **************************************************************************************************************************************************
    ok: [ec2-3-92-33-42.compute-1.amazonaws.com]

    PLAY RECAP ******************************************************************************************************************************************************************************
    ec2-3-92-33-42.compute-1.amazonaws.com : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ```

## Best practices
- Named all tasks
- Used `ansible.cfg` for configurations especially for private key file path
- Structured as given template

# Lab 6


## Playbook output for Python web application
    ```sh
    $ ansible-playbook playbooks/dev/app_python/main.yml 

    PLAY [Deploy Python Application] ************************************************************************************************************************************************************************************************

    TASK [Gathering Facts] **********************************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Apt packages updating] *******************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Docker.io package updating] **************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Python3-pip upgrading] *******************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Upgrade pip] *****************************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Install docker sdk] **********************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Install docker-compose] ******************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker compose file existence] *******************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker container stop] ***************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker images remove] ****************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Compose file remove] *****************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Create directory] ********************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Copy template] ***********************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Stop containers] *********************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Run docker-compose] ******************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    PLAY RECAP **********************************************************************************************************************************************************************************************************************
    ec2-18-209-66-201.compute-1.amazonaws.com : ok=15   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ```

## Playbook output for Typescript web application
    ```sh
    $ ansible-playbook playbooks/dev/app_typescript/main.yml 

    PLAY [Deploy Python Application] ************************************************************************************************************************************************************************************************

    TASK [Gathering Facts] **********************************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Apt packages updating] *******************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Docker.io package updating] **************************************************************************************************************************************************************************************
    ^C [ERROR]: User interrupted execution
    (base) azamat@Aza:~/Documents/DevOps/S24-core-course-labs/ansible$ ansible-playbook playbooks/dev/app_typescript/main.yml 

    PLAY [Deploy Typescript Application] ********************************************************************************************************************************************************************************************

    TASK [Gathering Facts] **********************************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Apt packages updating] *******************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Docker.io package updating] **************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Python3-pip upgrading] *******************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Upgrade pip] *****************************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Install docker sdk] **********************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [docker : Install docker-compose] ******************************************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker compose file existence] *******************************************************************************************************************************************************************
    ok: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker container stop] ***************************************************************************************************************************************************************************
    skipping: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker images remove] ****************************************************************************************************************************************************************************
    skipping: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Compose file remove] *****************************************************************************************************************************************************************************
    skipping: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Create directory] ********************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Copy template] ***********************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Stop containers] *********************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Run docker-compose] ******************************************************************************************************************************************************************************
    changed: [ec2-18-209-66-201.compute-1.amazonaws.com]

    PLAY RECAP **********************************************************************************************************************************************************************************************************************
    ec2-18-209-66-201.compute-1.amazonaws.com : ok=12   changed=4    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
    ```
## Docker status on aws machine:

```sh
$ sudo docker ps

CONTAINER ID   IMAGE                             COMMAND                  CREATED              STATUS              PORTS                                                 NAMES
9835819af48a   a1kuat/my-typescript-app:latest   "docker-entrypoint.s…"   About a minute ago   Up About a minute   3000/tcp, 0.0.0.0:5001->5001/tcp, :::5001->5001/tcp   my-typescript-app_web_1
05eac2696c0a   a1kuat/my-python-app:latest       "python app.py"          4 minutes ago        Up 4 minutes        0.0.0.0:5000->5000/tcp, :::5000->5000/tcp             my-python-app_web_1

```