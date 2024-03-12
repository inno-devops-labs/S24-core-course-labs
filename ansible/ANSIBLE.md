#### Ansible Overview

Ansible is an automation tool that simplifies complex, cross-platform IT tasks. It's used by IT professionals for tasks like application deployment, system updates, cloud provisioning, and configuration management.

## Working with Ansible: Roles, Playbooks, and Inventory

- **Roles:**

Roles are Ansible's way of bundling related tasks, variables, and handlers. They simplify the management of complex projects and promote reusability of code. Roles follow a standard directory structure, which includes tasks, handlers, defaults, vars, etc, and this structure helps in managing role-specific content.

- **Playbooks:**

Playbooks are Ansible's language for automation. They are written in YAML and provide a human-readable way to model IT processes. Playbooks facilitate the management of configurations and deployments. They can also orchestrate complex IT workflows involving rolling updates and delegate actions. Ansible includes several options for playbook verification such as --check, --diff, --list-hosts, --list-tasks, and --syntax-check.

- **Inventory:**

The inventory in Ansible is a catalog of nodes managed by the tool. It contains node-specific details like the IP address and is used for grouping nodes and assigning variables in bulk. The inventory can be dynamic, and Ansible can use the output of an executable inventory file. It's advisable to maintain playbooks, roles, inventory, and variables files in a version control system for easy auditing and maintenance.


PLAY [Установка Docker] ********************************************************

TASK [Gathering Facts] *********************************************************
ok: [new_host]

TASK [docker : Update apt] *****************************************************
changed: [new_host]

TASK [docker : Python3 and pip3 installation] **********************************
ok: [new_host]

TASK [docker : Install Docker] *************************************************
ok: [new_host]

TASK [docker : Install Docker Compose] *****************************************
ok: [new_host]

PLAY RECAP *********************************************************************
new_host                   : ok=5    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
