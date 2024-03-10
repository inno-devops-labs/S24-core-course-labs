# Outputs for Task 2

## ansible-playbook playbooks/dev/main.yml --diff - fails without vpn

```text
PLAY [Install Docker] **************************************\*\***************************************\***************************************\*\***************************************

TASK [Gathering Facts] ************************************\*\*\*\*************************************\*\*\*\*************************************\*\*\*\*************************************
ok: [localhost]

TASK [docker : Add user to docker group] ********************************\*\*\*\*********************************\*\*********************************\*\*\*\*********************************
ok: [localhost]

TASK [docker : include_tasks] ************************************\*\*************************************\*************************************\*\*************************************
included: /home/mpiniagin/stuff/S24-DevOps-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install pip] ************************************\*\*************************************\*\*\*************************************\*\*************************************
ok: [localhost]

TASK [docker : Install system packages] ********************************\*\*\*\*********************************\*\*\*********************************\*\*\*\*********************************
ok: [localhost]

TASK [docker : Add Docker GPG Key] **********************************\*\***********************************\*\*\*\***********************************\*\***********************************
ok: [localhost]

TASK [docker : Add Docker repository] **********************************\*\***********************************\***********************************\*\***********************************
ok: [localhost]

TASK [docker : Update apt cache and install docker-ce] ****************************\*\*\*\*****************************\*\*\*\*****************************\*\*\*\*****************************
skipping: [localhost]

TASK [docker : include_tasks] ************************************\*\*************************************\*************************************\*\*************************************
included: /home/mpiniagin/stuff/S24-DevOps-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Install Docker Compose using pip] ******************************\*\*\*\*******************************\*\*******************************\*\*\*\*******************************
ok: [localhost]

PLAY RECAP ****************************************\*\*****************************************\*\*\*\*****************************************\*\*****************************************
localhost : ok=9 changed=0 unreachable=0 failed=0 skipped=1 rescued=0 ignored=0
```

## ansible-inventory -i inventory/default_aws_ec2.yml --list

### Results in an empty inventory because I don't have any EC2 instances

```json
{
  "_meta": {
    "hostvars": {}
  },
  "all": {
    "children": ["ungrouped"]
  }
}
```

## Outputs for sudo ansible-playbook playbooks/dev/web_app.yml

```text
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match
'all'

PLAY [Deploy Web App] ***************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************
ok: [localhost]

TASK [docker : Add user to docker group] ********************************************************************************
ok: [localhost]

TASK [docker : include_tasks] *******************************************************************************************
included: /home/mpiniagin/stuff/S24-DevOps-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install pip] *********************************************************************************************
ok: [localhost]

TASK [docker : Install system packages] *********************************************************************************
ok: [localhost]

TASK [docker : Add Docker GPG Key] **************************************************************************************
ok: [localhost]

TASK [docker : Add Docker repository] ***********************************************************************************
ok: [localhost]

TASK [docker : Update apt cache and install docker-ce] ******************************************************************
skipping: [localhost]

TASK [docker : include_tasks] *******************************************************************************************
included: /home/mpiniagin/stuff/S24-DevOps-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Install Docker Compose using pip] ************************************************************************
ok: [localhost]

TASK [web_app : Wipe app] ***********************************************************************************************
included: /home/mpiniagin/stuff/S24-DevOps-labs/ansible/roles/web_app/tasks/wipe.yml for localhost

TASK [web_app : Info] ***************************************************************************************************
skipping: [localhost]

TASK [web_app : Stop container] *****************************************************************************************
skipping: [localhost]

TASK [web_app : Remove container] ***************************************************************************************
skipping: [localhost]

TASK [web_app : Remove image] *******************************************************************************************
skipping: [localhost]

TASK [web_app : Check compose file] *************************************************************************************
ok: [localhost]

TASK [web_app : Delete Docker Compose] **************************************************************************
skipping: [localhost]

TASK [web_app : Delete directory] ***************************************************************************************
ok: [localhost]

TASK [web_app : Deploy app] *********************************************************************************************
included: /home/mpiniagin/stuff/S24-DevOps-labs/ansible/roles/web_app/tasks/deploy.yml for localhost

TASK [web_app : Deploy App using Docker] *********************************************************************************
skipping: [localhost]

TASK [web_app : Create directory] ***************************************************************************************
changed: [localhost]

TASK [web_app : Create docker compose file] ******************************************************************************
changed: [localhost]

TASK [web_app : Run Docker Compose] *************************************************************************************
changed: [localhost]

PLAY RECAP **************************************************************************************************************
localhost                  : ok=15   changed=3    unreachable=0    failed=0    skipped=7    rescued=0    ignored=0
```
