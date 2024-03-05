### Deployment command
```ansible-playbook playbooks/dev/main.yaml --diff```
```
(myenv) nikitazorin@MacBook-Air-Nikita-2 ansible % ansible-playbook playbooks/dev/main.yaml --diff                                                                       

PLAY [Install Docker] ***************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************
ok: [vm1]

TASK [docker : include_tasks] *******************************************************************************************************************************************
included: /Users/nikitazorin/Documents/DevOps/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yaml for vm1

TASK [docker : Installation of necessary system packages] ***************************************************************************************************************
ok: [vm1]

TASK [docker : Retrieve Docker GPG apt Key] *****************************************************************************************************************************
ok: [vm1]

TASK [docker : Delete conflicting Docker GPG apt Key] *******************************************************************************************************************
ok: [vm1]

TASK [docker : Add Docker Repository to apt sources] ********************************************************************************************************************
ok: [vm1]

TASK [docker : Update apt cache and install Docker Community Edition (docker-ce)] ***************************************************************************************
skipping: [vm1]

TASK [docker : include_tasks] *******************************************************************************************************************************************
included: /Users/nikitazorin/Documents/DevOps/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yaml for vm1

TASK [docker : Install pip] *********************************************************************************************************************************************
ok: [vm1]

TASK [docker : Set Docker Compose pip package name] *********************************************************************************************************************
ok: [vm1]

TASK [docker : Install Docker Compose] **********************************************************************************************************************************
changed: [vm1]

PLAY RECAP **************************************************************************************************************************************************************
vm1                        : ok=10   changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

```
### Inventory information
``` ansible-inventory -i inventory/cloud_yandex.yaml --list```

```
{
    "_meta": {
        "hostvars": {
            "vm1": {
                "ansible_host": "178.154.207.144",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "myhosts"
        ]
    },
    "myhosts": {
        "hosts": [
            "vm1"
        ]
    }
}

```