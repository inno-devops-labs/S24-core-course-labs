# Ansible

Initially I tried `geerlingguy.docker` role, then I created my own one following
official docs.

## Best Parctices

1. Use `ansible-lint`, thus following:
    - Use `ansible.builtin` naming
    - Always mention the `state`
    - Always give `name`
2. Use `fact_caching` (see `ansible.cfg`)

## `ansible-playbook playbooks/dev/main.yml -i inventory --diff`

> Note: I have already played my playbook, so the output is trimmed because
> everything had been deployed successfully

```text
PLAY [Dev playbook] *************************************************************************************

TASK [Gathering Facts] **********************************************************************************
ok: [terraform-vm]

TASK [docker : Install Docker] **************************************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Update apt package index] ****************************************************************
changed: [terraform-vm]

TASK [docker : Install required system packages] ********************************************************
ok: [terraform-vm] => (item=apt-transport-https)
ok: [terraform-vm] => (item=ca-certificates)
ok: [terraform-vm] => (item=curl)
ok: [terraform-vm] => (item=gnupg-agent)
ok: [terraform-vm] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ***********************************************************
ok: [terraform-vm]

TASK [docker : Add Docker's official apt repository] ****************************************************
ok: [terraform-vm]

TASK [docker : Install Docker and dependencies] *********************************************************
ok: [terraform-vm] => (item=docker-ce)
ok: [terraform-vm] => (item=docker-ce-cli)
ok: [terraform-vm] => (item=containerd.io)

TASK [docker : Install Docker Compose] ******************************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install Docker Compose] ******************************************************************
ok: [terraform-vm]

PLAY RECAP **********************************************************************************************
terraform-vm               : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## `ansible-inventory -i inventory/yacloud_compute.yml --list | tail -n 50`

```text
                },
                "ansible_user_gecos": {
                    "__ansible_unsafe": "Ubuntu"
                },
                "ansible_user_gid": 1001,
                "ansible_user_id": {
                    "__ansible_unsafe": "ubuntu"
                },
                "ansible_user_shell": {
                    "__ansible_unsafe": "/bin/bash"
                },
                "ansible_user_uid": 1000,
                "ansible_userspace_architecture": {
                    "__ansible_unsafe": "x86_64"
                },
                "ansible_userspace_bits": {
                    "__ansible_unsafe": "64"
                },
                "ansible_virtualization_role": {
                    "__ansible_unsafe": "NA"
                },
                "ansible_virtualization_tech_guest": [],
                "ansible_virtualization_tech_host": [],
                "ansible_virtualization_type": {
                    "__ansible_unsafe": "NA"
                },
                "discovered_interpreter_python": {
                    "__ansible_unsafe": "/usr/bin/python3"
                },
                "gather_subset": [
                    {
                        "__ansible_unsafe": "all"
                    }
                ],
                "module_setup": true
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "yacloud"
        ]
    },
    "yacloud": {
        "hosts": [
            "terraform-vm"
        ]
    }
}
```

## `ansible-playbook playbooks/dev/app_python/main.yml -i inventory`

```text
PLAY [Deploy app_python] *********************************************************************

TASK [Gathering Facts] ***********************************************************************
ok: [terraform-vm]

TASK [docker : Install Docker] ***************************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Update apt package index] *****************************************************
changed: [terraform-vm]

TASK [docker : Install required system packages] *********************************************
ok: [terraform-vm] => (item=apt-transport-https)
ok: [terraform-vm] => (item=ca-certificates)
ok: [terraform-vm] => (item=curl)
ok: [terraform-vm] => (item=gnupg-agent)
ok: [terraform-vm] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ************************************************
ok: [terraform-vm]

TASK [docker : Add Docker's official apt repository] *****************************************
ok: [terraform-vm]

TASK [docker : Install Docker and dependencies] **********************************************
ok: [terraform-vm] => (item=docker-ce)
ok: [terraform-vm] => (item=docker-ce-cli)
ok: [terraform-vm] => (item=containerd.io)

TASK [docker : Install Docker Compose] *******************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install Docker Compose] *******************************************************
ok: [terraform-vm]

TASK [web_app : Full wipe] *******************************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for terraform-vm

