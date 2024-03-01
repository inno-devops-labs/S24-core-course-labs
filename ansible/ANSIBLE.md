# Ansible Playbook Documentation

## Overview

This document provides an overview of the Ansible playbook and associated roles used in the project. It includes details
about the project structure, inventory, playbooks, roles, and how to run the playbook.

## Inventory

Inventory contains ips of remote Vms. It is quite simple, as I deployed only on 1 VM

## Ansible.cfg

Configuration file for ansible. It contain some important meta data, for example ssh private key and directory paths

## Playbooks

The playbooks directory contains the main Ansible playbook(s) used in the project.

## Roles

The roles directory contains reusable Ansible roles that define tasks, variables, templates, and other resources needed
to configure a specific component or service.

## Best practices applied

### Role-based Structure:

The playbook organizes tasks related to Docker into a separate Ansible role named docker, following a modular and
reusable structure.

### Use of Modules:

Ansible modules like `apt`, `apt_key`, `apt_repository`, `pip`, and command are used to perform specific tasks, ensuring
idempotent and platform-independent execution.
Parameterization:

The playbook parameterizes package names and states where applicable, making it easier to adapt to different operating
systems and package versions.

### Task Naming:

Tasks are named descriptively, providing clear indications of their purpose and making the playbook more readable and
understandable.

### Separation of Concerns:

Tasks are logically grouped within the tasks directory of the docker role, maintaining a separation of concerns and
improving code organization.

## Process:

- use terraform to create vm with ssh keys
- test that I can remotely connect to vm using `ssh "private key path" "username"@"ip"`
- define `inventory` and `ansible.cfg` files
- copy `ansible/roles/docker/defaults/main.yml` and `ansible/roles/docker/handlers/main.yml` from the template
- implement tasks in `docker` role
- reference them in `ansible/playbooks/dev/main.yaml` file
- execute playbook using `ansible-playbook playbooks/dev/main.yaml`
- check that VM acquired docker, pip and docker-compose

## Output

```
***

TASK [../../roles/docker : Install pip] **************************************************************************************************************************************************************
included: /home/djovi/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/install_pip.yml for 158.160.26.69

TASK [../../roles/docker : Update apt] ***************************************************************************************************************************************************************
changed: [158.160.26.69]

TASK [../../roles/docker : Install python] ***********************************************************************************************************************************************************
ok: [158.160.26.69]

TASK [../../roles/docker : Install pip] **************************************************************************************************************************************************************
ok: [158.160.26.69]

TASK [../../roles/docker : Install docker deps] ******************************************************************************************************************************************************
included: /home/djovi/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker_dependencies.yml
for 158.160.26.69

TASK [../../roles/docker : Install Docker dependencies] **********************************************************************************************************************************************
ok: [158.160.26.69] => (item=apt-transport-https)
ok: [158.160.26.69] => (item=ca-certificates)
ok: [158.160.26.69] => (item=curl)
ok: [158.160.26.69] => (item=gnupg-agent)
ok: [158.160.26.69] => (item=software-properties-common)

TASK [../../roles/docker : Add Docker GPG key] *******************************************************************************************************************************************************
ok: [158.160.26.69]

TASK [../../roles/docker : Install docker] ***********************************************************************************************************************************************************
included: /home/djovi/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for
158.160.26.69

TASK [../../roles/docker : Add Docker repository] ****************************************************************************************************************************************************
ok: [158.160.26.69]

TASK [../../roles/docker : Update apt packages] ******************************************************************************************************************************************************
ok: [158.160.26.69]

TASK [../../roles/docker : Install Docker] ***********************************************************************************************************************************************************
ok: [158.160.26.69]

TASK [../../roles/docker : Install docker compose] ***************************************************************************************************************************************************
included: /home/djovi/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker_compose.yml for
158.160.26.69

TASK [../../roles/docker : Install Docker Compose using pip] *****************************************************************************************************************************************
ok: [158.160.26.69]

PLAY
RECAP *******************************************************************************************************************************************************************************************
158.160.26.69              : ok=14 changed=1 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0   
```

## Inventory file command

`ansible-inventory -i <name_of_your_inventory_file>.yaml --list`

```
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "158.160.26.69",
                "ansible_user": "djhovi"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "web_server"
        ]
    }
}
```

In inventory, I defined virtual machine related data such as port number and user on VM