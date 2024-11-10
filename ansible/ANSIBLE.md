# Ansible lab

## Command output for docker role

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

## Command output for web_app role

### ansible-playbook playbooks/dev/main.yml --diff

```
PLAY [Install flask time server] **************************************************

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
ok: [default_host]

TASK [web_app : Create app directory] *********************************************
ok: [default_host]

TASK [web_app : Docker compose] ***************************************************
--- before
+++ after: /home/qexik/.ansible/tmp/ansible-local-52812vb7z8_f/tmpl1bhyw13/docker-compose.yml.j2
@@ -0,0 +1,6 @@
+services:
+  web_app:
+    image: qexik1/flask-time-server:latest
+    ports:
+      - 5000:5000
+

changed: [default_host]

TASK [web_app : Start the app] ****************************************************
changed: [default_host]

TASK [web_app : Remove build] *****************************************************
skipping: [default_host]

TASK [web_app : Remove source] ****************************************************
skipping: [default_host]

PLAY RECAP ************************************************************************
default_host               : ok=11   changed=2    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```