TASK [web_app : Wipe images] *****************************************************************
changed: [terraform-vm]

TASK [web_app : Remove app directory] ********************************************************
changed: [terraform-vm]

TASK [web_app : Deploy dockerized app] *******************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/web_app/tasks/1-deploy.yml for terraform-vm

TASK [web_app : Create app directory] ********************************************************
changed: [terraform-vm]

TASK [web_app : Copy Docker Compose template] ************************************************
changed: [terraform-vm]

TASK [web_app : Ensure docker service is OK] *************************************************
ok: [terraform-vm]

TASK [web_app : Create and start the services] ***********************************************
changed: [terraform-vm]

PLAY RECAP ***********************************************************************************
terraform-vm               : ok=17   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## `ansible-playbook playbooks/dev/app_java/main.yml -i inventory`

```text
PLAY [Deploy app_java] ***********************************************************************

TASK [Gathering Facts] ***********************************************************************
ok: [terraform-vm]

TASK [docker : Install Docker] ***************************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform-vm

TASK [docker : Update apt package index] *****************************************************
changed: [terraform-vm]

TASK [docker : Install required system packages] *********************************************
ok: [terraform-vm] => (item=apt-transport-https)
ok: [terraform-vm] => (item=ca-certificates)
ok: [terraform-vm] => (item=curl)
ok: [terraform-vm] => (item=gnupg-agent)
ok: [terraform-vm] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ************************************************
ok: [terraform-vm]

TASK [docker : Add Docker's official apt repository] *****************************************
ok: [terraform-vm]

TASK [docker : Install Docker and dependencies] **********************************************
ok: [terraform-vm] => (item=docker-ce)
ok: [terraform-vm] => (item=docker-ce-cli)
ok: [terraform-vm] => (item=containerd.io)

TASK [docker : Install Docker Compose] *******************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform-vm

TASK [docker : Install Docker Compose] *******************************************************
ok: [terraform-vm]

TASK [web_app : Full wipe] *******************************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/web_app/tasks/0-wipe.yml for terraform-vm

TASK [web_app : Wipe images] *****************************************************************
ok: [terraform-vm]

TASK [web_app : Remove app directory] ********************************************************
changed: [terraform-vm]

TASK [web_app : Deploy dockerized app] *******************************************************
included: /home/dmfrpro/Projects/S24-core-course-labs/ansible/roles/web_app/tasks/1-deploy.yml for terraform-vm

TASK [web_app : Create app directory] ********************************************************
changed: [terraform-vm]

TASK [web_app : Copy Docker Compose template] ************************************************
changed: [terraform-vm]

TASK [web_app : Ensure docker service is OK] *************************************************
ok: [terraform-vm]

TASK [web_app : Create and start the services] ***********************************************
changed: [terraform-vm]

PLAY RECAP ***********************************************************************************
terraform-vm               : ok=17   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## `sudo docker ps` on remote host

```bash
ubuntu@epdbkrfvkblikpr8veg4:~$ sudo docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED              STATUS              PORTS                                       NAMES
8821bc5bbed1   dmfrpro/app_java:latest     "/__cacert_entrypoin…"   24 seconds ago       Up 22 seconds       0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   app_java-web-1
baae28c2c2d2   dmfrpro/app_python:latest   "sh -c 'python3 -m g…"   About a minute ago   Up About a minute   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   app_python-web-1
```

## `curl localhost:port` on remote host

```bash
ubuntu@epdbkrfvkblikpr8veg4:~$ curl localhost:8080
<!DOCTYPE html>
<html>
<head>
    <title>Current Time in Moscow</title>
</head>
<body>
    <h1>Current Time in Moscow:</h1>
    <p>2024-03-10 16:06:56.007010+03:00</p>
</body>
</html>ubuntu@epdbkrfvkblikpr8veg4:~$ curl localhost:8000
<!DOCTYPE html>
<html>
<head>
    <title>Current Time in Samara</title>
</head>
<body>
<h1>Current Time in Samara:</h1>
<p>2024-03-10 17:06:59</p>
</body>
</html>
ubuntu@epdbkrfvkblikpr8veg4:~$ 
```
