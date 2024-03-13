# Best practices
- Do not stored confidential values in text
- Tried to keep it simple
- Used consistent naming



# Task 1
- Intalled existing role `geerlingguy.docker`
- Utilizied the following playbook
```
- hosts: all
  roles:
    - geerlingguy.docker
```
- Checked all worked

# Task 2

## Output
```
PLAY [Install Docker] ********************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************
ok: [51.250.92.223]

TASK [../../roles/docker : include_tasks] ************************************************************************************************
included: /mnt/d/MINE/Repositories/Devops/ansible/roles/docker/tasks/setup_repo_debian.yml for 51.250.92.223

TASK [../../roles/docker : Install Dependencies] *****************************************************************************************
ok: [51.250.92.223]

TASK [../../roles/docker : Setup keyrings folder] ****************************************************************************************
changed: [51.250.92.223]

TASK [../../roles/docker : Docker apt key] ***********************************************************************************************
ok: [51.250.92.223]

TASK [../../roles/docker : Docker repository] ********************************************************************************************
ok: [51.250.92.223]

TASK [../../roles/docker : Install pip] **************************************************************************************************
ok: [51.250.92.223]

TASK [../../roles/docker : Install Docker] ***********************************************************************************************
ok: [51.250.92.223]

TASK [../../roles/docker : Install Docker Compose] ***************************************************************************************
ok: [51.250.92.223]

PLAY RECAP *******************************************************************************************************************************
51.250.92.223              : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory
```
{
    "_meta": {
        "hostvars": {
            "51.250.92.223": {
                "ansible_ssh_private_key_file": "~/yc_devops",
                "ansible_user": "habur331"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "vm"
        ]
    },
    "vm": {
        "hosts": [
            "51.250.92.223"
        ]
    }
}
```