# Ansible

## Best practices

- Assign unambiguous files.
- Comply with the lab's recommended file structure.
- Set up global preferences in ```ansible.cfg```.
- Use fully qualified collection names to avoid ambiguity.
## Outputs


```json
$ ansible-playbook playbooks/dev/main.yaml --diff
{
    "_meta": {
        "hostvars": {
            "ec2-3-124-209-126.eu-central-1.compute.amazonaws.com": {
                "ansible_connection": "ssh",
                "ansible_ssh_private_key_file": "~/.ssh/devops_new.pem",
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
            "ec2-3-124-209-126.eu-central-1.compute.amazonaws.com"
        ]
    }
}
```
```ansible
$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Install Docker] *********************************************************************************************************************
TASK [Gathering Facts] ***************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install pip] ********************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Add user to docker group] *************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Update packages] *********************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker] *******************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker Compose] ***********************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
PLAY RECAP ***************************************************************************************************************************************************
ec2-3-124-209-126.eu-central-1.compute.amazonaws.com : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
ansible-inventory -i ./ansible/inventory/default_aws_ec2.yml --list
```
