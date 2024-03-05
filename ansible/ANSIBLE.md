PLAY [playbook] *******************************************************************************************************

TASK [docker : Install dependencies] **********************************************************************************
ok: [vm] => (item=apt-transport-https)
ok: [vm] => (item=ca-certificates)
ok: [vm] => (item=curl)
ok: [vm] => (item=gnupg-agent)
ok: [vm] => (item=software-properties-common)

TASK [docker : Add GPG key] *******************************************************************************************
ok: [vm]

TASK [docker : Add docker repo to apt] ********************************************************************************
ok: [vm]

TASK [docker : include_tasks] *****************************************************************************************
included: /root/DevOps-S24/ansible/roles/docker/tasks/install_docker.yml for vm

TASK [docker : install docker] ****************************************************************************************
ok: [vm] => (item=docker-ce)
ok: [vm] => (item=docker-ce-cli)
ok: [vm] => (item=containerd.io)

TASK [docker : check docker is active] ********************************************************************************
ok: [vm]

TASK [docker : Ensure group "docker" exists] **************************************************************************
ok: [vm]

TASK [docker : adding ubuntu to docker group] *************************************************************************
ok: [vm]

TASK [docker : include_tasks] *****************************************************************************************
included: /root/DevOps-S24/ansible/roles/docker/tasks/install_compose.yml for vm

TASK [docker : Install docker-compose] ********************************************************************************
ok: [vm]

TASK [docker : Change file ownership, group and permissions] **********************************************************
ok: [vm]

PLAY RECAP ************************************************************************************************************
vm                         : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
