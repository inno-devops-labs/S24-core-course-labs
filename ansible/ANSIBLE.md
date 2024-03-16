# Ansible

## Inventory

This Ansible inventory file defines a single host named `host1` with the IP address `158.160.62.182` and the `ubuntu`
user as the target for Ansible operations.

## Playbook

This Ansible playbook gives a series of tasks to be executed across all hosts. It incorporates a `docker` role to be
executed with elevated privileges, and specifies a variable `ansible_ssh_private_key_file` indicating the location of
the SSH private key file.

## Role: docker

1. `default/main.yml` - defines configurations for installing and managing Docker and
   Docker Compose.
2. `handlers/main.yml` - defines a handler that employs the service module to restart the Docker
   service when triggered.
3. `tasks/install_compose.yml` - installs Docker Compose using the pip module.
4. `tasks/install_docker.yml` - installs Docker on a Debian-based system via the `apt` module.
5. `tasks/main.yml` - defines tasks to update the apt cache, install `Python 3` and `pip3`, and import and execute tasks
   to install Docker and Docker Compose.

## Ansible Configuration

This Ansible configuration file (ansible.cfg) sets default parameters. It specifies directories for playbooks,
inventory, and roles. Additionally, it defines default user and SSH key settings, simplifying configuration across
playbooks.

# Lab 5

## Output for docker role
```
PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
Enter passphrase for key '/home/vladimir/.ssh/id_ed25519': 
ok: [host1]

TASK [docker : Apt update] *****************************************************
changed: [host1]

TASK [docker : Installation of python3 and pip3] *******************************
changed: [host1]

TASK [docker : Installation of docker] *****************************************
changed: [host1]

TASK [docker : Installation of docker-compose] *********************************
changed: [host1]

PLAY RECAP *********************************************************************
host1                      : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

## Inventory details
```
{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_host": "158.160.62.182",
                "ansible_user": "vladimir"
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
            "host1"
        ]
    }
}
```

# Lab 6
## Output for docker and web_app role
```
PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
Enter passphrase for key '/home/vladimir/.ssh/id_ed25519': 
Enter passphrase for key '/home/vladimir/.ssh/id_ed25519': 
ok: [host1]

TASK [docker : Apt update] *****************************************************
ok: [host1]

TASK [docker : Installation of python3 and pip3] *******************************
ok: [host1]

TASK [docker : Installation of docker] *****************************************
ok: [host1]

TASK [docker : Installation of docker-compose] *********************************
ok: [host1]

TASK [web_app : Docker image pulling] ******************************************
changed: [host1]

TASK [web_app : Docker container running] **************************************
changed: [host1]

PLAY RECAP *********************************************************************
host1                      : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```