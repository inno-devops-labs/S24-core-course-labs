# Ansible Documentation

## Overview
This repository uses Ansible for infrastructure automation and Docker deployment.

## Setup
- Install Ansible using pip: `pip install ansible`
- Use SSH for communication between the Ansible control node and target hosts.

## Output

### Docker

The command:

`ansible-playbook playbooks/dev/main.yml --diff`

Gives the following output:

```bash
PLAY [Install Docker and Docker Compose] ****************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************
ok: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

TASK [docker : Update apt packages] *********************************************************************************************
changed: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Update docker.io package] ********************************************************************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Upgrade python3-pip] *************************************************************************************
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
changed: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

TASK [docker : Upgrade pip] *****************************************************************************************************
changed: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker sdk] **********************************************************************************************
changed: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker-compose] ******************************************************************************************
changed: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

RUNNING HANDLER [docker : Give ubuntu docker group access] **********************************************************************
changed: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

RUNNING HANDLER [docker : Run docker] *******************************************************************************************
changed: [ec2-54-185-58-229.us-west-2.compute.amazonaws.com]

PLAY RECAP **********************************************************************************************************************
ec2-54-185-58-229.us-west-2.compute.amazonaws.com : ok=9    changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
---
The command:

`ansible-inventory -i inventory/default_aws_ec2.yml --list`

Gives the following output:

```json
{
    "_meta": {
        "hostvars": {
            "ec2-54-185-58-229.us-west-2.compute.amazonaws.com": {
                "ansible_connection": "ssh",
                "ansible_ssh_private_key_file": "~/.ssh/manual_pair.pem",
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
            "ec2-54-185-58-229.us-west-2.compute.amazonaws.com"
        ]
    }
}
```
---
### Python App

P.S: I change AWS instances beacuase the free trials end.

Deploying the application by the command:

`ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/python_app/main.yml`

Gives the following output:

```bash
PLAY [Install Docker] **************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Update apt packages] ************************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Update docker.io package] ***********************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Upgrade python3-pip] ****************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Upgrade pip] ********************************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker sdk] *************************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker-compose] *********************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

RUNNING HANDLER [docker : Give ubuntu docker group access] *************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

RUNNING HANDLER [docker : Run docker] **********************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

PLAY [Python web app deployment] ***************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Update apt packages] ************************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Update docker.io package] ***********************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Install/Upgrade python3-pip] ****************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Upgrade pip] ********************************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker sdk] *************************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [docker : Install docker-compose] *********************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : Create App Directory] **********************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : Ensure Docker Service is Running and Enabled] **********************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : Pull Docker Image] *************************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : Generate Docker-Compose Configuration] *****************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : Remove existing Docker containers] *********************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : Start Docker Compose] **********************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

PLAY RECAP *************************************************************************************************************
ec2-35-94-146-206.us-west-2.compute.amazonaws.com : ok=22   changed=13   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
---

Wiping the application by the command:

`ansible-playbook playbooks/dev/python_app/main.yml --tags "wipe" --diff`

Gives the following output:

```bash
PLAY [Install Docker] **************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

PLAY [Python web app deployment] ***************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : include_tasks] *****************************************************************************************
included: /home/g-akleh/Desktop/VSCode/S24-core-course-labs/ansible/roles/web_app/tasks/wipe.yml for ec2-35-94-146-206.us-west-2.compute.amazonaws.com

TASK [web_app : Check Docker Compose File Presence] ********************************************************************
ok: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : Remove Docker Environment] *****************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : command] ***********************************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : command] ***********************************************************************************************
changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

TASK [web_app : file] **************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/ubuntu-python-web-app/docker-compose.yml",
-    "state": "file"
+    "state": "absent"
 }

changed: [ec2-35-94-146-206.us-west-2.compute.amazonaws.com]

PLAY RECAP *************************************************************************************************************
ec2-35-94-146-206.us-west-2.compute.amazonaws.com : ok=8    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Best Practices

1. Used tags for more precise control over playbook execution.
2. Implemented wipe logic, with a control variable to determine whether to wipe the web app or not.
3. Templates were used to generate configuration files for Docker Compose, ensuring consistency and ease of maintenance.
4. Roles were separated logically