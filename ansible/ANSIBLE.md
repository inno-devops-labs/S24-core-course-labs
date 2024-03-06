# Deployment Output
```sh
ansible-playbook playbooks/dev/main.yml --diff
```

```
PLAY [lab-05] **************************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [web_server]

TASK [docker : include_tasks] **********************************************************************************************************************************************
included: /Users/dilaraf/DevOps_Innopolis/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yaml for web_server

TASK [docker : Install dependences for Docker] *****************************************************************************************************************************
ok: [web_server] => (item=apt-transport-https)
ok: [web_server] => (item=ca-certificates)
ok: [web_server] => (item=curl)
ok: [web_server] => (item=gnupg-agent)
ok: [web_server] => (item=software-properties-common)

TASK [docker : Add GPG key for  Docker] ************************************************************************************************************************************
ok: [web_server]

TASK [docker : Add Docker repository] **************************************************************************************************************************************
ok: [web_server]

TASK [docker : Update apt packages] ****************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install Docker] *********************************************************************************************************************************************
ok: [web_server]

TASK [docker : include_tasks] **********************************************************************************************************************************************
included: /Users/dilaraf/DevOps_Innopolis/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yaml for web_server

TASK [docker : Update apt] *************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install python] *********************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install pip] ************************************************************************************************************************************************
ok: [web_server]

TASK [docker : Install Docker Compose using pip] ***************************************************************************************************************************
ok: [web_server]

PLAY RECAP *****************************************************************************************************************************************************************
web_server                 : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


```

# Inventory Details
```sh
ansible-inventory -i inventory/yandex_cloud.yaml --list
```

```
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "51.250.8.183",
                "ansible_user": "dfarkhutdinova"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "web_server"
        ]
    }
}
```