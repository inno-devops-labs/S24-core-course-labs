# Ansible

## Best practices 
In my implementation I applied the following best practices:
* files and folder structure: I structured my files as provided in the task;
* specification of hosts: instead of using `hosts: all` I specified host;
* configuration of global settings: I set all needed global setting in `ansible.cfg`;
* well-documented;
* implementation is simple as possible.

## Workflow
I followed the following workflow:
* structure your folders;
* add public ssh key to your server;
* check if server is up;
* specify `ansible_host` and `ansible_user` in `inventory/default_aws_ec2.yml`;
* add `defaults/main.yml` and `handlers/main.yml` and in the [template](https://github.com/geerlingguy/ansible-role-docker);
* implement `tasks/install_compose.yml` which installs Docker-Compose using `pip`;
* implement `tasks/install_docker.yml` which installs Docker using `apt`;
* implement `tasks/main.yml` which updates `apt`, installs `python3` and `python3-pip` and runs all previous tasks;
* configure settings in `ansible.cfg` for your role;
* specify `playbooks/dev/main.yml` which runs on specific host and your role;
* run and test role.

## Outputs
Output of the `ansible-playbook playbooks/dev/main.yaml --diff` command:
```commandline
yegor@yegor:~/devops/S24-Devops-core-course-labs/ansible$ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [web_server] **************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************
ok: [web_server]

TASK [docker : Update apt] *****************************************************************************************
changed: [web_server]

TASK [docker : Python3 and pip3 installation] **********************************************************************
The following NEW packages will be installed:
  python3-pip
0 upgraded, 1 newly installed, 0 to remove and 2 not upgraded.
changed: [web_server]

TASK [docker : Docker installation] ********************************************************************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base libidn11 pigz runc
  ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io libidn11 pigz
  runc ubuntu-fan
Preconfiguring packages ...
0 upgraded, 9 newly installed, 0 to remove and 2 not upgraded.
changed: [web_server]

TASK [docker : Docker-compose installation] ************************************************************************
ok: [web_server]

PLAY RECAP *********************************************************************************************************
web_server                 : ok=5    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

Output of the `ansible-inventory -i inventory/default_aws_ec2.yml --list` command:
```commandline
yegor@yegor:~/devops/S24-Devops-core-course-labs/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "3.64.165.68",
                "ansible_user": "ubuntu"
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
