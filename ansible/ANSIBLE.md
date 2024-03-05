# Ansible

## Best practices

- Follow the structure of files that was recommended in the lab
- Assign a clear names for plays and tasks
- Configure global settings in ```ansible.cfg```
- Use fully qualified collection names to avoid ambiguity

## Outputs

### Deployment Output
 
```sh
$ ansible-playbook playbooks/dev/main.yaml --diff

BECOME password: 

PLAY [web_server] **************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************
ok: [web_server]

TASK [docker : Install pip] ****************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_pip.yml for web_server

TASK [docker : Update apt] *****************************************************************************************
ok: [web_server]

TASK [docker : Install python] *************************************************************************************
ok: [web_server]

TASK [docker : Install pip] ****************************************************************************************
ok: [web_server]

TASK [docker : Install docker] *************************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for web_server

TASK [docker : Update apt] *****************************************************************************************
ok: [web_server]

TASK [docker : Install docker] *************************************************************************************
changed: [web_server]

TASK [docker : Install docker-compose] *****************************************************************************
included: /home/everyonehateme/programing/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for web_server

TASK [docker : Install docker-compose] *****************************************************************************
changed: [web_server]

PLAY RECAP *********************************************************************************************************
web_server                 : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

### Inventory details

```sh
$ ansible-inventory -i inventory/default_local.yml --list
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "84.201.128.97",
                "ansible_user": "vm-admin"
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