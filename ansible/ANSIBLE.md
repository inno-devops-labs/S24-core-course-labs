# Ansible

## Best practise
Choose XML instead of JSON

Use the same spaces

Use a consistent tagging strategy

Add comments

Use a consistent naming strategy

Define a style guide

Keep it simple

Store your projects in a Version Control System (VCS)

Do not store confidential values in plain text

Test projects
## TASK 1
- installed existing role
```
ansible-galaxy role install geerlingguy.docker
```
```
- hosts: all
  roles:
    - geerlingguy.docker
```

```shell
$ ansible-inventory -i inventory/vm.yacloud_compute.yml --list
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
```shell
$ ansible-playbook playbooks/dev/main.yml -i inventory
PLAY [Deploy Docker on Yandex Cloud] **********************************************************************************

TASK [Gathering Facts] ************************************************************************************************
ok: [178.154.201.217]

TASK [../../roles/docker : include_tasks] *****************************************************************************
included: /mnt/c/MINE/Programming/Devops/S24-core-course-labs/ansible/roles/docker/tasks/setup_repo_debian.yml for 178.154.201.217

TASK [../../roles/docker : Install Dependencies] **********************************************************************
ok: [178.154.201.217]

TASK [../../roles/docker : Setup keyrings folder] *********************************************************************
changed: [178.154.201.217]

TASK [../../roles/docker : Add Docker apt key] ************************************************************************
ok: [178.154.201.217]

TASK [../../roles/docker : Add Docker repository] *********************************************************************
changed: [178.154.201.217]

TASK [../../roles/docker : Disable Unattended Upgrades] ***************************************************************
changed: [178.154.201.217]

TASK [../../roles/docker : Install pip] *******************************************************************************
changed: [178.154.201.217]

TASK [../../roles/docker : include_tasks] *****************************************************************************
included: /mnt/c/MINE/Programming/Devops/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for 178.154.201.217

TASK [../../roles/docker : Install Docker] ****************************************************************************
ok: [178.154.201.217]

TASK [../../roles/docker : include_tasks] *****************************************************************************
included: /mnt/c/MINE/Programming/Devops/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for 178.154.201.217

TASK [../../roles/docker : Install Docker Compose with pip] ***********************************************************
changed: [178.154.201.217]

TASK [Run container] **************************************************************************************************
changed: [178.154.201.217]

PLAY RECAP ************************************************************************************************************
178.154.201.217            : ok=13   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
