# Ansible

## Playbook diff

```
PLAY [Main] **********************************************************************************

TASK [Gathering Facts] ***********************************************************************
ok: [some-sad-machine]

TASK [docker : Register version codename] ****************************************************
changed: [some-sad-machine]

TASK [docker : Install docker dependencies] **************************************************
The following NEW packages will be installed:
  apt-transport-https gnupg-agent
0 upgraded, 2 newly installed, 0 to remove and 123 not upgraded.
changed: [some-sad-machine]

TASK [docker : Add docker gpg key] ***********************************************************
changed: [some-sad-machine]

TASK [docker : Add docker repository] ********************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu jammy stable

changed: [some-sad-machine]

TASK [docker : Install docker engine] ********************************************************
The following additional packages will be installed:
  docker-ce-rootless-extras libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin docker-scan-plugin libltdl7
  libslirp0 pigz slirp4netns
0 upgraded, 11 newly installed, 0 to remove and 123 not upgraded.
changed: [some-sad-machine]

TASK [docker : Install pip] ******************************************************************
The following additional packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6 libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev libfakeroot
  libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3 libgomp1 libisl23
  libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev libpython3.10
  libpython3.10-dev libpython3.10-minimal libpython3.10-stdlib libquadmath0
  libstdc++-11-dev libtiff5 libtirpc-dev libtsan0 libubsan1 libwebp7 libxpm4
  linux-libc-dev lto-disabled-list make manpages-dev python3-dev python3-wheel
  python3.10 python3.10-dev python3.10-minimal rpcsvc-proto zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc python3.10-venv python3.10-doc binfmt-support
Recommended packages:
  libnss-nis libnss-nisplus
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
The following packages will be upgraded:
  libc6 libpython3.10 libpython3.10-minimal libpython3.10-stdlib python3.10
  python3.10-minimal
6 upgraded, 64 newly installed, 0 to remove and 117 not upgraded.
changed: [some-sad-machine]

TASK [docker : Install Docker SDK] ***********************************************************
changed: [some-sad-machine]

TASK [docker : Setup user 'dima-batalov'] ****************************************************
changed: [some-sad-machine]

PLAY RECAP ***********************************************************************************
some-sad-machine           : ok=9    changed=8    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory

```
{
    "_meta": {
        "hostvars": {
            "some-sad-machine": {
                "ansible_host": "51.250.102.90",
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa_kluster",
                "ansible_user": "dima-batalov"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "vms"
        ]
    },
    "vms": {
        "hosts": [
            "some-sad-machine"
        ]
    }
}
```

## Web app deploy

```
PLAY [some-sad-machine] ****************************************************************************

TASK [Gathering Facts] *****************************************************************************
ok: [some-sad-machine]

TASK [docker : Register version codename] **********************************************************
changed: [some-sad-machine]

TASK [docker : Install docker dependencies] ********************************************************
ok: [some-sad-machine]

TASK [docker : Add docker gpg key] *****************************************************************
ok: [some-sad-machine]

TASK [docker : Add docker repository] **************************************************************
ok: [some-sad-machine]

TASK [docker : Install docker engine] **************************************************************
ok: [some-sad-machine]

TASK [docker : Install pip] ************************************************************************
ok: [some-sad-machine]

TASK [docker : Install Docker SDK] *****************************************************************
ok: [some-sad-machine]

TASK [docker : Setup user 'dima-batalov'] **********************************************************
ok: [some-sad-machine]

TASK [web_app : Wipe app] **************************************************************************
skipping: [some-sad-machine]

TASK [web_app : Pull docker image] *****************************************************************
changed: [some-sad-machine]

TASK [web_app : Run container] *********************************************************************
changed: [some-sad-machine]

PLAY RECAP *****************************************************************************************
some-sad-machine           : ok=11   changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0 
```