# ANSIBLE

## Best practices
* ansible lint

## Outputs

```
ansible-playbook playbooks/dev/main.yaml -i inventory/default_aws_ec2.yaml --diff
```

```
PLAY [Run Docker role] ***********************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************
ok: [51.15.48.52]

TASK [docker : Install pip] ******************************************************************************************
ok: [51.15.48.52]

TASK [docker : Update repositories] **********************************************************************************
ok: [51.15.48.52]

TASK [docker : Install required packages] ****************************************************************************
ok: [51.15.48.52]

TASK [docker : Add GPG key] ******************************************************************************************
ok: [51.15.48.52]

TASK [docker : Add repository] ***************************************************************************************
ok: [51.15.48.52]

TASK [docker : Install Docker] ***************************************************************************************
ok: [51.15.48.52]

TASK [docker : Install Docker-Compose] *******************************************************************************
ok: [51.15.48.52]

PLAY RECAP ***********************************************************************************************************
51.15.48.52             : ok=8    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

```
ansible-inventory -i inventory/default_aws_ec2.yaml --list
```

```angular2html
{
    "_meta": {
        "hostvars": {
            "51.15.48.52": {
                "ansible_user": "grisharybolovlev"
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
            "51.15.48.52"
        ]
    }
}
```