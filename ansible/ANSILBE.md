# Ansible

### Inventory details
```sh 
 ansible-inventory inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "ec2-3-17-174-129.us-east-2.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/xvda",
                        "ebs": {
                            "attach_time": "2024-03-10T14:42:57+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-0a1cc765c65c9735b"
                        }
                    }
                ],
                "boot_mode": "uefi-preferred",
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "78de5dde-3b3f-4576-9714-4db8c8fe599a",
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
                "image_id": "ami-022661f8a4a1b91cf",
                "instance_id": "i-0abd3f24080f1a506",
                "instance_type": "t2.micro",
                "key_name": "ikram",
                "launch_time": "2024-03-10T14:42:56+00:00",
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
                            "public_dns_name": "ec2-3-17-174-129.us-east-2.compute.amazonaws.com",
                            "public_ip": "3.17.174.129"
                        },
                        "attachment": {
                            "attach_time": "2024-03-10T14:42:56+00:00",
                            "attachment_id": "eni-attach-0fc93a616089bdf09",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-0553b3b7458e098cb",
                                "group_name": "launch-wizard-1"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "02:de:a6:08:e2:1f",
                        "network_interface_id": "eni-0b87ce939e05539d7",
                        "owner_id": "767398008935",
                        "private_dns_name": "ip-172-31-7-110.us-east-2.compute.internal",
                        "private_ip_address": "172.31.7.110",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-3-17-174-129.us-east-2.compute.amazonaws.com",
                                    "public_ip": "3.17.174.129"
                                },
                                "primary": true,
                                "private_dns_name": "ip-172-31-7-110.us-east-2.compute.internal",
                                "private_ip_address": "172.31.7.110"
                            }
                        ],
                        "source_dest_check": true,
                        "status": "in-use",
                        "subnet_id": "subnet-0d680a79342990751",
                        "vpc_id": "vpc-09d108dfb025c5eae"
                    }
                ],
                "owner_id": "767398008935",
                "placement": {
                    "availability_zone": "us-east-2a",
                    "group_name": "",
                    "region": "us-east-2",
                    "tenancy": "default"
                },
                "platform_details": "Linux/UNIX",
                "private_dns_name": "ip-172-31-7-110.us-east-2.compute.internal",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": true,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "172.31.7.110",
                "product_codes": [],
                "public_dns_name": "ec2-3-17-174-129.us-east-2.compute.amazonaws.com",
                "public_ip_address": "3.17.174.129",
                "requester_id": "",
                "reservation_id": "r-07064a8051ebe9e8b",
                "root_device_name": "/dev/xvda",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-0553b3b7458e098cb",
                        "group_name": "launch-wizard-1"
                    }
                ],
                "source_dest_check": true,
                "state": {
                    "code": 16,
                    "name": "running"
                },
                "state_transition_reason": "",
                "subnet_id": "subnet-0d680a79342990751",
                "tags": {
                    "Name": "IkramServer"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2024-03-10T14:42:56+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-09d108dfb025c5eae"
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
            "ec2-3-17-174-129.us-east-2.compute.amazonaws.com"
        ]
    }
}
```

## Playbook output

    ```sh
    $ ansible-playbook playbooks/dev/main.yaml --diff

    PLAY [Docker Deployment] ************************************************************************************************************************************************

    TASK [Gathering Facts] ******************************************************************************************************************************************************************
    ok: [ec2-3-17-174-129.us-east-2.compute.amazonaws.com]

    TASK [docker : Update apt packages] ****************************************************************************************************************************************
    ok: [ec2-3-17-174-129.us-east-2.compute.amazonaws.com]

    TASK [docker : Update Docker.io package] *************************************************************************************************************************************************************
    ok: [ec2-3-17-174-129.us-east-2.compute.amazonaws.com]

    TASK [docker : Upgrade Python3-pip] ****************************************************************************************************************************************************
    ok: [ec2-3-17-174-129.us-east-2.compute.amazonaws.com]

    TASK [docker : pip upgrade] ************************************************************************************************************************************************
    ok: [ec2-3-17-174-129.us-east-2.compute.amazonaws.com]

    TASK [docker : docker sdk install] **********************************************************************************************************************************************************
    ok: [ec2-3-17-174-129.us-east-2.compute.amazonaws.com]

    TASK [docker : docker-compose install] **************************************************************************************************************************************************
    ok: [ec2-3-17-174-129.us-east-2.compute.amazonaws.com]

    PLAY RECAP ******************************************************************************************************************************************************************************
    ec2-3-17-174-129.us-east-2.compute.amazonaws.com : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ```

## Optimal Approaches
- Assigned names to all tasks
- Employed ansible.cfg for configurations, particularly for specifying the private key file path
- Organized according to the provided template

### Playbook output for python app
```sh
    $ ansible-playbook playbooks/dev/app_python/main.yml 

    PLAY [Deploy Python Application] ************************************************************************************************************************************************************************************************

    TASK [Gathering Facts] **********************************************************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [docker : Update apt packages] *********************************************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [docker : Update Docker.io package] ****************************************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [docker : Upgrade Python3-pip] *********************************************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [docker : pip upgrade] *****************************************************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [docker : docker sdk install] **********************************************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [docker : docker-compose install] ******************************************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker compose file existence] *******************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker container stop] ***************************************************************************************************************************************************************************
    changed: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Docker images remove] ****************************************************************************************************************************************************************************
    changed: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Compose file remove] *****************************************************************************************************************************************************************************
    changed: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Create directory] ********************************************************************************************************************************************************************************
    ok: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Copy template] ***********************************************************************************************************************************************************************************
    changed: [ec2-44-222-224-117.compute-1.amazonaws.com]
    
    TASK [../../../roles/web_app : Stop containers] *********************************************************************************************************************************************************************************
    changed: [ec2-44-222-224-117.compute-1.amazonaws.com]

    TASK [../../../roles/web_app : Run docker-compose] ******************************************************************************************************************************************************************************
    changed: [ec2-44-222-224-117.compute-1.amazonaws.com]

    PLAY RECAP **********************************************************************************************************************************************************************************************************************
    ec2-44-222-224-117.compute-1.amazonaws.com : ok=15   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
## Output of docker status on ubuntu aws instance:
```sh
    ubuntu@ip-172-31-23-179:~$ sudo docker ps
    CONTAINER ID   IMAGE                       COMMAND                  CREATED          STATUS          PORTS                                                 NAMES
    f5c08dc07f7f   itoqsky/python-app:latest   "flask run --host=0.…"   52 seconds ago   Up 51 seconds   5555/tcp, 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   python-app_web_1
```
    