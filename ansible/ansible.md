This document describes the steps to install and configure ansible on a local machine and use it to provision an AWS EC2 instance with Docker and Docker Compose.

# Install Ansible
The following steps are used to install ansible on a local machine:
1- Install python3 and pip3
2- Install ansible using pip3
3- Verify the installation

## Install python3 and pip3
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

## Install ansible using pip3
```bash
pip3 install ansible
```

## Verify the installation
```bash
ansible --version
```

# Configure Ansible
The following steps are used to configure ansible on a local machine:
1- Create a directory for the ansible project
2- Create an inventory file
3- Create a playbook file
4- Install the required roles and collections
5- Create a main playbook file

I installed docker role and aws collection using the following commands:
```bash
ansible-galaxy role install geerlingguy.docker
ansible-galaxy collection install amazon.aws 
```

# Inventory
I created an inventory file named default_aws_ec2.yml. This file is used to define the AWS EC2 instance that will be provisioned.

## Output
By running the command `ansible-inventory -i inventory/default_aws_ec2.yml --list` I got the following output:

```
{
    "_meta": {
        "hostvars": {
            "ec2-54-203-134-149.us-west-2.compute.amazonaws.com": {
                "ami_launch_index": 0,
                "ansible_host": "54.203.134.149",
                "ansible_user": "ubuntu",
                "architecture": "x86_64",
                "block_device_mappings": [
                    {
                        "device_name": "/dev/sda1",
                        "ebs": {
                            "attach_time": "2024-03-05T22:49:21+00:00",
                            "delete_on_termination": true,
                            "status": "attached",
                            "volume_id": "vol-09dad4aafa830d9ef"
                        }
                    }
                ],
                "capacity_reservation_specification": {
                    "capacity_reservation_preference": "open"
                },
                "client_token": "9ef5d099-5d19-4006-948f-ec882f8e26d0",
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
                "instance_id": "i-04471611c4a53a265",
                "instance_type": "t2.micro",
                "key_name": "mosta",
                "launch_time": "2024-03-05T22:49:21+00:00",
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
                            "public_dns_name": "ec2-54-203-134-149.us-west-2.compute.amazonaws.com",
                            "public_ip": "54.203.134.149"
                        },
                        "attachment": {
                            "attach_time": "2024-03-05T22:49:21+00:00",
                            "attachment_id": "eni-attach-0a4bdcd6265348e11",
                            "delete_on_termination": true,
                            "device_index": 0,
                            "network_card_index": 0,
                            "status": "attached"
                        },
                        "description": "",
                        "groups": [
                            {
                                "group_id": "sg-0d123df373261b926",
                                "group_name": "launch-wizard-2"
                            }
                        ],
                        "interface_type": "interface",
                        "ipv6_addresses": [],
                        "mac_address": "02:8e:35:0d:e2:f5",
                        "network_interface_id": "eni-04b809698384cc990",
                        "owner_id": "195079873263",
                        "private_dns_name": "ip-172-31-18-112.us-west-2.compute.internal",
                        "private_ip_address": "172.31.18.112",
                        "private_ip_addresses": [
                            {
                                "association": {
                                    "ip_owner_id": "amazon",
                                    "public_dns_name": "ec2-54-203-134-149.us-west-2.compute.amazonaws.com",
                                    "public_ip": "54.203.134.149"
                                },
                                "primary": true,
                                "private_dns_name": "ip-172-31-18-112.us-west-2.compute.internal",
                                "private_ip_address": "172.31.18.112"
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
                "private_dns_name": "ip-172-31-18-112.us-west-2.compute.internal",
                "private_dns_name_options": {
                    "enable_resource_name_dns_a_record": true,
                    "enable_resource_name_dns_aaaa_record": false,
                    "hostname_type": "ip-name"
                },
                "private_ip_address": "172.31.18.112",
                "product_codes": [],
                "public_dns_name": "ec2-54-203-134-149.us-west-2.compute.amazonaws.com",
                "public_ip_address": "54.203.134.149",
                "requester_id": "",
                "reservation_id": "r-09b348cfc54811643",
                "root_device_name": "/dev/sda1",
                "root_device_type": "ebs",
                "security_groups": [
                    {
                        "group_id": "sg-0d123df373261b926",
                        "group_name": "launch-wizard-2"
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
                    "Name": "mosta"
                },
                "usage_operation": "RunInstances",
                "usage_operation_update_time": "2024-03-05T22:49:21+00:00",
                "virtualization_type": "hvm",
                "vpc_id": "vpc-011c6f37b738e34b8"
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
            "ec2-54-203-134-149.us-west-2.compute.amazonaws.com"
        ]
    }
}
```

# Custom Docker Role
I created a custom role named docker. This role is used to install docker and docker-compose on the AWS EC2 instance. The role is defined in the directory roles/docker.

## Output
By running the command `ansible-playbook playbooks/dev/main.yml --diff` I got the following output:
```
PLAY [Install Docker and Docker Compose] ***************************************

TASK [Gathering Facts] *********************************************************
ok: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

TASK [docker : Update apt packages] ********************************************
changed: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Update docker.io package] *******************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Upgrade python3-pip] ************************************
The following additional packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-wheel python3.10-dev rpcsvc-proto
  zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc
The following NEW packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-pip python3-wheel python3.10-dev
  rpcsvc-proto zlib1g-dev
0 upgraded, 64 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

TASK [docker : Upgrade pip] ****************************************************
changed: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker sdk] *********************************************
changed: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker-compose] *****************************************
changed: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

RUNNING HANDLER [docker : Add ubuntu to the docker group] **********************
changed: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

RUNNING HANDLER [docker : Start docker] ****************************************
changed: [ec2-54-203-134-149.us-west-2.compute.amazonaws.com]

PLAY RECAP *********************************************************************
ec2-54-203-134-149.us-west-2.compute.amazonaws.com : ok=9    changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```