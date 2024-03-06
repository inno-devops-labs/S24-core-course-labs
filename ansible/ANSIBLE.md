# Ansible

## Installing Ansible
```
python3 -m pip install --user ansible
```

## Adding a docker role
```
ansible-galaxy role install geerlingguy.docker
```

## Invventory
```
$ ansible-inventory --list
{
    "_meta": {
        "hostvars": {
            "ec2-user@ec2-18-171-184-83.eu-west-2.compute.amazonaws.com": {
                "ansible_connection": "ssh",
                "ansible_ssh_private_key_file": "ansible.pem",
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
            "ec2-user@ec2-18-171-184-83.eu-west-2.compute.amazonaws.com"
        ]
    }
}
```

## Running a playbook
```
$ ansible-playbook playbook/dev/main.yaml --diff


PLAY [Install Docker and Docker Compose] *******************************************************************************

TASK [Gathering Facts] *************************************************************************************************
fatal: [ec2-user@ec2-18-171-184-83.eu-west-2.compute.amazonaws.com]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: no such identity: ansible.pem: No such file or directory\r\nubuntu@ec2-18-171-184-83.eu-west-2.compute.amazonaws.com: Permission denied (publickey,gssapi-keyex,gssapi-with-mic).", "unreachable": true}

PLAY RECAP *************************************************************************************************************
ec2-user@ec2-18-171-184-83.eu-west-2.compute.amazonaws.com : ok=0    changed=0    unreachable=1    failed=0    skipped=0    rescued=0    ignored=0
```

