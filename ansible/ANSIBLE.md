# ANSIBLE

## 1. INSTALLING DOCKER ROLE

```bash
ansible-galaxy role install geerlingguy.docker
```

## 2. ANSIBLE INVENTORY

```bash
ansible-inventory --list
```

Output:  
```
{
    "_meta": {
        "hostvars": {
            "ec2-3-71-79-119.eu-central-1.compute.amazonaws.com": {
                "ansible_connection": "ssh",
                "ansible_ssh_private_key_file": "~/.ssh/ansible-docker.pem",
                "ansible_user": "ubuntu",
                "docker_user": "ubuntu"
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
            "ec2-3-71-79-119.eu-central-1.compute.amazonaws.com"
        ]
    }
}
```

## 3. RUNNING ANSIBLE

```bash
ansible-playbook playbook/dev/main.yaml --diff
```

Output:  

```
(venv) tanmay@tanmay-ubuntu:~/Tanmay/Courses/Devops/S24-core-course-labs/ansible$ ansible-playbook playbook/dev/main.yaml --diff

PLAY [Install Docker and Docker Compose] *********************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************
ok: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install pip] **********************************************************************************************************************************
fatal: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]: FAILED! => {"changed": false, "msg": "No package matching 'python3-pip' is available"}

PLAY RECAP ***************************************************************************************************************************************************
ec2-3-71-79-119.eu-central-1.compute.amazonaws.com : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

(venv) tanmay@tanmay-ubuntu:~/Tanmay/Courses/Devops/S24-core-course-labs/ansible$ ansible-playbook playbook/dev/main.yaml --diff

PLAY [Install Docker and Docker Compose] *********************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************
ok: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : APT Update] ***********************************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install pip] **********************************************************************************************************************************
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
0 upgraded, 64 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install Docker dependencies] ******************************************************************************************************************
The following NEW packages will be installed:
  apt-transport-https gnupg-agent
0 upgraded, 2 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Add Docker's official GPG key] ****************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Add Docker's APT repository] ******************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable

changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install Docker] *******************************************************************************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install Docker Compose via pip] ***************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

RUNNING HANDLER [docker : Ensure ubuntu has Docker group access] *********************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

RUNNING HANDLER [docker : Restart Docker] ********************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

PLAY RECAP ***************************************************************************************************************************************************
ec2-3-71-79-119.eu-central-1.compute.amazonaws.com : ok=10   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## 4. Custom ```web_app``` Role

A custom web_app role is created to deploy the web applications on Amazon AWS EC2 instances. This role uses docker compose to run the web app, the docker image is pulled from docker hub.

```playbooks/dev/app_python/main.yml```:
```
---
- name: Deploy web app
  hosts: app_server_python
  roles: 
  - role: web_app
    become: true
    vars:
      app_name: "app_python"
      app_port: 5000
      app_dir: "/home/{{ ansible_user }}/{{ app_name }}"
      host_name: "{{ ansible_host }}"
      web_app_full_wipe: true
```

#### Usage

To deploy the web app:
```
ansible-playbook playbooks/dev/app_python/main.yml
```

To wipe the web app:
```
ansible-playbook playbooks/dev/app_bun/main.yml --extra-vars "web_app_full_wipe=true" --tags "wipe"
```

#### Output
Running ansible-playbook playbooks/dev/app_python/main.yml --diff gives me the following output (last 50 lines):
```

TASK [web_app : Remove compose file] ****************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/home/ubuntu/app_python/docker-compose.yml",
-    "state": "file"
+    "state": "absent"
 }

changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [web_app : Create folder for web app if it does not exist] *************************************************************************************
ok: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [web_app : Copy template file] *****************************************************************************************************************
--- before
+++ after: /home/tanmay/.ansible/tmp/ansible-local-331725eglls44/tmpo5_niu7a/docker-compose.yml.j2
@@ -0,0 +1,7 @@
+version: "3"
+
+services:
+  web:
+    image: sharmatanmay617/app_python:latest
+    ports:
+      - "5000:5000"
\ No newline at end of file

changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [web_app : Stop and remove Docker containers] **************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [web_app : Run docker-compose] *****************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

PLAY RECAP ******************************************************************************************************************************************
ec2-3-71-79-119.eu-central-1.compute.amazonaws.com : ok=18   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

#### Demo

![](https://i.postimg.cc/rs3bGBgC/Screenshot-from-2024-03-20-01-53-00.png)



## BEST PRACTICES

1. ```ansible.cfg``` was used for settings.
2. Tasks were named before using.
3. Folder structure mentioned in the lab was used.