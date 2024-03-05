# Ansible Docker Deployment

This is a simple Ansible playbook to install Docker and Docker Compose on a target machine using custom role `docker`.

## Directory Structure
```bash
.
├── ansible.cfg
├── ANSIBLE.md
├── inventory
│   └── defaults_yc.yaml
├── playbooks
│   └── dev
│       └── main.yaml
└── roles
    ├── docker
    │   ├── defaults
    │   │   └── main.yaml
    │   ├── handlers
    │   │   └── main.yaml
    │   ├── README.md
    │   └── tasks
    │       ├── install_compose.yaml
    │       ├── install_docker.yaml
    │       └── main.yaml
    └── web_app
        ├── defaults
        │   └── main.yaml
        ├── handlers
        │   └── main.yaml
        ├── meta
        │   └── main.yaml
        ├── tasks
        │   └── main.yaml
        └── templates
            └── docker-compose.yaml.j2

```

## Deployment Output
```bash
PLAY [Install Docker and Docker Compose] ***************************************

TASK [Gathering Facts] *********************************************************
ok: [158.160.146.176]

TASK [docker : Install Docker] *************************************************
included: /home/slrypc/Study/devops-2024/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yaml for 158.160.146.176

TASK [docker : Install Dependencies] *******************************************
ok: [158.160.146.176] => (item=apt-transport-https)
ok: [158.160.146.176] => (item=ca-certificates)
ok: [158.160.146.176] => (item=curl)
ok: [158.160.146.176] => (item=gnupg-agent)
ok: [158.160.146.176] => (item=software-properties-common)

TASK [docker : Add Docker GPG Key] *********************************************
ok: [158.160.146.176]

TASK [docker : Add Docker Repository] ******************************************
ok: [158.160.146.176]

TASK [docker : Install Docker] *************************************************
ok: [158.160.146.176] => (item=docker-ce)
ok: [158.160.146.176] => (item=docker-ce-cli)
ok: [158.160.146.176] => (item=containerd.io)

TASK [docker : Check Docker Status] ********************************************
ok: [158.160.146.176]

TASK [docker : Ensure "docker" group exists] ***********************************
ok: [158.160.146.176]

TASK [docker : Add user to "docker" group] *************************************
ok: [158.160.146.176]

TASK [docker : Install Docker Compose] *****************************************
included: /home/slrypc/Study/devops-2024/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yaml for 158.160.146.176

TASK [docker : Install pip] ****************************************************
ok: [158.160.146.176]

TASK [docker : Install Docker Compose] *****************************************
ok: [158.160.146.176]

PLAY RECAP *********************************************************************
158.160.146.176            : ok=12   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Inventory Details
```json
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
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped",
            "vms"
        ]
    },
    "vms": {
        "hosts": [
            "158.160.146.176"
        ]
    }
}
```
