# Ansible Docker

## Docker Setup using ansible-galaxy

```
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/ansible$ ansible-galaxy install geerlingguy.docker
Starting galaxy role install process
- downloading role 'docker', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-docker/archive/7.1.0.tar.gz
- extracting geerlingguy.docker to /home/fatm1nd/Documents/Innopolis/devops-core-innopolis-course/ansible/roles/geerlingguy.docker
- geerlingguy.docker (7.1.0) was installed successfully
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/ansible$ ansible-playbook playbooks/main.yml --diff

PLAY [Install Docker] ***********************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Load OS-specific vars.] ******************************************************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************************
included: /home/fatm1nd/Documents/Innopolis/devops-core-innopolis-course/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for vm1

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ****************************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ******************************************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] *************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] **********************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Add Docker apt key.] *********************************************************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] **********************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] *************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Add Docker repository.] ******************************************************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Install Docker packages.] ****************************************************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ****************************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Install docker-compose plugin.] **********************************************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **********************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***************************************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********************************************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *******************************************************************************************************************
ok: [vm1]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***************************************************************************************************

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Get docker group info using getent.] *****************************************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ********************************************************************************************************
skipping: [vm1]

TASK [geerlingguy.docker : include_tasks] ***************************************************************************************************************************************************
skipping: [vm1]

PLAY RECAP **********************************************************************************************************************************************************************************
vm1                        : ok=11   changed=0    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   

fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/ansible$ 
```

## Install Docker and Docker Compose using custom role

```
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/ansible$ ansible-playbook playbooks/dev/main.yml --diff

PLAY [Install Docker] ***********************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [vm1]

TASK [docker : Update apt cache] ************************************************************************************************************************************************************
changed: [vm1]

TASK [docker : Install pip] *****************************************************************************************************************************************************************
ok: [vm1]

TASK [docker : Install Docker dependencies] *************************************************************************************************************************************************
ok: [vm1] => (item=apt-transport-https)
ok: [vm1] => (item=ca-certificates)
ok: [vm1] => (item=curl)
ok: [vm1] => (item=gnupg-agent)
ok: [vm1] => (item=software-properties-common)

TASK [docker : Remove conflicting Docker GPG keys] ******************************************************************************************************************************************
ok: [vm1]

TASK [docker : Clear APT cache] *************************************************************************************************************************************************************
ok: [vm1]

TASK [docker : Ensure correct Docker repository configuration] ******************************************************************************************************************************
ok: [vm1]

TASK [docker : Install Docker] **************************************************************************************************************************************************************
skipping: [vm1]

TASK [docker : Install Docker Compose] ******************************************************************************************************************************************************
changed: [vm1]

TASK [docker : Add Docker GPG key] **********************************************************************************************************************************************************
ok: [vm1]

TASK [docker : Add Docker repository] *******************************************************************************************************************************************************
ok: [vm1]

TASK [docker : Install Docker] **************************************************************************************************************************************************************
ok: [vm1]

TASK [docker : Install Docker Compose] ******************************************************************************************************************************************************
ok: [vm1]

PLAY RECAP **********************************************************************************************************************************************************************************
vm1                        : ok=12   changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0 
```

## Ansible Inventory

```
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/ansible$ ansible-inventory -i inventory/yandex_cloud.yml --list
{
    "_meta": {
        "hostvars": {
            "vm1": {
                "ansible_host": "62.84.117.86",
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

## Web App Deployment

```
fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/ansible$ ansible-playbook playbooks/dev/main.yml --tags "deploy,wipe" --diff

PLAY [Install Docker] *******************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************
ok: [vm1]

PLAY [Deploy Web Application] ***********************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************
ok: [vm1]

TASK [web_app : Copy Docker Compose template] *******************************************************************************
ok: [vm1]

TASK [web_app : Ensure Docker Compose is installed] *************************************************************************
ok: [vm1]

TASK [web_app : Run Docker Compose] *****************************************************************************************
changed: [vm1]

TASK [web_app : include_tasks] **********************************************************************************************
skipping: [vm1]

PLAY RECAP ******************************************************************************************************************
vm1                        : ok=5    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

fatm1nd@fatm1nd-IdeaPad-5-14ARE05:~/Documents/Innopolis/devops-core-innopolis-course/ansible$ 
```