# Ansible

## Prerequisites

The assignment required I have an AWS EC2 instance running that could be accessed using SSH. I also needed to have `ansible` installed on my local machine.

For `ansible.cfg`, I used the following configuration:

```ini
inventory=./inventory
roles_path=./roles
host_key_checking=False
```

The first two were to specify the directory for the inventory and roles. The `host_key_checking` was set to `False` to avoid the prompt for adding the host to the `known_hosts` file.

## Inventory

I used static inventory for specifying the nodes in which ansible will apply the configurations and tasks

### Output

Running `ansible-inventory -i inventory/default_aws_ec2.yml` gives me the following output:

```json
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

The playbook `main.yml` in the `playbooks/dev` directory to use the role looks like this:

```yaml
- name: Install Docker and Docker Compose
  hosts: aws_ec2
  roles:
    - role: docker
      become: true
```

### Output (Custom)

Running `ansible-playbook playbooks/dev/main.yml --diff` gives me the following output:

```ansible


PLAY [Install Docker and Docker Compose] *********************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]

TASK [../../roles/docker : Install `pip`] ********************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]

TASK [../../roles/docker : Refresh apt packages] *************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]

TASK [../../roles/docker : Install/Update docker.io] *********************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]

TASK [../../roles/docker : Install docker] *******************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]

TASK [../../roles/docker : Install docker-compose] ***********************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]

PLAY RECAP ***************************************************************************************************************************************************
ec2-3-124-209-126.eu-central-1.compute.amazonaws.com : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  

ansible-inventory -i ./ansible/inventory/default_aws_ec2.yml --list

```

## Best Practices

- A proper folder structure was used to organize the files.
- `ansible.cfg` was used for global settings.
- Virtual environment was maintained
- `--syntax-check` was used before running the playbook to check for syntax errors.
- `ansible-lint` was used to check for best practices.



