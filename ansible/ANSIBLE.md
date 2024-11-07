# Ansible Documentation

_Note: 'docker' role is the existing `geerlingguy.docker' role, that I used first. My custom role is under 'mine docker' name._

## Playbook Execution

### Command
```bash
$ ansible-playbook ansible/playbooks/dev/main.yaml --diff

PLAY [Deploy Docker] ***********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [../../roles/mine docker : Install Docker] ********************************
included: /mnt/c/users/arina/OneDrive/Рабочий стол/iu/devOps/S24-core-course-labs-Zavelevich/ansible/roles/mine docker/tasks/install_docker.yml for localhost

TASK [../../roles/mine docker : Install Docker dependencies] *******************
ok: [localhost] => (item=apt-transport-https)
ok: [localhost] => (item=ca-certificates)
ok: [localhost] => (item=curl)
ok: [localhost] => (item=software-properties-common)

TASK [../../roles/mine docker : Add Docker GPG apt Key] ************************
ok: [localhost]

TASK [../../roles/mine docker : Add Docker Repository] *************************
ok: [localhost]

TASK [../../roles/mine docker : Install Docker] ********************************
ok: [localhost]

TASK [../../roles/mine docker : Ensure Docker service is started and enabled] ***
ok: [localhost]

TASK [../../roles/mine docker : Install Docker Compose] ************************
included: /mnt/c/users/arina/OneDrive/Рабочий стол/iu/devOps/S24-core-course-labs-Zavelevich/ansible/roles/mine docker/tasks/install_compose.yml for localhost

TASK [../../roles/mine docker : Install pip3] **********************************
ok: [localhost]

TASK [../../roles/mine docker : Install Docker Compose] ************************
The following additional packages will be installed:
  python3-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-compose python3-docker python3-dockerpty
  python3-docopt python3-dotenv python3-texttable python3-websocket
0 upgraded, 8 newly installed, 0 to remove and 0 not upgraded.
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=10   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

```bash 
$ ansible-inventory -i ansible/inventory/default_yandex_cloud.yml --list
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    }
}
```
Inventory is empty because the deployment is local.