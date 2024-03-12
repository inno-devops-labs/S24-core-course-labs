# Ansible

```bash
ansible-playbook playbooks/dev/main.yaml --diff -i inventory/default_aws_ec2.yml
```

```bash
PLAY [Dev playbook] *************************************************************

TASK [Gathering Facts] **********************************************************
ok: [host_01]

TASK [docker : Install `pip`] ***************************************************
The following additional packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-wheel python3.10-dev rpcsvc-proto
  zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc

PLAY [Dev playbook] *************************************************************

TASK [Gathering Facts] **********************************************************
ok: [host_01]

TASK [docker : Install `pip`] ***************************************************
The following additional packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-wheel python3.10-dev rpcsvc-proto
  zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
The following NEW packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
- name: Install required system packages
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-pip python3-wheel python3.10-dev
  rpcsvc-proto zlib1g-dev
0 upgraded, 64 newly installed, 0 to remove and 0 not upgraded.
changed: [host_01]

TASK [docker : Install required system packages] ********************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

TASK [docker : Add Docker GPG key] **********************************************
changed: [host_01]

TASK [docker : Add Docker Repository] *******************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc
The following NEW packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-pip python3-wheel python3.10-dev
  rpcsvc-proto zlib1g-dev
0 upgraded, 64 newly installed, 0 to remove and 0 not upgraded.
changed: [host_01]

TASK [docker : Install required system packages] ********************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

TASK [docker : Add Docker GPG key] **********************************************
changed: [host_01]

TASK [docker : Add Docker Repository] *******************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable

changed: [host_01]

TASK [docker : Install Docker] **************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
  rpcsvc-proto zlib1g-dev
0 upgraded, 64 newly installed, 0 to remove and 0 not upgraded.
changed: [host_01]

TASK [docker : Install required system packages] ********************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

TASK [docker : Add Docker GPG key] **********************************************
changed: [host_01]

TASK [docker : Add Docker Repository] *******************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable

changed: [host_01]

TASK [docker : Install Docker] **************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

TASK [docker : Install Docker Compose] ******************************************
The following additional packages will be installed:
  python3-docker python3-dockerpty python3-docopt python3-dotenv
  python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-texttable python3-websocket
0 upgraded, 7 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

PLAY RECAP **********************************************************************
host_01                    : ok=7    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable

changed: [host_01]

TASK [docker : Install Docker] **************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

TASK [docker : Install Docker Compose] ******************************************
The following additional packages will be installed:
  python3-docker python3-dockerpty python3-docopt python3-dotenv
  python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-texttable python3-websocket
0 upgraded, 7 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

PLAY RECAP **********************************************************************
host_01                    : ok=7    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

```bash
ansible-inventory -i inventory/default_aws_ec2.yml --list
```

```json
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "51.250.72.152",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "my_hosts"
        ]
    },
    "my_hosts": {
        "hosts": [
            "host_01"
        ]
    }
}
```



```bash
yaroslav@xiaomao ~/S/D/d/ansible (lab6)> ansible-playbook playbooks/dev/app_python/main.yaml --diff -i inventory/default_aws_ec2.yml --private-key ~/.ssh/yandex_cloud

PLAY [Deploy app_python] *******************************************************

TASK [Gathering Facts] *********************************************************
ok: [host_01]

TASK [docker : Install `pip`] **************************************************
ok: [host_01]

TASK [docker : Install required system packages] *******************************
^C [ERROR]: User interrupted execution
yaroslav@xiaomao ~/S/D/d/ansible (lab6) [99]> vim playbooks/dev/app_python/main.yaml 
yaroslav@xiaomao ~/S/D/d/ansible (lab6)> vim playbooks/dev/app_scala/main.yaml 
yaroslav@xiaomao ~/S/D/d/ansible (lab6)> ansible-playbook playbooks/dev/app_python/main.yaml --diff -i inventory/default_aws_ec2.yml --private-key ~/.ssh/yandex_cloud

PLAY [Deploy app_python] *******************************************************

TASK [Gathering Facts] *********************************************************
ok: [host_01]

TASK [docker : Install `pip`] **************************************************
ok: [host_01]

TASK [docker : Install required system packages] *******************************
ok: [host_01]

TASK [docker : Add Docker GPG key] *********************************************
ok: [host_01]

