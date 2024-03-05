PLAY [all,localhost] ************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************
ok: [localhost]

TASK [Install dependencies] *****************************************************************************************
ok: [localhost] => (item=apt-transport-https)
ok: [localhost] => (item=ca-certificates)
ok: [localhost] => (item=curl)
ok: [localhost] => (item=gnupg-agent)
ok: [localhost] => (item=software-properties-common)

TASK [Add GPG key] **************************************************************************************************
ok: [localhost]

TASK [Add docker repo to apt] ***************************************************************************************
ok: [localhost]

TASK [include_tasks] ************************************************************************************************
included: /root/DevOps-S24/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [install docker] ***********************************************************************************************
ok: [localhost] => (item=docker-ce)
ok: [localhost] => (item=docker-ce-cli)
ok: [localhost] => (item=containerd.io)

TASK [check docker is active] ***************************************************************************************
ok: [localhost]

TASK [Ensure group "docker" exists] *********************************************************************************
ok: [localhost]

TASK [adding ubuntu to docker group] ********************************************************************************
changed: [localhost]

TASK [include_tasks] ************************************************************************************************
included: /root/DevOps-S24/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [Install docker-compose] ***************************************************************************************
changed: [localhost]

TASK [Change file ownership, group and permissions] *****************************************************************
changed: [localhost]

PLAY RECAP **********************************************************************************************************
localhost                  : ok=12   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
