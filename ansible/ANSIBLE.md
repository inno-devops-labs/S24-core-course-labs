# Ansible Project Overview

## Playbook: `playbooks/dev/main.yaml`

Automates Docker container deployment on localhost.

## Role: `roles/docker`

Facilitates Docker and Docker Compose installation on Ubuntu systems. Adheres to best practices by organizing files based on functionality.

## Configuration: `ansible.cfg`

Configured to specify project directories following best practices.

## Output of `ansible-playbook ./ansible/playbooks/dev/main.yaml --diff`:
```bash
PLAY [Task 2] *************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] *********************************************************************************************************************************
included: /mnt/d/progs/uni_projects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install pip] ***********************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker] ********************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] *********************************************************************************************************************************
included: /mnt/d/progs/uni_projects/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Install Docker Compose] ************************************************************************************************************************
ok: [localhost]

TASK [Pull Docker Image] **************************************************************************************************************************************
ok: [localhost]

TASK [Run Docker Container] ***********************************************************************************************************************************
ok: [localhost]

PLAY RECAP ****************************************************************************************************************************************************
localhost                  : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Output of `ansible-inventory -i ansible/inventory/timeweb_cloud.yml --list`:

```bash
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    }
}
```