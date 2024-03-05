# Best practice

1. Named tasks properly

# Output
## Command 1
``` bash
    sudo ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml --diff
```
```
PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Install pip] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Update repositories] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Install required packages] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Add GPG key] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Add repository] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Install Docker] ***
ok: [cloud_host]

TASK [/Users/renathajrullin/DevOps/S24-core-course-labs/ansible/roles/docker : Install Docker-Compose] ***
ok: [cloud_host]

TASK [Install python3-pip package] *********************************************
ok: [cloud_host]

PLAY RECAP *********************************************************************
cloud_host                 : ok=9    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
## Command 2
``` bash
    ansible-inventory -i ansible/inventory/default_aws_ec2.yml --list
```
```
{
    "_meta": {
        "hostvars": {
            "cloud_host": {
                "ansible_host": "158.160.149.60",
                "ansible_user": "snapman"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "cloud_host"
        ]
    }
}
```
