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

## Output of `ansible-playbook playbooks/dev/main.yml` for `web_app` role

```commandline
PLAY [Run Docker role] ***********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [host01]

TASK [docker : Install python3 and pip] ******************************************************************************
ok: [host01]

TASK [docker : Install Docker] ***************************************************************************************
ok: [host01]

TASK [docker : Install Docker Compose] *******************************************************************************
ok: [host01]

TASK [web_app : Create app directory] ********************************************************************************
changed: [host01]

TASK [web_app : Copy docker-compose template] ************************************************************************
changed: [host01]

TASK [web_app : Ensure docker started] *******************************************************************************
ok: [host01]

TASK [web_app : Run image] *******************************************************************************************
changed: [host01]

TASK [web_app : Remove Docker container] *****************************************************************************
skipping: [host01]

TASK [web_app : Remove related files] ********************************************************************************
skipping: [host01]

PLAY RECAP ***********************************************************************************************************
host01                 : ok=10    changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0  
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
