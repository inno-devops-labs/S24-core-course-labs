# Ansible work

# Lab 6

## Commands Outputs

- `ansible-playbook playbooks/dev/main.yml`

```
PLAY [all] *******************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************
ok: [katykosh]

TASK [docker : Install pip3] *************************************************************************************
ok: [katykosh]

TASK [docker : Install docker] ***********************************************************************************
ok: [katykosh]

TASK [docker : Install docker-compose] ***************************************************************************
ok: [katykosh]

TASK [web_app : pull the docker image] ***************************************************************************
changed: [katykosh]

TASK [web_app : run the docker container] ************************************************************************
changed: [katykosh]

PLAY RECAP *******************************************************************************************************
katykosh                   : ok=6    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

# Lab 5

## Overview

I used Yandex Cloud VM to run the ansible roles. Its credetials are specified in `ansible/inventory/default_yandex_cloud.yml` file.

Ansible configuration can be found in `ansible.cfg`.

`ansible/playbooks/dev/main.yml` contains the tasts to be executed on all hosts. It also contains the role docker.

`ansible/roles/docker` folder contains:
- the `default/main.yml` file from the [example](https://github.com/geerlingguy/ansible-role-docker). It is a config for installing docker.
- the custom docker role described in `ANSIBLE.md` file

## Commands Outputs

- `ansible-playbook playbooks/dev/main.yml --diff`

```
PLAY [Install docker and docker-compose] ********************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************
ok: [katykosh]

TASK [docker : Install pip3] *******************************************************************************************************
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
0 upgraded, 64 newly installed, 0 to remove and 0 not upgraded.
changed: [katykosh]

TASK [docker : Install docker] *************************************************************************************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 0 not upgraded.
changed: [katykosh]

TASK [docker : Install docker-compose] *****************************************************************************************
changed: [katykosh]

PLAY RECAP **************************************************************************************************************************
katykosh                   : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```


- `ansible-inventory -i inventory/default_yandex_cloud.yml --list`

```
{
    "_meta": {
        "hostvars": {
            "devops": {
                "ansible_connection": "ssh",
                "ansible_host": "84.201.158.25",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "katykosh"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "katykosh"
        ]
    }
}
```
