# Ansible

## Ansible best practices

* Using version control: Keeping your playbooks and inventory files in VSC like `git`
* Follow the directory structure: Organize your playbook directory structure (separating roles, host inventories, and group variables)
* Use dynamic inventory with clouds.
* Documentation: Document your playbooks, roles, and variables using comments or README files

## Deploy docker to web server

### Initial steps

* Generate ssh keys on host machine

```shell
ssh-keygen -t ed25519
```
* Connect to server and configure ssh to ansible user

```shell
sudo useradd -m -d /home/ansible-user -s /bin/bash ansible-user
sudo su - ansible-user
mkdir .ssh
touch .ssh/authorized_keys
echo "public_key" > /home/ansible-user/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

* Add password to ansible user (from root)

```shell
sudo passwd ansible-user
```

* Add ansible-user to sudo group

```shell
sudo usermod -aG sudo ansible-user
```

### Check ansible connection
```shell
(venv) shredding@SHREDDING-2 ansible % ansible web_server -m ping -i inventory/default_aws_ec2.yml
web_server | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}

```

### Use pip for docker set up

```shell
(venv) shredding@SHREDDING-2 ansible % ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml -K 
BECOME password: 

PLAY [Deploy Docker] **************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install pip] *******************************************************************************************************************************
included: /Users/shredding/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/pip.yml for web_server

TASK [../../roles/docker : Update apt] ********************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install python] ****************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install pip] *******************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install docker] ****************************************************************************************************************************
included: /Users/shredding/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for web_server

TASK [../../roles/docker : Install docker via pip] ********************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Install docker-compose] ********************************************************************************************************************
included: /Users/shredding/PycharmProjects/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for web_server

TASK [../../roles/docker : Install docker-compose via pip] ************************************************************************************************************
ok: [web_server]

PLAY RECAP ************************************************************************************************************************************************************
web_server                 : ok=9    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

### Inventory details with docker via pip

```shell
(venv) shredding@SHREDDING-2 ansible % ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "78.153.140.41",
                "ansible_user": "ansible-user"
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
            "web_server"
        ]
    }
}

```