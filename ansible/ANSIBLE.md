# Ansible lab

## Command output

### ansible-playbook playbooks/dev/main.yml --diff

```
PLAY [Install Docker] *************************************************************

TASK [Gathering Facts] ************************************************************
[WARNING]: Platform linux on host default_host is using the discovered Python
interpreter at /usr/bin/python3.12, but future installation of another Python
interpreter could change the meaning of that path. See
https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [default_host]

TASK [docker : include_tasks] *****************************************************
included: /home/qexik/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for default_host

TASK [docker : Install apt dependencies] ******************************************
ok: [default_host]

TASK [docker : Add Docker’s GPG key] **********************************************
ok: [default_host]

TASK [docker : Add Docker apt repository] *****************************************
ok: [default_host]

TASK [docker : Install Docker] ****************************************************
ok: [default_host]

TASK [docker : include_tasks] *****************************************************
included: /home/qexik/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for default_host

TASK [docker : Install compose via apt] *******************************************
The following additional packages will be installed:
  python3-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-packaging python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-compose python3-docker python3-dockerpty
  python3-docopt python3-dotenv python3-packaging python3-texttable
  python3-websocket
0 upgraded, 9 newly installed, 0 to remove and 17 not upgraded.
changed: [default_host]

PLAY RECAP ************************************************************************
default_host               : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### ansible-inventory -i inventory/default_yandex_compute.yml --list

```
{
    "_meta": {
        "hostvars": {
            "default_host": {
                "ansible_host": "89.169.138.171",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "myhosts"
        ]
    },
    "myhosts": {
        "hosts": [
            "default_host"
        ]
    }
}
```
