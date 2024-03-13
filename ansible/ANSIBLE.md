# Ansible

## Prerequisites

- I bought Yandex Cloud VM and specified login credentials in the `inventory/yandex_cloud.yml`.
- I also configured ansible in `ansible.cfg`.

## Commands output

Task 2.3

```sh
ansible-playbook playbooks/dev/main.yml --diff
```

```plaintext
PLAY [Install Docker and Docker Compose] ********************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************
ok: [devops]

TASK [docker : Install `pip`] *******************************************************************************************************
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
changed: [devops]

TASK [docker : Docker installation] *************************************************************************************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 0 not upgraded.
changed: [devops]

TASK [docker : docker-compose installation] *****************************************************************************************
changed: [devops]

PLAY RECAP **************************************************************************************************************************
devops                     : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Task 2.4

```sh
ansible-inventory -i <name_of_your_inventory_file>.yaml --list
```

```plaintext
{
    "_meta": {
        "hostvars": {
            "devops": {
                "ansible_connection": "ssh",
                "ansible_host": "84.201.161.146",
                "ansible_ssh_private_key_file": "~/.ssh/yandex/id_ed25519",
                "ansible_user": "devops"
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
            "devops"
        ]
    }
}
```

## Best Practices

- I used the proper files organization
- I used `ansible.cfg` to setup global settings

## Lab 6 Output

```sh
ansible-playbook playbooks/dev/main.yml --diff
```

```plaintext
PLAY [Setup Web Application] *************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************
ok: [devops]

TASK [docker : Install `pip`] ************************************************************************************************
ok: [devops]

TASK [docker : Docker installation] ******************************************************************************************
ok: [devops]

TASK [docker : docker-compose installation] **********************************************************************************
ok: [devops]

TASK [web_app : Stop and remove the moscow_time container] *******************************************************************
skipping: [devops]

TASK [web_app : Deliver docker compose] **************************************************************************************
ok: [devops]

TASK [web_app : Pull the image from Dockerhub] *******************************************************************************
changed: [devops]

TASK [web_app : Run a container] *********************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [devops]

PLAY RECAP *******************************************************************************************************************
devops                     : ok=7    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0 
```
