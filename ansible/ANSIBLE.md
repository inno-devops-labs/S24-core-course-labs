# Ansible configuration results
- Yandex cloud server
- Config in the inventory 
- Configuring of `ansible.cfg`

## Deployment Output
```bash
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

## Details
```bash
{
    "_meta": {
        "hostvars": {
            "devops": {
                "ansible_connection": "ssh",
                "ansible_host": "158.160.60.140",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "pechersky"
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

## Best practices:
- Using ansible.cfg configuration
- Proper structure
