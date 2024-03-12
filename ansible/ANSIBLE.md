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

Result of `ansible-playbook playbooks/dev/main.yaml` for Lab 6
```bash
TASK [geerlingguy.docker : Add Docker repository.] *****************************
ok: [host_01]

TASK [geerlingguy.docker : Install Docker packages.] ***************************
skipping: [host_01]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
ok: [host_01]

TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
skipping: [host_01]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
ok: [host_01]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
skipping: [host_01]

TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
skipping: [host_01]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
ok: [host_01]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [host_01]

TASK [geerlingguy.docker : Get docker group info using getent.] ****************
skipping: [host_01]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [host_01]

TASK [geerlingguy.docker : include_tasks] **************************************
skipping: [host_01]

TASK [web_app : Add user to Docker group] **************************************
changed: [host_01]

TASK [web_app : Pull the Docker image] *****************************************
ok: [host_01]

TASK [web_app : Run the Docker container] **************************************
ok: [host_01]

PLAY RECAP *********************************************************************
host_01                    : ok=14   changed=1    unreachable=0    failed=0    skipped=12   rescued=0
```