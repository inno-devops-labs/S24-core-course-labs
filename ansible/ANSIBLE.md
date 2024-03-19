## ansible-playbook main.yml --diff

```bash
[WARNING]: provided hosts list is empty, only localhost is available. Note that the
implicit localhost does not match 'all'

PLAY [Install pip] *******************************************************************

TASK [Gathering Facts] ***************************************************************
ok: [localhost]

TASK [Install python3-pip] ***********************************************************
ok: [localhost]

PLAY [Install Docker] ****************************************************************

TASK [Gathering Facts] ***************************************************************
ok: [localhost]

TASK [include_tasks] *****************************************************************
included: /home/system_user/ansible-env/ans/roles/docker/tasks/install_docker.yml for localhost

TASK [Update apt package cache] ******************************************************
ok: [localhost]

TASK [Install required packages for Docker] ******************************************
ok: [localhost] => (item=apt-transport-https)
ok: [localhost] => (item=ca-certificates)
ok: [localhost] => (item=curl)
ok: [localhost] => (item=gnupg)
ok: [localhost] => (item=lsb-release)

TASK [Add GPG key] *******************************************************************
ok: [localhost]

TASK [Add Docker repository] *********************************************************
ok: [localhost]

TASK [Install Docker] ****************************************************************
ok: [localhost]

TASK [Ensure Docker service is started and enabled] **********************************
ok: [localhost]

PLAY [Install Docker Compose] ********************************************************

TASK [Gathering Facts] ***************************************************************
ok: [localhost]

TASK [include_tasks] *****************************************************************
included: /home/system_user/ansible-env/ans/roles/docker/tasks/install_compose.yml for localhost

TASK [Install Docker Compose] ********************************************************
ok: [localhost]

PLAY RECAP ***************************************************************************
localhost                  : ok=13   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## ansible-playbook -i ../../inventory/inventory.yml main.yml
```bash
TASK [Update apt package cache] ************************************************
changed: [yandex_host]

TASK [Install required packages for Docker] ************************************
ok: [yandex_host] => (item=apt-transport-https)
ok: [yandex_host] => (item=ca-certificates)
ok: [yandex_host] => (item=curl)
ok: [yandex_host] => (item=gnupg)
ok: [yandex_host] => (item=lsb-release)

TASK [Add GPG key] *************************************************************
ok: [yandex_host]

TASK [Add Docker repository] ***************************************************
ok: [yandex_host]

TASK [Install Docker] **********************************************************
ok: [yandex_host]

TASK [Ensure Docker service is started and enabled] ****************************
ok: [yandex_host]

PLAY [Install Docker Compose] **************************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_host]

TASK [include_tasks] ***********************************************************
included: /home/system_user/ansible-env/ans/roles/docker/tasks/install_compose.yml for yandex_host

TASK [Install Docker Compose] **************************************************
ok: [yandex_host]

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_host]

TASK [include_tasks] ***********************************************************
included: /home/system_user/ansible-env/ans/roles/web_app/tasks/main.yml for yandex_host

TASK [Pull the Docker image] ***************************************************
ok: [yandex_host]

TASK [Run the Docker container] ************************************************
ok: [yandex_host]

PLAY RECAP *********************************************************************
yandex_host                : ok=17   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```