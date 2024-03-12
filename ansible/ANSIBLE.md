
# Console Outputs

## Docker Deployment
> Using custom docker role
```console
$ ansible-playbook playbooks/dev/main.yml --diff | tail -50
PLAY [Install Docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_cloud_vm]

TASK [docker : Install Docker] *************************************************
included: /home/nabuki/repos/study/devops-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_cloud_vm

TASK [docker : Install aptitude] ***********************************************
ok: [yandex_cloud_vm]

TASK [docker : Install required system packages] *******************************
ok: [yandex_cloud_vm]

TASK [docker : Add Docker GPG apt Key] *****************************************
changed: [yandex_cloud_vm]

TASK [docker : Add Docker Repository] ******************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu focal stable

changed: [yandex_cloud_vm]

TASK [docker : Update apt and install docker-ce] *******************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 3 not upgraded.
changed: [yandex_cloud_vm]

TASK [docker : Install docker-compose] *****************************************
included: /home/nabuki/repos/study/devops-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_cloud_vm

TASK [docker : Install docker-compose] *****************************************
changed: [yandex_cloud_vm]

TASK [docker : Add user to docker group] ***************************************
changed: [yandex_cloud_vm]

PLAY RECAP *********************************************************************
yandex_cloud_vm            : ok=10   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Web App Deployment

```console
$ ansible-playbook playbooks/dev/main.yml --diff | tail -50

TASK [docker : Install docker-compose] *****************************************
included: /home/nabuki/repos/study/devops-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_cloud_vm

TASK [docker : Install docker-compose] *****************************************
changed: [yandex_cloud_vm]

TASK [docker : Add user to docker group] ***************************************
changed: [yandex_cloud_vm]

TASK [web_app : Deploy web application] ****************************************
included: /home/nabuki/repos/study/devops-labs/ansible/roles/web_app/tasks/0-deploy.yml for yandex_cloud_vm

TASK [web_app : Create app directory] ******************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/opt/web_app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [yandex_cloud_vm]

TASK [web_app : Render docker-compose.yml] *************************************
--- before
+++ after: /home/nabuki/.ansible/tmp/ansible-local-1548458o4o253r/tmpv19ymu7v/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+version: "3.9"
+
+services:
+  web_app:
+    image: "nabuki/moscowtime-web:latest"
\ No newline at end of file

changed: [yandex_cloud_vm]

TASK [web_app : Ensure docker is running] **************************************
ok: [yandex_cloud_vm]

TASK [web_app : Create and start the services] *********************************
changed: [yandex_cloud_vm]

TASK [web_app : Wipe out web application] **************************************
skipping: [yandex_cloud_vm]

PLAY RECAP *********************************************************************
yandex_cloud_vm            : ok=15   changed=10   unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

```

## Inventory

### Details

Inventory is simple static defined

### Console Output

```console
$ ansible-inventory -i inventory/main.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex_cloud_vm": {
                "ansible_host": "51.250.14.193"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "yandex_cloud_vm"
        ]
    }
}
```

