# Lab 5

# Ansible Documentation

## Overview
This document outlines the Ansible-related work completed for the deployment of Docker on a cloud VM.

## Custom Docker Role

### Task Summary
The custom Docker role was developed to automate the installation of Docker and Docker Compose on a target host. Needed variables was added to ```defaults/main.yml```.

## Deployment Output
```ansible-playbook ./playbooks/dev/main.yml --diff -i ./inventory/default_aws_ec2.yml```
### Output:
```
PLAY [Install docker manually] ****************************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : Install `pip`] *****************************************************************************************************************************************
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
0 upgraded, 64 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

TASK [../../roles/docker : install docker] ****************************************************************************************************************************************
included: /mnt/p/Prog/DevOops/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for host_01

TASK [../../roles/docker : Dependencies packages] *********************************************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : GPG key] ***********************************************************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : Adding Docker Repo] ************************************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable

changed: [host_01]

TASK [../../roles/docker : Docker Installation] ***********************************************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : install docker-compose] ********************************************************************************************************************************
included: /mnt/p/Prog/DevOops/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for host_01

TASK [../../roles/docker : Install Docker Compose using pip] **********************************************************************************************************************
ok: [host_01]

PLAY RECAP ************************************************************************************************************************************************************************
host_01                    : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
## Inventory Details
```ansible-inventory -i ./inventory/default_aws_ec2.yml --list```
### Output
```
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "158.160.116.148",
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

# Lab 6

## Task 1: Application Deployment

Last 50 lines of the output ```ansible-playbook playbooks/dev/main.yml -i inventory```:

```
PLAY [My web app] *************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************
ok: [host_01]

TASK [docker : Install `pip`] *************************************************************************************************************
ok: [host_01]

TASK [docker : install docker] ************************************************************************************************************
included: /mnt/p/Prog/DevOops/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for host_01

TASK [docker : Dependencies packages] *****************************************************************************************************
ok: [host_01]

TASK [docker : GPG key] *******************************************************************************************************************
ok: [host_01]

TASK [docker : Adding Docker Repo] ********************************************************************************************************
ok: [host_01]

TASK [docker : Docker Installation] *******************************************************************************************************
ok: [host_01]

TASK [docker : install docker-compose] ****************************************************************************************************
included: /mnt/p/Prog/DevOops/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for host_01

TASK [docker : Install Docker Compose using pip] ******************************************************************************************
ok: [host_01]

TASK [../../roles/web_app : Initialize directory] *****************************************************************************************
changed: [host_01]

TASK [../../roles/web_app : Docker-compose template] **************************************************************************************
changed: [host_01]

TASK [../../roles/web_app : App creation] *************************************************************************************************
changed: [host_01]

TASK [../../roles/web_app : Docker wiping] ************************************************************************************************
skipping: [host_01]

TASK [../../roles/web_app : Directory wiping] *********************************************************************************************
skipping: [host_01]

PLAY RECAP ********************************************************************************************************************************
host_01                    : ok=12   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

## Task 2: Ansible Best Practices

running wipe:

```
PLAY [My web app] *************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************
ok: [host_01]

TASK [../../roles/web_app : Docker wiping] ************************************************************************************************
changed: [host_01]

TASK [../../roles/web_app : Directory wiping] *********************************************************************************************
changed: [host_01]

PLAY RECAP ********************************************************************************************************************************
host_01                    : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

