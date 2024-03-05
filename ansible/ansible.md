# Ansible

## Requirements 

- Yandex cloud server and config in the inventory file 
- Configuring of `ansible.cfg`

## Task 2.3 
`ansible-playbook playbooks/dev/main.yml --diff`

```
PLAY [Install docker] **************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [devops]

TASK [docker : Install `pip`] ******************************************************************************************
ok: [devops]

TASK [docker : Refresh apt packages] ***********************************************************************************
ok: [devops]

TASK [docker : Install/Update docker.io] *******************************************************************************
ok: [devops]

TASK [docker : Install docker] *****************************************************************************************
ok: [devops]

TASK [docker : Install docker-compose] *********************************************************************************
ok: [devops]

PLAY RECAP *************************************************************************************************************
devops                     : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Task 2.4

`ansible-inventory -i inventory/yandex_cloud.yaml --list`

``` 
{
    "_meta": {
        "hostvars": {
            "devops": {
                "ansible_connection": "ssh",
                "ansible_host": "158.160.150.142",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "alba"
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
            "devops"
        ]
    }
}
```

## Best practices used

- Organized file in proper way
- Ansible.cfg file for global settings