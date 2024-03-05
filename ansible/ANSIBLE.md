# Ansible

## Deployment Output
```bash
(venv) anastasiamartynova@Anastasias-MacBook-Pro ansible % ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Install Docker] ******************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
ok: [ubuntu_server]

TASK [docker : Install docker] *********************************************************************************************************************************
included: /Users/anastasiamartynova/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for ubuntu_server

TASK [docker : Installation of necessary system packages] ******************************************************************************************************
ok: [ubuntu_server]

TASK [docker : Retrieve Docker GPG apt Key] ********************************************************************************************************************
ok: [ubuntu_server]

TASK [docker : Delete conflicting Docker GPG apt Key] **********************************************************************************************************
ok: [ubuntu_server]

TASK [docker : Add Docker Repository to apt sources] ***********************************************************************************************************
ok: [ubuntu_server]

TASK [docker : Update apt cache and install Docker Community Edition (docker-ce)] ******************************************************************************
skipping: [ubuntu_server]

TASK [docker : Install docker-compose] *************************************************************************************************************************
included: /Users/anastasiamartynova/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for ubuntu_server

TASK [docker : Install pip] ************************************************************************************************************************************
ok: [ubuntu_server]

TASK [docker : Set Docker Compose pip package name] ************************************************************************************************************
ok: [ubuntu_server]

TASK [docker : Install Docker Compose] *************************************************************************************************************************
ok: [ubuntu_server]

PLAY RECAP *****************************************************************************************************************************************************
ubuntu_server              : ok=10   changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```
## Inventory Details

```bash
(venv) anastasiamartynova@Anastasias-MacBook-Pro ansible % ansible-inventory -i inventory/cloud_yandex.yml --list 
{
    "_meta": {
        "hostvars": {
            "ubuntu_server": {
                "ansible_host": "45.61.137.75",
                "ansible_user": "root"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "servers"
        ]
    },
    "servers": {
        "hosts": [
            "ubuntu_server"
        ]
    }
}

```