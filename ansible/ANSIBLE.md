#Ansible

```
(base) yanapavlova@MacBook-Air-Ana ansible % ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Install Docker] ******************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [host_01]

TASK [docker : Update apt cache] *******************************************************************************************************************************************
changed: [host_01]

TASK [docker : Install required packages] **********************************************************************************************************************************
The following additional packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
  dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan5 libatomic1
  libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
  libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-9-dev libgomp1 libisl22 libitm1 liblsan0 libmpc3 libmpfr6
  libpython3-dev libpython3.8-dev libquadmath0 libstdc++-9-dev libtsan0
  libubsan1 linux-libc-dev make manpages-dev python-pip-whl python3-dev
  python3-wheel python3.8-dev zlib1g-dev
Suggested packages:
  binutils-doc cpp-doc gcc-9-locales debian-keyring g++-multilib
  g++-9-multilib gcc-9-doc gcc-multilib autoconf automake libtool flex bison
  gdb gcc-doc gcc-9-multilib glibc-doc bzr libstdc++-9-doc make-doc
The following NEW packages will be installed:
  binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
  dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base gnupg-agent
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan5 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev
  libctf-nobfd0 libctf0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libgcc-9-dev libgomp1 libisl22 libitm1 liblsan0
  libmpc3 libmpfr6 libpython3-dev libpython3.8-dev libquadmath0
  libstdc++-9-dev libtsan0 libubsan1 linux-libc-dev make manpages-dev
  python-pip-whl python3-dev python3-pip python3-wheel python3.8-dev
  zlib1g-dev
0 upgraded, 52 newly installed, 0 to remove and 15 not upgraded.
changed: [host_01]

TASK [docker : Remove conflicting Docker GPG keys] *************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/etc/apt/sources.list.d/docker.list",
-    "state": "file"
+    "state": "absent"
 }

changed: [host_01]

TASK [docker : Clear APT cache] ********************************************************************************************************************************************
Del containerd.io 1.6.28-1 [29.6 MB]
Del docker-compose-plugin 2.24.6-1~ubuntu.20.04~focal [12.1 MB]
Del docker-ce-cli 5:25.0.3-1~ubuntu.20.04~focal [13.7 MB]
Del docker-ce-rootless-extras 5:25.0.3-1~ubuntu.20.04~focal [9324 kB]
Del docker-ce 5:25.0.3-1~ubuntu.20.04~focal [24.3 MB]
Del docker-buildx-plugin 0.12.1-1~ubuntu.20.04~focal [28.2 MB]
changed: [host_01]

TASK [docker : Ensure correct Docker repository configuration] *************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [host_01]

TASK [docker : Install Docker] *********************************************************************************************************************************************
ok: [host_01]

TASK [docker : Install Docker Compose] *************************************************************************************************************************************
changed: [host_01]

TASK [docker : Add Docker GPG key] *****************************************************************************************************************************************
ok: [host_01]

TASK [docker : Add Docker repository] **************************************************************************************************************************************
ok: [host_01]

TASK [docker : Install Docker (again, if repository configuration changed)] ************************************************************************************************
ok: [host_01]

TASK [docker : Install Docker Compose (again, if repository configuration changed)] ****************************************************************************************
ok: [host_01]

PLAY RECAP *****************************************************************************************************************************************************************
host_01                    : ok=22   changed=6    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0
```

## Ansible inventory output
```
(base) yanapavlova@MacBook-Air-Ana ansible %  ansible-inventory -i inventory/ya-cloud-vm.yml --list 
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "51.250.66.22",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "myhosts"
        ]
    },
    "myhosts": {
        "hosts": [
            "host_01"
        ]
    }
}
```