TASK [docker : Add Docker Repository] ******************************************
ok: [host_01]

TASK [docker : Install Docker] *************************************************
ok: [host_01]

TASK [docker : Install Docker Compose] *****************************************
ok: [host_01]

TASK [web_app : Full wipe] *****************************************************
included: /home/yaroslav/Study/DevOps/dev-ops-course/ansible/roles/web_app/tasks/0-wipe.yml for host_01

TASK [web_app : Clean up docker compose project] *******************************
changed: [host_01]

TASK [web_app : Clean up project files] ****************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "app_python/",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "app_python/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [host_01]

TASK [web_app : Create app directory] ******************************************
--- before
+++ after
@@ -1,6 +1,6 @@
 {
-    "group": 0,
-    "owner": 0,
+    "group": 1001,
+    "owner": 1000,
     "path": "app_python",
-    "state": "absent"
+    "state": "directory"
 }

changed: [host_01]

TASK [web_app : Copy Docker Compose template] **********************************
--- before
+++ after: /home/yaroslav/.ansible/tmp/ansible-local-555553b0z_q2_/tmp8776wn9r/docker-compose.yml.j2
@@ -0,0 +1,7 @@
+services:
+  web_app:
+    image: "catdog905/dev-ops-terraform-exercize-app-python:lab5"
+    ports:
+      - "80:80"
+    environment:
+      - SECRET_KEY="QCY?tAnfk?aZ?iwrNwnxIlR6CTf:G3gf:90Latabg@5241AB`R5W:1uDFN];Ik@n"

changed: [host_01]

TASK [web_app : Create and start the services] *********************************
changed: [host_01]

PLAY RECAP *********************************************************************
host_01                    : ok=13   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

yaroslav@xiaomao ~/S/D/d/ansible (lab6)> ansible-playbook playbooks/dev/app_scala/main.yaml --diff -i inventory/default_aws_ec2.yml --private-key ~/.ssh/yandex_cloud

PLAY [Deploy app_scala] ********************************************************

TASK [Gathering Facts] *********************************************************
ok: [host_01]

TASK [docker : Install `pip`] **************************************************
ok: [host_01]

TASK [docker : Install required system packages] *******************************
ok: [host_01]

TASK [docker : Add Docker GPG key] *********************************************
ok: [host_01]

TASK [docker : Add Docker Repository] ******************************************
ok: [host_01]

TASK [docker : Install Docker] *************************************************
ok: [host_01]

TASK [docker : Install Docker Compose] *****************************************
ok: [host_01]

TASK [web_app : Full wipe] *****************************************************
included: /home/yaroslav/Study/DevOps/dev-ops-course/ansible/roles/web_app/tasks/0-wipe.yml for host_01

TASK [web_app : Clean up docker compose project] *******************************
changed: [host_01]

TASK [web_app : Clean up project files] ****************************************
--- before
+++ after
@@ -1,10 +1,4 @@
 {
     "path": "app_scala/",
-    "path_content": {
-        "directories": [],
-        "files": [
-            "app_scala/docker-compose.yml"
-        ]
-    },
-    "state": "directory"
+    "state": "absent"
 }

changed: [host_01]

TASK [web_app : Create app directory] ******************************************
--- before
+++ after
@@ -1,6 +1,6 @@
 {
-    "group": 0,
-    "owner": 0,
+    "group": 1001,
+    "owner": 1000,
     "path": "app_scala",
-    "state": "absent"
+    "state": "directory"
 }

changed: [host_01]

TASK [web_app : Copy Docker Compose template] **********************************
--- before
+++ after: /home/yaroslav/.ansible/tmp/ansible-local-55781ea5grl3u/tmprhu3ejui/docker-compose.yml.j2
@@ -0,0 +1,7 @@
+services:
+  web_app:
+    image: "catdog905/dev-ops-terraform-exercize-app-scala:lab5"
+    ports:
+      - "9000:9000"
+    environment:
+      - SECRET_KEY="QCY?tAnfk?aZ?iwrNwnxIlR6CTf:G3gf:90Latabg@5241AB`R5W:1uDFN];Ik@n"

changed: [host_01]

TASK [web_app : Create and start the services] *********************************
changed: [host_01]

PLAY RECAP *********************************************************************
host_01                    : ok=13   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
