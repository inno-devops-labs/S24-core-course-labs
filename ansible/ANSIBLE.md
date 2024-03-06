# Ansible-related work 

## Best practices

1. Testing with Ansible linting: validating Ansible code using linting tools like ansible-lint. Linting helps identify potential issues, enforces best practices, and improves the overall quality of  automation code.
2. Using FQCN
3. Modular playbook structure: organizing playbook into logical module.

## Outputs of following commands:

`ansible-playbook playbooks/dev/playbook.yaml -i inventory/inventory.yaml --diff`

```
PLAY [Run Docker role] ***********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [84.201.135.38]

TASK [docker : Install pip] ******************************************************************************************
ok: [84.201.135.38]

TASK [docker : Update repositories] **********************************************************************************
ok: [84.201.135.38]

TASK [docker : Install required packages] ****************************************************************************
ok: [84.201.135.38]

TASK [docker : Add GPG key] ******************************************************************************************
ok: [84.201.135.38]

TASK [docker : Add repository] ***************************************************************************************
ok: [84.201.135.38]

TASK [docker : Install Docker] ***************************************************************************************
ok: [84.201.135.38]

TASK [docker : Install Docker-Compose] *******************************************************************************
ok: [84.201.135.38]

PLAY RECAP ***********************************************************************************************************
84.201.135.38             : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

`ansible-inventory -i inventory/inventory.yaml --list`

```
{
    "_meta": {
        "hostvars": {
            "84.201.135.38": {
                "ansible_user": "hugowea"
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
            "84.201.135.38"
        ]
    }
}
```