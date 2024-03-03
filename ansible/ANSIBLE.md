# Ansible

> Note: The role `geerlingguy.docker` is not physically present in the
> repository. You should install it by running `ansible-galaxy install -r
> roles/requirements.yml` from the `ansible` directory.

## Best practices

1. Use FQCN for builtin module actions
1. Name the tasks and roles properly
1. Use `ansible-lint` to check the playbooks and roles for best practices.
1. Use `ansible-playbook --check --diff` to run the playbooks in check mode to
   see the changes that will be made.
1. Use `requirements.yml` to manage the roles and collections.
1. Store secrets in the environment variables.
1. Ensure the idempotentency of the tasks. Do not use moduels like `command` or
   `shell` if there are alternatives.

## CLI Outputs

### Docker Deployment

1. `ansible-playbook playbooks/dev/main.yml --diff` (with `geerlingguy.docker` role)

    ```text
    TASK [geerlingguy.docker : Install Docker packages.] ***************************
    skipping: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***
    The following additional packages will be installed:
    docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
    Suggested packages:
    aufs-tools cgroupfs-mount | cgroup-lite
    The following NEW packages will be installed:
    containerd.io docker-buildx-plugin docker-ce docker-ce-cli
    docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
    slirp4netns
    0 upgraded, 10 newly installed, 0 to remove and 38 not upgraded.
    changed: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Install docker-compose plugin.] *********************
    skipping: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
    ok: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************
    skipping: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Configure Docker daemon options.] *******************
    skipping: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******
    ok: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

    RUNNING HANDLER [geerlingguy.docker : restart docker] **************************
    changed: [yandex-cloud-vm]

    TASK [geerlingguy.docker : include_tasks] **************************************
    skipping: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Get docker group info using getent.] ****************
    skipping: [yandex-cloud-vm]

    TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
    skipping: [yandex-cloud-vm]

    TASK [geerlingguy.docker : include_tasks] **************************************
    skipping: [yandex-cloud-vm]

    PLAY RECAP *********************************************************************
    yandex-cloud-vm            : ok=12   changed=5    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
    ```

1. `ansible-inventory -i inventory/default_yandex_vm.yml --list`

    ```json
    {
        "_meta": {
            "hostvars": {
                "yandex-cloud-vm": {
                    "ansible_host": "158.160.116.203",
                    "ansible_user": "ubuntu"
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
                "yandex-cloud-vm"
            ]
        }
    }
    ```

1. `ansible-playbook -C playbooks/dev/main.yml --diff` (with custom `docker`
   role, running in check mode)

    ```text
    libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
    libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
    libgcc-9-dev libgomp1 libisl22 libitm1 liblsan0 libmpc3 libmpfr6
    libpython3-dev libpython3.8-dev libquadmath0 libstdc++-9-dev libtsan0
    libubsan1 linux-libc-dev make manpages-dev python-pip-whl python3-appdirs
    python3-dev python3-distlib python3-filelock python3-virtualenv
    python3-wheel python3.8-dev zlib1g-dev
    Suggested packages:
    binutils-doc cpp-doc gcc-9-locales debian-keyring g++-multilib
    g++-9-multilib gcc-9-doc gcc-multilib autoconf automake libtool flex bison
    gdb gcc-doc gcc-9-multilib glibc-doc bzr libstdc++-9-doc make-doc
    The following NEW packages will be installed:
    binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
    dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base libalgorithm-diff-perl
    libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan5 libatomic1
    libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
    libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
    libgcc-9-dev libgomp1 libisl22 libitm1 liblsan0 libmpc3 libmpfr6
    libpython3-dev libpython3.8-dev libquadmath0 libstdc++-9-dev libtsan0
    libubsan1 linux-libc-dev make manpages-dev python-pip-whl python3-appdirs
    python3-dev python3-distlib python3-filelock python3-pip python3-virtualenv
    python3-wheel python3.8-dev virtualenv zlib1g-dev
    0 upgraded, 56 newly installed, 0 to remove and 8 not upgraded.
    changed: [yandex-cloud-vm]

    TASK [docker : Add Docker GPG apt Key] *******************************************************
    ok: [yandex-cloud-vm]

    TASK [docker : Add Docker Repository] ********************************************************
    --- before: /dev/null
    +++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
    @@ -0,0 +1 @@
    +deb https://download.docker.com/linux/ubuntu focal stable

    changed: [yandex-cloud-vm]

    TASK [docker : Update apt and install docker-ce] *********************************************
    ok: [yandex-cloud-vm]

    TASK [docker : include_tasks] ****************************************************************
    included: /workspaces/devops/ansible/roles/docker/tasks/install_compose.yml for yandex-cloud-vm

    TASK [docker : Install docker-compose plugin] ************************************************
    skipping: [yandex-cloud-vm]

    TASK [docker : Add user to docker group] *****************************************************
    changed: [yandex-cloud-vm]

    PLAY RECAP ***********************************************************************************
    yandex-cloud-vm            : ok=9    changed=4    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
    ```

### Dynamic Inventory

For the dynamic inventory, I utilized [yacloud_compute][yacloud_compute]
inventory plugin and slightly modified it to get `yacloud_token` from the envs.
Running `ansible-inventory -e yacloud_token=... --list` gives the following
output:

```json
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "158.160.116.203",
                "yacloud_token": "..."
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
            "terraform1"
        ]
    }
}
```

