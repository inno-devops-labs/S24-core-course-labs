# Ansible lab

## Output for commands

- for command `ansible-playbook playbooks/dev/main.yml --diff`:

    ```plaintext

    PLAY [Install Docker and Docker Compose on Ubuntu] *********************************************************************************************************************************************************

    TASK [Gathering Facts] *************************************************************************************************************************************************************************************
    The authenticity of host '51.250.104.24 (51.250.104.24)' can't be established.
    ED25519 key fingerprint is SHA256:qJN0PCzuzUQV0ArGVn39PsDf+XKZdwwBWbOK8CfRBVo.
    This key is not known by any other names
    Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
    ok: [devops]

    TASK [docker : Update apt] *********************************************************************************************************************************************************************************
    changed: [devops]

    TASK [docker : Python3 and pip3 installation] **************************************************************************************************************************************************************
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
    0 upgraded, 64 newly installed, 0 to remove and 2 not upgraded.
    changed: [devops]

    TASK [docker : Install docker] *****************************************************************************************************************************************************************************
    The following additional packages will be installed:
    bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
    Suggested packages:
    ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
    rinse zfs-fuse | zfsutils
    The following NEW packages will be installed:
    bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
    ubuntu-fan
    0 upgraded, 8 newly installed, 0 to remove and 2 not upgraded.
    changed: [devops]

    TASK [docker : Install docker compose] *********************************************************************************************************************************************************************
    changed: [devops]

    PLAY RECAP *************************************************************************************************************************************************************************************************
    devops                     : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ```


- for command `ansible-inventory -i inventory/yandex_cloud.yml  --list`:

    ```plaintext
    {
        "_meta": {
            "hostvars": {
                "devops": {
                    "ansible_host": "51.250.104.24",
                    "ansible_user": "ubuntu"
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