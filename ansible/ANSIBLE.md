# Ansible

## `ansible-playbook --diff` (lab 5), last 50 lines

```
  aufs-tools cgroupfs-mount | cgroup-lite git-daemon-run | git-daemon-sysvinit
  git-doc git-el git-email git-gui gitk gitweb git-cvs git-mediawiki git-svn
  diffutils-doc perl-doc libterm-readline-gnu-perl
  | libterm-readline-perl-perl make libb-debug-perl liblocale-codes-perl
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin git git-man libcurl3-gnutls
  liberror-perl libgdbm-compat4 libperl5.30 patch perl perl-modules-5.30 pigz
  slirp4netns
0 upgraded, 17 newly installed, 0 to remove and 14 not upgraded.
changed: [host_01]

TASK [docker : include_tasks] ***************************************************************************************
included: /home/nikolay/Docs/Uni/DevOps/ansible/roles/docker/tasks/docker-compose.yaml for host_01

TASK [docker : Install pip via apt] *********************************************************************************
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
  dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan5 libatomic1
  libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
  libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-9-dev libgomp1 libisl22 libitm1 liblsan0 libmpc3 libmpfr6
  libpython3-dev libpython3.8-dev libquadmath0 libstdc++-9-dev libtsan0
  libubsan1 linux-libc-dev make manpages-dev python-pip-whl python3-dev
  python3-pip python3-wheel python3.8-dev zlib1g-dev
0 upgraded, 51 newly installed, 0 to remove and 14 not upgraded.
changed: [host_01]

TASK [docker : Install docker-compose via pip] **********************************************************************
changed: [host_01]

PLAY RECAP **********************************************************************************************************
host_01                    : ok=12   changed=6    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
this                       : ok=4    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

```

## `ansible-inventory --list`

```
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "51.250.1.65",
                "ansible_user": "ubuntu"
            },
            "this": {
                "ansible_host": "localhost"
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
    },
    "ungrouped": {
        "hosts": [
            "this"
        ]
    }
}
```

In the above output there are two hosts defined: `{ anshible_host: localhost }` and
`{ ansible_host: "51.250.1.65", ansible_user: "ubuntu" }`. The first one belongs to the
`ungrouped` group, the second belongs to the `myhosts` group, both belong to the `all`
metagroup (which is a special group that contains all defined hosts).

## `ansible-playbook --diff` for app_python, last 50 lines
```
  libpython3-dev libpython3.8-dev libquadmath0 libstdc++-9-dev libtsan0
  libubsan1 linux-libc-dev make manpages-dev python-pip-whl python3-dev
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
  libubsan1 linux-libc-dev make manpages-dev python-pip-whl python3-dev
  python3-pip python3-wheel python3.8-dev zlib1g-dev
0 upgraded, 51 newly installed, 0 to remove and 15 not upgraded.
changed: [terraform1]

TASK [docker : Install docker-compose via pip] ***********************************************************************
changed: [terraform1]

TASK [web_app : Pull image] ******************************************************************************************
--- before
+++ after
@@ -1,3 +1,3 @@
 {
-    "exists": false
+    "id": "sha256:55ef999c615bdb60c47911f0a4d11b1f5eb5eb9975d1f34d105cbaeac08626ca"
 }

changed: [terraform1]

TASK [web_app : Create container] ************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [terraform1]

PLAY RECAP ***********************************************************************************************************
terraform1                 : ok=12   changed=9    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

```

## Best practices

The project uses the following best practices:

-   Generous use of whitespace

-   Give names to everything

-   Always mention the state

-   Use fully qualified collection names

-   Use dynamic inventory with clouds