[yacloud_compute]:
    https://github.com/rodion-goritskov/yacloud_compute/blob/master/yacloud_compute.py

## Web App Deployment

### Deploy

`ansible-playbook -e "yacloud_token=..." playbooks/dev/python.yml --diff`:

```text
included: /workspaces/devops/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Install docker-compose plugin] **********************************
changed: [terraform1]

TASK [docker : Add user to docker group] ***************************************
changed: [terraform1]

TASK [web_app : Deploy web application] ****************************************
included: /workspaces/devops/ansible/roles/web_app/tasks/0-deploy.yml for terraform1

TASK [web_app : Create app directory] ******************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/opt/web_app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform1]

TASK [web_app : Copy Docker Compose template] **********************************
--- before
+++ after: /home/vscode/.ansible/tmp/ansible-local-168213t94c7dpz/tmp7k2dsk0b/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: "3.9"
+
+services:
+  web:
+    image: "fedorivn/simple-web-app:python-1.0.0"
+    ports:
+      - target: "80"
+        published: "8000"

changed: [terraform1]

TASK [web_app : Ensure docker is running] **************************************
ok: [terraform1]

TASK [web_app : Create and start the services] *********************************
changed: [terraform1]

TASK [web_app : Wipe out web application] **************************************
skipping: [terraform1]

PLAY RECAP *********************************************************************
terraform1                 : ok=15   changed=8    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

Running `docker ps` on the remote machine:

```text
ubuntu@fhms2hta7o1v987i1180:~$ docker ps
CONTAINER ID   IMAGE                                  COMMAND                  CREATED          STATUS          PORTS                                   NAMES
eb439b3b2179   fedorivn/simple-web-app:python-1.0.0   "uvicorn main:app --…"   11 minutes ago   Up 11 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   web_app-web-1
```

### Wipe

`ansible-playbook -e yacloud_token=... -e web_app_full_wipe=true --tag wipe
playbooks/dev/python.yml`:

```text

PLAY [Install Docker & Deploy web application] ***********************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Wipe out web application] ****************************************************************************************************************************************
included: /workspaces/devops/ansible/roles/web_app/tasks/1-wipe.yml for terraform1

TASK [web_app : Shutdown and remove the services] ********************************************************************************************************************************
changed: [terraform1]

TASK [web_app : Remove app directory] ********************************************************************************************************************************************
changed: [terraform1]

PLAY RECAP ***********************************************************************************************************************************************************************
terraform1                 : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

Running `docker ps` on the remote machine:

```text
ubuntu@fhmu5ucf069g6cuiuhrk:~$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

### Deploy (Bonus)

`ansible-playbook -e yacloud_token=... playbooks/dev/rust.yml --diff`:

```text
PLAY [Install Docker & Deploy web application] ***********************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : include_tasks] ****************************************************************************************************************************************************
included: /workspaces/devops/ansible/roles/docker/tasks/install_docker.yml for terraform1

TASK [docker : Install aptitude] *************************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Install required system packages] *********************************************************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker GPG apt Key] *******************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker Repository] ********************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Update apt and install docker-ce] *********************************************************************************************************************************
ok: [terraform1]

TASK [docker : include_tasks] ****************************************************************************************************************************************************
included: /workspaces/devops/ansible/roles/docker/tasks/install_compose.yml for terraform1

TASK [docker : Install docker-compose plugin] ************************************************************************************************************************************
ok: [terraform1]

TASK [docker : Add user to docker group] *****************************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Deploy web application] ******************************************************************************************************************************************
included: /workspaces/devops/ansible/roles/web_app/tasks/0-deploy.yml for terraform1

TASK [web_app : Create app directory] ********************************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/opt/web_app",
-    "state": "absent"
+    "state": "directory"
 }

changed: [terraform1]

TASK [web_app : Copy Docker Compose template] ************************************************************************************************************************************
--- before
+++ after: /home/vscode/.ansible/tmp/ansible-local-2438756woxv2u6/tmpxtljgvte/docker-compose.yml.j2
@@ -0,0 +1,8 @@
+version: "3.9"
+
+services:
+  web:
+    image: "fedorivn/simple-web-app:rust-1.0.0"
+    ports:
+      - target: "80"
+        published: "8000"

changed: [terraform1]

TASK [web_app : Ensure docker is running] ****************************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Create and start the services] ***********************************************************************************************************************************
changed: [terraform1]

TASK [web_app : Wipe out web application] ****************************************************************************************************************************************
skipping: [terraform1]

PLAY RECAP ***********************************************************************************************************************************************************************
terraform1                 : ok=15   changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

### Wipe (Bonus)

`ansible-playbook -e yacloud_token=... -e web_app_full_wipe=true --tag wipe
playbooks/dev/rust.yml --diff`:

```text
PLAY [Install Docker & Deploy web application] ***********************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************************************
ok: [terraform1]

TASK [web_app : Wipe out web application] ****************************************************************************************************************************************
included: /workspaces/devops/ansible/roles/web_app/tasks/1-wipe.yml for terraform1

TASK [web_app : Shutdown and remove the services] ********************************************************************************************************************************
changed: [terraform1]

TASK [web_app : Remove app directory] ********************************************************************************************************************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "/opt/web_app",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "/opt/web_app/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [terraform1]

PLAY RECAP ***********************************************************************************************************************************************************************
terraform1                 : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
