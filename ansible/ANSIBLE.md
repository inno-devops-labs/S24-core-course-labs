# Ansible


Result of `ansible-playbook playbooks/dev/main.yaml --diff`
```bash
PLAY [Install Docker using existing role] **************************************

TASK [Gathering Facts] *********************************************************
ok: [host_01]

TASK [docker : include_tasks] **************************************************
included: /Users/nad/S24-DevOps/ansible/roles/docker/tasks/install_docker.yml for host_01

TASK [docker : Install pip] ****************************************************
ok: [host_01]

TASK [docker : Install required system packages] *******************************
ok: [host_01]

TASK [docker : Add Docker GPG apt Key] *****************************************
ok: [host_01]

TASK [docker : Add Docker Repository] ******************************************
ok: [host_01]

TASK [docker : Update apt cache and install docker-ce] *************************
ok: [host_01]

TASK [docker : Add user to docker group] ***************************************
ok: [host_01]

TASK [docker : include_tasks] **************************************************
included: /Users/nad/S24-DevOps/ansible/roles/docker/tasks/install_compose.yml for host_01

TASK [docker : Install Docker Compose using pip] *******************************
ok: [host_01]

PLAY RECAP *********************************************************************
host_01                    : ok=10   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

Result of `ansible-inventory -i inventory --list`
```bash
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "158.160.54.22",
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
            "host_01"
        ]
    }
}
```