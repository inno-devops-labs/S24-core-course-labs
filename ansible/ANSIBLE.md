# Ansible

#### ansible-playbook playbooks/dev/main.yml --diff

```
PLAY [Update apt] ***************************************************************

TASK [Gathering Facts] **********************************************************
ok: [host2]
ok: [host1]

TASK [Update all apt packages] **************************************************
changed: [host1]
changed: [host2]

PLAY [Deploy geerlingguy.docker] ************************************************

TASK [Gathering Facts] **********************************************************
ok: [host1]
ok: [host2]

TASK [geerlingguy.docker : Load OS-specific vars.] ******************************
ok: [host1]
ok: [host2]

TASK [geerlingguy.docker : include_tasks] ***************************************
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : include_tasks] ***************************************
included: /home/xdr/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for host1, host2

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ****
ok: [host1]
ok: [host2]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ******************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 294 not upgraded.
changed: [host1]
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 294 not upgraded.
changed: [host2]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
The following additional packages will be installed:
  dirmngr gnupg gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client
  gpg-wks-server gpgconf gpgsm gpgv
Suggested packages:
  dbus-user-session pinentry-gnome3 tor parcimonie xloadimage scdaemon
The following NEW packages will be installed:
  gnupg2
The following packages will be upgraded:
  dirmngr gnupg gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client
  gpg-wks-server gpgconf gpgsm gpgv
11 upgraded, 1 newly installed, 0 to remove and 283 not upgraded.
changed: [host2]
The following additional packages will be installed:
  dirmngr gnupg gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client
  gpg-wks-server gpgconf gpgsm gpgv
Suggested packages:
  dbus-user-session pinentry-gnome3 tor parcimonie xloadimage scdaemon
The following NEW packages will be installed:
  gnupg2
The following packages will be upgraded:
  dirmngr gnupg gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client
  gpg-wks-server gpgconf gpgsm gpgv
11 upgraded, 1 newly installed, 0 to remove and 283 not upgraded.
changed: [host1]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] ***
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Add Docker apt key.] *********************************
changed: [host1]
changed: [host2]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] ***
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ***
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Add Docker repository.] ******************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu bionic stable

changed: [host2]
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu bionic stable

changed: [host1]

TASK [geerlingguy.docker : Install Docker packages.] ****************************
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ****
The following additional packages will be installed:
  dbus dbus-user-session docker-buildx-plugin docker-compose-plugin
  libdbus-1-3 libltdl7 libseccomp2 pigz
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
Recommended packages:
  slirp4netns
The following NEW packages will be installed:
  containerd.io dbus-user-session docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 pigz
The following packages will be upgraded:
  dbus libdbus-1-3 libseccomp2
3 upgraded, 9 newly installed, 0 to remove and 280 not upgraded.
changed: [host1]
The following additional packages will be installed:
  dbus dbus-user-session docker-buildx-plugin docker-compose-plugin
  libdbus-1-3 libltdl7 libseccomp2 pigz
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
Recommended packages:
  slirp4netns
The following NEW packages will be installed:
  containerd.io dbus-user-session docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 pigz
The following packages will be upgraded:
  dbus libdbus-1-3 libseccomp2
3 upgraded, 9 newly installed, 0 to remove and 280 not upgraded.
changed: [host2]

TASK [geerlingguy.docker : Install docker-compose plugin.] **********************
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***
ok: [host1]
ok: [host2]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ***************
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Configure Docker daemon options.] ********************
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] *******
ok: [host1]
ok: [host2]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ***

RUNNING HANDLER [geerlingguy.docker : restart docker] ***************************
changed: [host1]
changed: [host2]

TASK [geerlingguy.docker : include_tasks] ***************************************
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Get docker group info using getent.] *****************
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***
skipping: [host1]
skipping: [host2]

TASK [geerlingguy.docker : include_tasks] ***************************************
skipping: [host1]
skipping: [host2]

PLAY [Deploy docker] ************************************************************

TASK [Gathering Facts] **********************************************************
ok: [host1]
ok: [host2]

TASK [docker : Install pip] *****************************************************
The following additional packages will be installed:
  build-essential cpp-7 dh-python dpkg-dev fakeroot g++ g++-7 gcc gcc-7
  gcc-7-base gcc-8-base libalgorithm-diff-perl libalgorithm-diff-xs-perl
  libalgorithm-merge-perl libasan4 libatomic1 libcc1-0 libcilkrts5
  libdpkg-perl libexpat1 libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-7-dev libgcc1 libgomp1 libitm1 liblsan0 libmpx2 libpython3-dev
  libpython3.6 libpython3.6-dev libpython3.6-minimal libpython3.6-stdlib
  libquadmath0 libstdc++-7-dev libstdc++6 libtsan0 libubsan0 python-pip-whl
  python3-crypto python3-dev python3-distutils python3-keyring
  python3-keyrings.alt python3-lib2to3 python3-pkg-resources
  python3-secretstorage python3-setuptools python3-wheel python3-xdg python3.6
  python3.6-dev python3.6-minimal
Suggested packages:
  gcc-7-locales debian-keyring g++-multilib g++-7-multilib gcc-7-doc
  libstdc++6-7-dbg gcc-multilib manpages-dev autoconf automake libtool flex
  bison gdb gcc-doc gcc-7-multilib libgcc1-dbg libgomp1-dbg libitm1-dbg
  libatomic1-dbg libasan4-dbg liblsan0-dbg libtsan0-dbg libubsan0-dbg
  libcilkrts5-dbg libmpx2-dbg libquadmath0-dbg bzr libstdc++-7-doc
  python-crypto-doc gnome-keyring libkf5wallet-bin gir1.2-gnomekeyring-1.0
  python-secretstorage-doc python-setuptools-doc python3.6-venv python3.6-doc
  binfmt-support
The following NEW packages will be installed:
  build-essential dh-python dpkg-dev fakeroot g++ g++-7 gcc gcc-7
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan4 libatomic1 libcc1-0 libcilkrts5 libdpkg-perl libexpat1-dev
  libfakeroot libfile-fcntllock-perl libgcc-7-dev libgomp1 libitm1 liblsan0
  libmpx2 libpython3-dev libpython3.6-dev libquadmath0 libstdc++-7-dev
  libtsan0 libubsan0 python-pip-whl python3-crypto python3-dev
  python3-distutils python3-keyring python3-keyrings.alt python3-lib2to3
  python3-pip python3-secretstorage python3-setuptools python3-wheel
  python3-xdg python3.6-dev
The following packages will be upgraded:
  cpp-7 gcc-7-base gcc-8-base libexpat1 libgcc1 libpython3.6
  libpython3.6-minimal libpython3.6-stdlib libstdc++6 python3-pkg-resources
  python3.6 python3.6-minimal
12 upgraded, 43 newly installed, 0 to remove and 268 not upgraded.
changed: [host2]
The following additional packages will be installed:
  build-essential cpp-7 dh-python dpkg-dev fakeroot g++ g++-7 gcc gcc-7
  gcc-7-base gcc-8-base libalgorithm-diff-perl libalgorithm-diff-xs-perl
  libalgorithm-merge-perl libasan4 libatomic1 libcc1-0 libcilkrts5
  libdpkg-perl libexpat1 libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-7-dev libgcc1 libgomp1 libitm1 liblsan0 libmpx2 libpython3-dev
  libpython3.6 libpython3.6-dev libpython3.6-minimal libpython3.6-stdlib
  libquadmath0 libstdc++-7-dev libstdc++6 libtsan0 libubsan0 python-pip-whl
  python3-crypto python3-dev python3-distutils python3-keyring
  python3-keyrings.alt python3-lib2to3 python3-pkg-resources
  python3-secretstorage python3-setuptools python3-wheel python3-xdg python3.6
  python3.6-dev python3.6-minimal
Suggested packages:
  gcc-7-locales debian-keyring g++-multilib g++-7-multilib gcc-7-doc
  libstdc++6-7-dbg gcc-multilib manpages-dev autoconf automake libtool flex
  bison gdb gcc-doc gcc-7-multilib libgcc1-dbg libgomp1-dbg libitm1-dbg
  libatomic1-dbg libasan4-dbg liblsan0-dbg libtsan0-dbg libubsan0-dbg
  libcilkrts5-dbg libmpx2-dbg libquadmath0-dbg bzr libstdc++-7-doc
  python-crypto-doc gnome-keyring libkf5wallet-bin gir1.2-gnomekeyring-1.0
  python-secretstorage-doc python-setuptools-doc python3.6-venv python3.6-doc
  binfmt-support
The following NEW packages will be installed:
  build-essential dh-python dpkg-dev fakeroot g++ g++-7 gcc gcc-7
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan4 libatomic1 libcc1-0 libcilkrts5 libdpkg-perl libexpat1-dev
  libfakeroot libfile-fcntllock-perl libgcc-7-dev libgomp1 libitm1 liblsan0
  libmpx2 libpython3-dev libpython3.6-dev libquadmath0 libstdc++-7-dev
  libtsan0 libubsan0 python-pip-whl python3-crypto python3-dev
  python3-distutils python3-keyring python3-keyrings.alt python3-lib2to3
  python3-pip python3-secretstorage python3-setuptools python3-wheel
  python3-xdg python3.6-dev
The following packages will be upgraded:
  cpp-7 gcc-7-base gcc-8-base libexpat1 libgcc1 libpython3.6
  libpython3.6-minimal libpython3.6-stdlib libstdc++6 python3-pkg-resources
  python3.6 python3.6-minimal
12 upgraded, 43 newly installed, 0 to remove and 268 not upgraded.
changed: [host1]

TASK [docker : Install docker] **************************************************
included: /home/xdr/UNI/DevOps/labs/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for host1, host2

TASK [docker : Install dependencies] ********************************************
ok: [host1]
ok: [host2]

TASK [docker : Add apt key] *****************************************************
ok: [host1]
ok: [host2]

TASK [docker : Add repository] **************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [host1]
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [host2]

TASK [docker : Install Docker] **************************************************
ok: [host1]
ok: [host2]

TASK [docker : Install docker-compose] ******************************************
included: /home/xdr/UNI/DevOps/labs/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for host1, host2

TASK [docker : Install dependencies] ********************************************
ok: [host2]
ok: [host1]

TASK [docker : Upgrade pip] *****************************************************
changed: [host1]
changed: [host2]

TASK [docker : Install docker-compose with pip] *********************************
changed: [host2]
changed: [host1]

PLAY RECAP **********************************************************************
host1                      : ok=25   changed=11   unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   
host2                      : ok=25   changed=11   unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   
```

#### ansible-inventory -i inventory/inventory.txt --list
```
{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_host": "127.0.0.1",
                "ansible_port": 2222,
                "ansible_ssh_extra_args": "-o IdentitiesOnly=yes",
                "ansible_ssh_private_key_file": "./inventory/vagrant/.vagrant/machines/host1/virtualbox/private_key",
                "ansible_user": "vagrant"
            },
            "host2": {
                "ansible_host": "127.0.0.1",
                "ansible_port": 2200,
                "ansible_ssh_extra_args": "-o IdentitiesOnly=yes",
                "ansible_ssh_private_key_file": "./inventory/vagrant/.vagrant/machines/host2/virtualbox/private_key",
                "ansible_user": "vagrant"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "app"
        ]
    },
    "app": {
        "hosts": [
            "host1",
            "host2"
        ]
    }
}
```
