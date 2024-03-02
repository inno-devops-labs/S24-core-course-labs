# Lab 5 - Ansible Setup

## Best practicies
- I configured and init all folders using ```ansible init``` to create automatically folders and project architecture.
- Documenting and use naming in ```.yml``` files
- Project structure according to Ansible standarts


## Steps of implementation

1. Initialize /roles/docker and /roles/web_server directories using ```ansible init``` to create a strcuture of the project.
2. Set up my ssh in the AWS terminal.
3. Add inventor ec2 file with server public IP.
3. Add necessary code and files to install docker and docker compose.
4. Add main.yaml in playbooks with roles.
4. Add Ansible.cfg.
5. Test outputs (The result will be in the next paragraph)


## Outputs

```
ansible-playbook playbooks/dev/main.yaml --diff 
```
```
BECOME password: 

PLAY [Setup docker] ******************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Update apt] *************************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Python3 and pip3 installation] ******************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Docker installation] ****************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Docker-compose installation] ********************************************************************************************************************
changed: [web_server]

PLAY RECAP *****************************************************************************************************************************************************************
web_server                 : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

```
ansible-inventory -i inventory/default_aws_ec2.yml --list 
```

```
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "16.171.41.136",
                "ansible_user": "ansible-user"
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
