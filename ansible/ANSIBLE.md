# Ansible Deployment

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
│       ├── app_python
│       │   └── main.yaml
│       └── app_typescript
│           └── main.yaml
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
        │   ├── 0-wipe.yaml
        │   └── main.yaml
        └── templates
            └── docker-compose.yaml.j2
```

## Docker Deployment Output
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

## Web App Deployment Output
```bash
PLAY [Deploy Python App] *******************************************************

TASK [Gathering Facts] *********************************************************
ok: [158.160.151.174]

TASK [docker : Install Docker] *************************************************
included: /home/slrypc/Study/devops-2024/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yaml for 158.160.151.174

TASK [docker : Install Dependencies] *******************************************
ok: [158.160.151.174] => (item=apt-transport-https)
ok: [158.160.151.174] => (item=ca-certificates)
ok: [158.160.151.174] => (item=curl)
ok: [158.160.151.174] => (item=gnupg-agent)
ok: [158.160.151.174] => (item=software-properties-common)

TASK [docker : Add Docker GPG Key] *********************************************
ok: [158.160.151.174]

TASK [docker : Add Docker Repository] ******************************************
ok: [158.160.151.174]

TASK [docker : Install Docker] *************************************************
ok: [158.160.151.174] => (item=docker-ce)
ok: [158.160.151.174] => (item=docker-ce-cli)
ok: [158.160.151.174] => (item=containerd.io)

TASK [docker : Check Docker Status] ********************************************
ok: [158.160.151.174]

TASK [docker : Ensure "docker" group exists] ***********************************
ok: [158.160.151.174]

TASK [docker : Add user to "docker" group] *************************************
ok: [158.160.151.174]

TASK [docker : Install Docker Compose] *****************************************
included: /home/slrypc/Study/devops-2024/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yaml for 158.160.151.174

TASK [docker : Install pip] ****************************************************
ok: [158.160.151.174]

TASK [docker : Install Docker Compose] *****************************************
ok: [158.160.151.174]

TASK [web_app : Docker compose down, remove app directory] *********************
included: /home/slrypc/Study/devops-2024/S24-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yaml for 158.160.151.174

TASK [web_app : Check if App directory exists] *********************************
ok: [158.160.151.174]

TASK [web_app : Check if docker-compose.yaml exists] ***************************
ok: [158.160.151.174]

TASK [web_app : Docker Compose Down] *******************************************
skipping: [158.160.151.174]

TASK [web_app : Remove App directory] ******************************************
skipping: [158.160.151.174]

TASK [web_app : Remove Docker Images] ******************************************
ok: [158.160.151.174]

TASK [web_app : Create App directory] ******************************************
ok: [158.160.151.174]

TASK [web_app : Copy template file] ********************************************
--- before
+++ after: /home/slrypc/.ansible/tmp/ansible-local-689004csjss22v/tmpt_bihe4i/docker-compose.yaml.j2
@@ -0,0 +1,6 @@
+version: '3'
+services:
+  app:
+    image: 'slry/python_moscow_time:latest'
+    ports:
+      - '8081:8080'

changed: [158.160.151.174]

TASK [web_app : Docker Compose Up] *********************************************
ok: [158.160.151.174]

PLAY RECAP *********************************************************************
158.160.151.174            : ok=19   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
```

