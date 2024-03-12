# Ansible

## Description

Ansible is a software tool that provides simple but powerful automation for cross-platform computer support. It is primarily intended for IT professionals, who use it for application deployment, updates on workstations and servers, cloud provisioning, configuration management, intra-service orchestration, and nearly anything a systems administrator does on a weekly or daily basis

## Roles, Playbooks, and Inventory in Ansible

- Roles:


**Definition:** Roles in Ansible are a way of automatically loading certain vars_files, tasks, and handlers based on a known file structure. They provide a method for organizing and encapsulating functionality in a way that is easy to reuse and share with others.
**Structure:** An Ansible role has a defined directory structure with eight main standard directories, including tasks, handlers, defaults, vars, and more. This structure allows for the organization and management of role-specific content.
**Benefits:** Roles make it easier to manage and reuse related Ansible content, and they allow for easy sharing of roles with other users. They provide a more manageable structure than using playbooks alone, especially as projects grow in complexity.

- Playbooks:


**Definition:** Playbooks in Ansible are used to record and execute Ansible's configuration, deployment, and orchestration functions. They describe the policies to be enforced on remote systems or a set of steps in a general IT process.
**Structure:** Playbooks are written in YAML and are easy to read, write, share, and understand. They can be used to manage configurations of and deployments to remote machines, and can also sequence multi-tier rollouts involving rolling updates and delegate actions to other hosts.
**Verification:** Ansible provides options for verifying playbooks to catch syntax errors and other problems before running them, including --check, --diff, --list-hosts, --list-tasks, and --syntax-check.

- Inventory:


**Definition:** The inventory in Ansible is a list of managed nodes provided by one or more inventory sources. It specifies information specific to each node, such as IP address, and is used for assigning groups and bulk variable assignment.
**Functionality:** The inventory can be dynamic, and if the inventory file is executable, Ansible will run it and use its output as the inventory. It can also specify groups, allowing for node selection in the play and bulk variable assignment.
**Best Practices:** It is recommended to keep the playbooks, roles, inventory, and variables files in a version control system to maintain an audit trail and make changes with meaningful comments. This helps in making playbooks and roles easier to read, maintain, and debug.

## Deployment Output:

```bash
ansible-playbook playbooks/dev/main.yaml --diff
```

```bash
PLAY [Установка Docker] ********************************************************

TASK [Gathering Facts] *********************************************************
The authenticity of host '84.201.133.194 (84.201.133.194)' can't be established.
ED25519 key fingerprint is SHA256:Qa6kjyU9lgZMIX/TTsDIFyrXa7woooEWA8qpqoKMsrs.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [new_host]

TASK [docker : Update apt] *****************************************************
changed: [new_host]

TASK [docker : Python3 and pip3 installation] **********************************
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
changed: [new_host]

TASK [docker : Install docker] *************************************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 3 not upgraded.
changed: [new_host]

TASK [docker : Install Docker Compose] *****************************************
changed: [new_host]

PLAY RECAP *********************************************************************
new_host                   : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Inventory Details:

```bash
ansible-inventory -i inventory/default_yandex_cloud.yml --list
```

```bash
{
    "_meta": {
        "hostvars": {
            "new_host": {
                "ansible_host": "84.201.133.194",
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
            "new_host"
        ]
    }
}
```

## Web-app

```bash
anastasia@anastasia-Vivobook-ASUSLaptop-M3401QA-M3401QA:~/S24-DevOps-labs/ansible$ ansible-playbook playbooks/dev/main.yaml --tags "deploy,wipe" --diff
```

```bash
PLAY [Установка Docker] ******************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************
ok: [new_host]

PLAY [Deploy Web Application] ************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************
ok: [new_host]

TASK [web_app : Stop and remove Docker container] ****************************************************************************************************
ok: [new_host]

PLAY RECAP *******************************************************************************************************************************************
new_host                   : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```
