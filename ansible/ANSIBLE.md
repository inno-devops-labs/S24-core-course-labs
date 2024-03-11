# Ansible

## Command Executions

``ansible-playbook playbooks/dev/main.yml --diff``

```console
ansible-playbook playbooks/dev/main.yml --diff

PLAY [Install Docker] **************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [terraform1]

TASK [docker : Update apt cache] ***************************************************************************************
changed: [terraform1]

TASK [docker : Install pip] ********************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker dependencies] ****************************************************************************
ok: [terraform1] => (item=apt-transport-https)
ok: [terraform1] => (item=ca-certificates)
ok: [terraform1] => (item=curl)
ok: [terraform1] => (item=gnupg-agent)
ok: [terraform1] => (item=software-properties-common)

TASK [docker : Remove conflicting Docker GPG keys] *********************************************************************
ok: [terraform1]

TASK [docker : Clear APT cache] ****************************************************************************************
ok: [terraform1]

TASK [docker : Create directory for apt keyrings] **********************************************************************
ok: [terraform1]

TASK [docker : Download Docker GPG key] ********************************************************************************
changed: [terraform1]

TASK [docker : Add Docker GPG key] *************************************************************************************
changed: [terraform1]

TASK [docker : Set permissions for Docker GPG key] *********************************************************************
ok: [terraform1]

TASK [docker : Ensure correct Docker repository configuration] *********************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [terraform1]

TASK [docker : Install Docker] *****************************************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 18 not upgraded.
changed: [terraform1]

TASK [docker : Install Docker Compose] *********************************************************************************
changed: [terraform1]

TASK [docker : Add Docker GPG key] *************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker repository] **********************************************************************************
ok: [terraform1]

TASK [docker : Install Docker] *****************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker Compose] *********************************************************************************
ok: [terraform1]

PLAY RECAP *************************************************************************************************************
terraform1                 : ok=17   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

``ansible-inventory -i inventory/yandex_cloud.yml --list``

```console
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "62.84.114.89",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "myhosts",
            "ungrouped"
        ]
    },
    "myhosts": {
        "hosts": [
            "terraform1"
        ]
    }
}
```

``terraform1`` is our Yandex Cloud host.

``ansible-playbook playbooks/dev/app_python/main.yml --diff``

```console
ansible-playbook playbooks/dev/app_python/main.yml --diff

PLAY [Ansible-Python] **************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker] *****************************************************************************************
included: /mnt/c/Users/evsey/InnopolisUniversity/Labs/Y3T2/Devops/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Install aptitude] ***************************************************************************************
ok: [terraform1]

TASK [docker : Install required system packages] ***********************************************************************
ok: [terraform1]

TASK [docker : Add Docker Repository] **********************************************************************************
ok: [terraform1]

TASK [docker : Update apt and install docker-ce] ***********************************************************************
ok: [terraform1]

TASK [docker : Install docker-compose] *********************************************************************************
included: /mnt/c/Users/evsey/InnopolisUniversity/Labs/Y3T2/Devops/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Install docker-compose plugin] **************************************************************************
ok: [terraform1]

TASK [docker : Add user to docker group] *******************************************************************************
ok: [terraform1]

TASK [web_app : Wipe images] *******************************************************************************************
skipping: [terraform1]

TASK [web_app : Remove app directory] **********************************************************************************
skipping: [terraform1]

TASK [web_app : Create app directory] **********************************************************************************
--- before
+++ after
@@ -1,5 +1,5 @@
 {
-    "group": 0,
-    "owner": 0,
+    "group": 1001,
+    "owner": 1000,
     "path": "/opt/app_python/"
 }

changed: [terraform1]

TASK [web_app : Copy Docker Compose template] **************************************************************************
--- before
+++ after: /home/aidenrockwell/.ansible/tmp/ansible-local-1407mk5oq96h/tmpba29tte5/docker-compose.yml.j2
@@ -0,0 +1,9 @@
+version: "3.9"
+
+services:
+  'app_python':
+    image:  'docker.io/evsey/flask-moscow-time-app:latest'
+    restart: always
+    container_name: 'app_python'
+    ports:
+        - '8000:3000'
\ No newline at end of file

changed: [terraform1]

TASK [web_app : Ensure docker service is OK] ***************************************************************************
ok: [terraform1]

TASK [web_app : Pull images] *******************************************************************************************
changed: [terraform1]

PLAY RECAP *************************************************************************************************************
terraform1                 : ok=13   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

```

``ansible-playbook playbooks/dev/app_nodejs/main.yml --diff``

```console
ansible-playbook playbooks/dev/app_nodejs/main.yml --diff

PLAY [Ansible-NodeJS] **************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
Enter passphrase for key '/home/aidenrockwell/.ssh/id_rsa':
ok: [terraform1]

TASK [docker : Install Docker] *****************************************************************************************
included: /mnt/c/Users/evsey/InnopolisUniversity/Labs/Y3T2/Devops/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Install aptitude] ***************************************************************************************
ok: [terraform1]

TASK [docker : Install required system packages] ***********************************************************************
ok: [terraform1]

TASK [docker : Add Docker Repository] **********************************************************************************
ok: [terraform1]

TASK [docker : Update apt and install docker-ce] ***********************************************************************
ok: [terraform1]

TASK [docker : Install docker-compose] *********************************************************************************
included: /mnt/c/Users/evsey/InnopolisUniversity/Labs/Y3T2/Devops/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Install docker-compose plugin] **************************************************************************
ok: [terraform1]

TASK [docker : Add user to docker group] *******************************************************************************
ok: [terraform1]

TASK [web_app : Wipe images] *******************************************************************************************
skipping: [terraform1]

TASK [web_app : Remove app directory] **********************************************************************************
skipping: [terraform1]

TASK [web_app : Create app directory] **********************************************************************************
--- before
+++ after
@@ -1,5 +1,5 @@
 {
-    "group": 0,
-    "owner": 0,
+    "group": 1001,
+    "owner": 1000,
     "path": "/opt/app_nodejs/"
 }

changed: [terraform1]

TASK [web_app : Copy Docker Compose template] **************************************************************************
--- before
+++ after: /home/aidenrockwell/.ansible/tmp/ansible-local-1534z30ooxue/tmpi5q3u9vf/docker-compose.yml.j2
@@ -0,0 +1,9 @@
+version: "3.9"
+
+services:
+  'app_nodejs':
+    image:  'docker.io/evsey/node-world-clock-app:latest'
+    restart: always
+    container_name: 'app_nodejs'
+    ports:
+        - '8001:3000'
\ No newline at end of file

changed: [terraform1]

TASK [web_app : Ensure docker service is OK] ***************************************************************************
ok: [terraform1]

TASK [web_app : Pull images] *******************************************************************************************
changed: [terraform1]

PLAY RECAP *************************************************************************************************************
terraform1                 : ok=13   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```