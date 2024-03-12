# Ansible

## Introduction

This repository uses Ansible for automation and configuration management. Ansible is an open-source automation tool that allows you to define and manage infrastructure as code.

## Ansible Roles

### Existing Ansible Role for Docker

Used the following command to run an Ansible playbook:

```bash
ansible-playbook -i ansible/inventory/cloud_yandex_vm1.yml ansible/playbooks/dev/main.yml
```

The output is following:

```bash
TASK [geerlingguy.docker : Load OS-specific vars.] *********************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************
included: /Users/exemplerie/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for vm1

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *******************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *********************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ****************
skipping: [vm1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *************************************
ok: [vm1]

TASK [geerlingguy.docker : Add Docker apt key.] ************************************************************************************
changed: [vm1]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ****************************************
skipping: [vm1]

TASK [geerlingguy.docker : Add Docker repository.] *********************************************************************************
changed: [vm1]

TASK [geerlingguy.docker : Install Docker packages.] *******************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *******************************************************
changed: [vm1]

TASK [geerlingguy.docker : Install docker-compose plugin.] *************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ******************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***********************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **********************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ******************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ******************************************************************************
changed: [vm1]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Get docker group info using getent.] ********************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***********************************************
skipping: [vm1]

TASK [geerlingguy.docker : include_tasks] ******************************************************************************************
skipping: [vm1]

PLAY RECAP *************************************************************************************************************************
vm1                        : ok=12   changed=4    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0 
```

### Custom Docker Role

Used the following command to run an Ansible playbook:

```bash
ansible-playbook -i ansible/inventory/cloud_yandex_vm1.yml ansible/playbooks/dev/main.yml
```

The output is following:

```bash
PLAY [Deploy Docker] **************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************
ok: [vm1]

TASK [docker : include_tasks] *****************************************************************************************************
included: /Users/exemplerie/Documents/study/devops/S24-core-course-labs/ansible/roles/docker/tasks/install_pip.yml for vm1

TASK [docker : Install pip] *******************************************************************************************************
ok: [vm1]

TASK [docker : include_tasks] *****************************************************************************************************
included: /Users/exemplerie/Documents/study/devops/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm1

TASK [docker : Installation of necessary system packages] *************************************************************************
ok: [vm1]

TASK [docker : Retrieve Docker GPG apt Key] ***************************************************************************************
ok: [vm1]

TASK [docker : Delete conflicting Docker GPG apt Key] *****************************************************************************
ok: [vm1]

TASK [docker : Add Docker Repository to apt sources] ******************************************************************************
ok: [vm1]

TASK [docker : Update apt cache and install Docker Community Edition (docker-ce)] *************************************************
skipping: [vm1]

TASK [docker : include_tasks] *****************************************************************************************************
included: /Users/exemplerie/Documents/study/devops/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm1

TASK [docker : Install Docker Compose] ********************************************************************************************
changed: [vm1]

PLAY RECAP ************************************************************************************************************************
vm1                        : ok=10   changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```

Used the following command to know the inventory information:

```bash
ansible-inventory -i playbooks/dev/main.yml --list
```

The output is following:

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

### Lines of the output from deployment command:

```bash
ansible-playbook -i ansible/inventory/cloud_yandex_vm1.yml ansible/playbooks/dev/main.yml --tags "deploy,wipe"
```

```
PLAY [Deploy Docker] *********************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
ok: [vm1]

PLAY [Deploy Web App] ********************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
ok: [vm1]

TASK [web_app : Copy Docker Compose] *****************************************************************************************************************************
ok: [vm1]

TASK [web_app : Check Docker Compose] ****************************************************************************************************************************
ok: [vm1]

TASK [web_app : Run Docker Compose] ******************************************************************************************************************************
changed: [vm1]

TASK [web_app : include_tasks] ***********************************************************************************************************************************
skipping: [vm1]

PLAY RECAP *******************************************************************************************************************************************************
vm1                        : ok=5    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```