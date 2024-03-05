# Configuring Ansible 

### Best Practices
- ansible project structure is following ansible standards


## Docker
Installing Docker via apt and Docker-compose via pip

### Outputs
```bash
$ ansible-playbook ./playbooks/dev/main.yaml
PLAY [Docker roles] *************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : Install python3-pip] *********************************************************************************
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
6 upgraded, 64 newly installed, 0 to remove and 115 not upgraded.
changed: [host_01]

TASK [../../roles/docker : include_tasks] ***************************************************************************************
included: /home/anastasia/Documents/devops/ansible/roles/docker/tasks/install_docker.yml for host_01

TASK [../../roles/docker : Docker installation] *********************************************************************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 115 not upgraded.
changed: [host_01]

TASK [../../roles/docker : include_tasks] ***************************************************************************************
included: /home/anastasia/Documents/devops/ansible/roles/docker/tasks/install_compose.yml for host_01

TASK [../../roles/docker : Docker-compose installation] *************************************************************************
changed: [host_01]

PLAY RECAP **********************************************************************************************************************
host_01                    : ok=6    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```


```bash
$ ansible-inventory -i inventory/default_yc_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "158.160.111.127",
                "ansible_user": "asya"
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
            "host_01"
        ]
    }
}
```