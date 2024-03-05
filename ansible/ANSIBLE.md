# Ansible

```sh
❯ ansible-playbook playbooks/dev/main.yml --diff 

PLAY [Install docker and docker-compose] ********************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************
ok: [ubuntu_server]

TASK [docker : Install docker] ******************************************************************************************************************************************
included: /Users/a.ragulin/Vault/Study/Innopolis/year3semester2/DevOps/homeworks/ansible/roles/docker/tasks/install_docker.yml for ubuntu_server

TASK [docker : Install required packages] *******************************************************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 217 not upgraded.
changed: [ubuntu_server] => (item=apt-transport-https)
ok: [ubuntu_server] => (item=ca-certificates)
ok: [ubuntu_server] => (item=curl)
ok: [ubuntu_server] => (item=software-properties-common)

TASK [docker : Add Docker's official GPG key] ***************************************************************************************************************************
changed: [ubuntu_server]

TASK [docker : Add Docker repository] ***********************************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] "https://download.docker.com/linux/ubuntu" bionic stable

changed: [ubuntu_server]

TASK [docker : Update apt and install Docker] ***************************************************************************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 217 not upgraded.
changed: [ubuntu_server]

TASK [docker : Install docker-compose] **********************************************************************************************************************************
included: /Users/a.ragulin/Vault/Study/Innopolis/year3semester2/DevOps/homeworks/ansible/roles/docker/tasks/install_compose.yml for ubuntu_server

TASK [docker : Install pip] *********************************************************************************************************************************************
The following additional packages will be installed:
  build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base gcc-12-base
  javascript-common libalgorithm-diff-perl libalgorithm-diff-xs-perl
  libalgorithm-merge-perl libasan6 libatomic1 libc-dev-bin libc-devtools libc6
  libc6-dev libcc1-0 libcrypt-dev libdeflate0 libdpkg-perl libexpat1
  libexpat1-dev libfakeroot libfile-fcntllock-perl libfontconfig1
  libgcc-11-dev libgcc-s1 libgd3 libgomp1 libisl23 libitm1 libjbig0
  libjpeg-turbo8 libjpeg8 libjs-jquery libjs-sphinxdoc libjs-underscore
  liblsan0 libmpc3 libnsl-dev libpython3-dev libpython3-stdlib libpython3.10
  libpython3.10-dev libpython3.10-minimal libpython3.10-stdlib libquadmath0
  libstdc++-11-dev libstdc++6 libtiff5 libtirpc-common libtirpc-dev libtirpc3
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3 python3-dev python3-distutils python3-lib2to3
  python3-minimal python3-wheel python3.10 python3.10-dev python3.10-minimal
  rpcsvc-proto zlib1g zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc python3-doc python3-tk python3-venv
  python3.10-venv python3.10-doc binfmt-support
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
  gcc-12-base libc6 libexpat1 libgcc-s1 libpython3-stdlib libpython3.10
  libpython3.10-minimal libpython3.10-stdlib libstdc++6 libtirpc-common
  libtirpc3 python3 python3-distutils python3-lib2to3 python3-minimal
  python3.10 python3.10-minimal zlib1g
18 upgraded, 64 newly installed, 0 to remove and 199 not upgraded.
changed: [ubuntu_server]

TASK [docker : Install docker-compose] **********************************************************************************************************************************
changed: [ubuntu_server]

PLAY RECAP **************************************************************************************************************************************************************
ubuntu_server              : ok=9    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

```sh
❯ ansible-inventory -i inventory/main.yaml --list
{
    "_meta": {
        "hostvars": {
            "ubuntu_server": {
                "ansible_host": "206.188.197.213",
                "ansible_user": "root"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "servers"
        ]
    },
    "servers": {
        "hosts": [
            "ubuntu_server"
        ]
    }
}
```
