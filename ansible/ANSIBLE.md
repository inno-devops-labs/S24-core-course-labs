# Ansible lab

- I installed Ansible
- I initiated directory with `ansible-galaxy init ansible/roles/docker`
- I installed deps. `ansible-galaxy install geerlingguy.docker`

## Working stages

### Machine configuration

I confidured ssh on both my machine and remote Amazon AWS.

### Working with ansible

- I configured ansible configuration files.

Then I ran: 

```
(Myenv) @blinikar ➜ /workspaces/S24-core-course-labs/ansible (lab4) $ ansible-playbook -i inverntory/default_aws_ec2.yml playbooks/dev/main.yaml -K 
[WARNING]: Ansible is being run in a world writable directory (/workspaces/S24-core-course-labs/ansible), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
BECOME password: 

PLAY [web_server] ***********************************************************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Update apt] **************************************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Python3 and pip3 installation] *******************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Docker installation] *****************************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Docker-compose installation] *********************************************************************************************************************************
changed: [web_server]

PLAY RECAP ******************************************************************************************************************************************************************************
web_server                 : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

Result of list command:

```
(Myenv) @blinikar ➜ /workspaces/S24-core-course-labs/ansible (lab4) $ ansible-inventory -i inverntory/default_aws_ec2.yml --list 
[WARNING]: Ansible is being run in a world writable directory (/workspaces/S24-core-course-labs/ansible), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "18.237.114.36",
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
