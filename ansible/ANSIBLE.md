### ansible-playbook playbooks/dev/main.yml

```
PLAY [all] **********************************************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [host_01]

TASK [docker : Install `pip`] ***************************************************************************
ok: [host_01]

TASK [docker : Install Docker] **************************************************************************
changed: [host_01]

TASK [docker : Install Docker Compose] ******************************************************************
changed: [host_01]

PLAY RECAP **********************************************************************************************
host_01                    : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

### ansible-inventory -i inventory/default_yc_ec2.yml --list

```
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_connection": "ssh",
                "ansible_host": "62.84.117.83",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "maintheme"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "selfhosts"
        ]
    },
    "selfhosts": {
        "hosts": [
            "host_01"
        ]
    }
}
```
The connection to host 62.84.117.83 is done via ssh and get the key from .ssh/id_rsa file. The host belongs to selfhosts group.