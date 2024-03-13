# Ansible lab
## Inventory
`ansible/inventory/yandex_cloud` file contains ip address for vm where I am installing docker and docker-compose

## Playbooks
`ansible/playbooks/dev/main.yml` runs the docker role which installs docker and docke-compose in the VM.

## commands output

### **`ansible-playbook playbooks/dev/main.yml --diff`**
```
    PLAY [Run Docker role] ****************************************************************************************************

    TASK [Gathering Facts] ****************************************************************************************************
    ok: [51.250.102.185]

    TASK [docker : Update apt] ************************************************************************************************
    ok: [51.250.102.185]

    TASK [docker : Install pip] ***********************************************************************************************
    The following additional packages will be installed:
    binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
    dpkg-dev fakeroot g++ g++-9 gcc gcc-10-base gcc-9 gcc-9-base
    libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
    libasan5 libatomic1 libbinutils libc-dev-bin libc6 libc6-dev libcc1-0
    libcrypt-dev libctf-nobfd0 libctf0 libdpkg-perl libexpat1 libexpat1-dev
    libfakeroot libfile-fcntllock-perl libgcc-9-dev libgcc-s1 libgdbm-compat4
    libgomp1 libisl22 libitm1 liblsan0 libmpc3 libmpfr6 libperl5.30
    libpython3-dev libpython3.8 libpython3.8-dev libpython3.8-minimal
    libpython3.8-stdlib libquadmath0 libstdc++-9-dev libstdc++6 libtsan0
    libubsan1 linux-libc-dev make manpages-dev patch perl perl-base
    perl-modules-5.30 python-pip-whl python3-dev python3-pkg-resources
    python3-wheel python3.8 python3.8-dev python3.8-minimal zlib1g zlib1g-dev
    Suggested packages:
    binutils-doc cpp-doc gcc-9-locales debian-keyring g++-multilib
    g++-9-multilib gcc-9-doc gcc-multilib autoconf automake libtool flex bison
    gdb gcc-doc gcc-9-multilib glibc-doc git bzr libstdc++-9-doc make-doc
    diffutils-doc perl-doc libterm-readline-gnu-perl
    | libterm-readline-perl-perl libb-debug-perl liblocale-codes-perl
    python-setuptools-doc python3.8-venv python3.8-doc binfmt-support
    The following NEW packages will be installed:
    binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-9
    dpkg-dev fakeroot g++ g++-9 gcc gcc-9 gcc-9-base libalgorithm-diff-perl
    libalgorithm-diff-xs-perl libalgorithm-merge-perl libasan5 libatomic1
    libbinutils libc-dev-bin libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0
    libctf0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
    libgcc-9-dev libgdbm-compat4 libgomp1 libisl22 libitm1 liblsan0 libmpc3
    libmpfr6 libperl5.30 libpython3-dev libpython3.8-dev libquadmath0
    libstdc++-9-dev libtsan0 libubsan1 linux-libc-dev make manpages-dev patch
    perl perl-modules-5.30 python-pip-whl python3-dev python3-pip python3-wheel
    python3.8-dev zlib1g-dev
    The following packages will be upgraded:
    gcc-10-base libc6 libexpat1 libgcc-s1 libpython3.8 libpython3.8-minimal
    libpython3.8-stdlib libstdc++6 perl-base python3-pkg-resources
    python3-setuptools python3.8 python3.8-minimal zlib1g
    14 upgraded, 56 newly installed, 0 to remove and 180 not upgraded.
    changed: [51.250.102.185]

    TASK [docker : Install Docker dependencies] *******************************************************************************
    ok: [51.250.102.185]

    TASK [docker : Add Docker GPG key] ****************************************************************************************
    changed: [51.250.102.185]

    TASK [docker : Add Docker repository] *************************************************************************************
    --- before: /dev/null
    +++ after: /etc/apt/sources.list.d/docker.list
    @@ -0,0 +1 @@
    +deb https://download.docker.com/linux/ubuntu bionic stable

    changed: [51.250.102.185]

    TASK [docker : Install Docker] ********************************************************************************************
    The following additional packages will be installed:
    containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
    docker-compose-plugin git git-man libcurl3-gnutls liberror-perl pigz
    slirp4netns
    Suggested packages:
    aufs-tools cgroupfs-mount | cgroup-lite git-daemon-run | git-daemon-sysvinit
    git-doc git-el git-email git-gui gitk gitweb git-cvs git-mediawiki git-svn
    The following NEW packages will be installed:
    containerd.io docker-buildx-plugin docker-ce docker-ce-cli
    docker-ce-rootless-extras docker-compose-plugin git git-man libcurl3-gnutls
    liberror-perl pigz slirp4netns
    0 upgraded, 12 newly installed, 0 to remove and 180 not upgraded.
    changed: [51.250.102.185]

    TASK [docker : Upgrade pip] ***********************************************************************************************
    changed: [51.250.102.185]

    TASK [docker : Install docker-compose] ************************************************************************************
    changed: [51.250.102.185]

    PLAY RECAP ****************************************************************************************************************
    51.250.102.185             : ok=9    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

### **`ansible-inventory -i inventory/yandex_cloud.yml --list`**
```json
    {
        "_meta": {
            "hostvars": {
                "51.250.102.185": {
                    "ansible_user": "ubuntu"
                }
            }
        },
        "all": {
            "children": [
                "myhost",
                "ungrouped"
            ]
        },
        "myhost": {
            "hosts": [
                "51.250.102.185"
            ]
        }
    }
```

### **`ansible-playbook playbooks/dev/main.yml -i inventory/yandex_cloud.yml`**
```
    PLAY [Install docker & deploy python app] ***************************************************************************************

    TASK [Gathering Facts] **********************************************************************************************************
    ok: [62.84.123.211]

    TASK [docker : Update apt] ******************************************************************************************************
    ok: [62.84.123.211]

    TASK [docker : Install pip] *****************************************************************************************************
    ok: [62.84.123.211]

    TASK [docker : Install Docker dependencies] *************************************************************************************
    ok: [62.84.123.211]

    TASK [docker : Add Docker GPG key] **********************************************************************************************
    ok: [62.84.123.211]

    TASK [docker : Add Docker repository] *******************************************************************************************
    ok: [62.84.123.211]

    TASK [docker : Install Docker] **************************************************************************************************
    ok: [62.84.123.211]

    TASK [docker : Install docker-compose] ******************************************************************************************
    ok: [62.84.123.211]

    TASK [web_app : create project directory] ***************************************************************************************
    changed: [62.84.123.211]

    TASK [web_app : start docker] ***************************************************************************************************
    ok: [62.84.123.211]

    TASK [web_app : pull the image] *************************************************************************************************
    ok: [62.84.123.211]

    TASK [web_app : create docker-compose file] *************************************************************************************
    changed: [62.84.123.211]

    TASK [web_app : run the container] **********************************************************************************************
    changed: [62.84.123.211]

    PLAY RECAP **********************************************************************************************************************
    62.84.123.211              : ok=13   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```