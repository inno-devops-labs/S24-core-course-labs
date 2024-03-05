## Output of `ansible-playbook playbooks/dev/main.yml --diff`

```commandline
PLAY [Run Docker role] ***********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [84.201.172.152]

TASK [docker : Install python3 and pip] ******************************************************************************
ok: [84.201.172.152]

TASK [docker : Install Docker] ***************************************************************************************
ok: [84.201.172.152]

TASK [docker : Install Docker Compose] *******************************************************************************
ok: [84.201.172.152]

PLAY RECAP ***********************************************************************************************************
84.201.172.152             : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Output of `ansible-inventory -i inventory/default_cloud.yml --list`

```commandline
{
    "_meta": {
        "hostvars": {
            "host01": {
                "ansible_host": "84.201.172.152",
                "ansible_user": "ubuntu"
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
            "host01"
        ]
    }
}
```
