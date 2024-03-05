# Best practices

1. Used ansible-lint
2. Used FQCN
3. Named tasks properly

# Outputs

`ansible-playbook playbooks/dev/playbook.yaml -i inventory/inventory.yaml --diff`

```
PLAY [Run Docker role] ***********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [158.160.107.10]

TASK [docker : Install pip] ******************************************************************************************
ok: [158.160.107.10]

TASK [docker : Update repositories] **********************************************************************************
ok: [158.160.107.10]

TASK [docker : Install required packages] ****************************************************************************
ok: [158.160.107.10]

TASK [docker : Add GPG key] ******************************************************************************************
ok: [158.160.107.10]

TASK [docker : Add repository] ***************************************************************************************
ok: [158.160.107.10]

TASK [docker : Install Docker] ***************************************************************************************
ok: [158.160.107.10]

TASK [docker : Install Docker-Compose] *******************************************************************************
ok: [158.160.107.10]

PLAY RECAP ***********************************************************************************************************
158.160.107.10             : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

`ansible-inventory -i inventory/inventory.yaml --list`

```
{
    "_meta": {
        "hostvars": {
            "158.160.107.10": {
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "myhost"
        ]
    },
    "myhost": {
        "hosts": [
            "158.160.107.10"
        ]
    }
}
```