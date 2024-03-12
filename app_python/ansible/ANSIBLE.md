## Outputs | Docker

Using the command `ansible-playbook playbooks/dev/main.yaml --diff`

Gives the ouput

```text
PLAY [Install Docker] *********************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Install Docker] ************************************************************************************************************************
fatal: [yandex_vm]: FAILED! => {"reason": "Could not find or access '/Users/ykozyrenko/Desktop/course3/Devops/S24-core-course-labs/app_python/ansible/playbooks/dev/install_docker.yml' on the Ansible Controller."}

PLAY RECAP ********************************************************************************************************************************************
yandex_vm                  : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

❯ ansible-playbook playbooks/dev/main.yaml --diff

PLAY [Install Docker] *********************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Install Docker] ************************************************************************************************************************
included: /Users/ykozyrenko/Desktop/course3/Devops/S24-core-course-labs/app_python/ansible/roles/docker/tasks/install_docker.yaml for yandex_vm

TASK [docker : Install aptitude] **********************************************************************************************************************
The following additional packages will be installed:
  aptitude-common bzip2 libboost-iostreams1.74.0 libcwidget4 libdpkg-perl
  libfile-fcntllock-perl libsigc++-2.0-0v5 libxapian30
Suggested packages:
  apt-xapian-index aptitude-doc-en | aptitude-doc debtags tasksel bzip2-doc
  libcwidget-dev debian-keyring gcc | c-compiler bzr xapian-tools
The following NEW packages will be installed:
  aptitude aptitude-common bzip2 libboost-iostreams1.74.0 libcwidget4
  libdpkg-perl libfile-fcntllock-perl libsigc++-2.0-0v5 libxapian30
0 upgraded, 9 newly installed, 0 to remove and 3 not upgraded.
changed: [yandex_vm]

TASK [docker : Install required system packages] ******************************************************************************************************
The following additional packages will be installed:
  build-essential cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libexpat1-dev libfakeroot libfontconfig1
  libgcc-11-dev libgd3 libgomp1 libisl23 libitm1 libjbig0 libjpeg-turbo8
  libjpeg8 libjs-jquery libjs-sphinxdoc libjs-underscore liblsan0 libmpc3
  libnsl-dev libpython3-dev libpython3.10-dev libquadmath0 libstdc++-11-dev
  libtiff5 libtirpc-dev libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev
  lto-disabled-list make manpages-dev python3-dev python3-distlib
  python3-filelock python3-pip-whl python3-platformdirs python3-setuptools-whl
  python3-virtualenv python3-wheel python3-wheel-whl python3.10-dev
  rpcsvc-proto zlib1g-dev
Suggested packages:
  cpp-doc gcc-11-locales debian-keyring g++-multilib g++-11-multilib
  gcc-11-doc gcc-multilib autoconf automake libtool flex bison gdb gcc-doc
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc libgd-tools
  libstdc++-11-doc make-doc python2-pip-whl python2-setuptools-whl
The following NEW packages will be installed:
  build-essential cpp cpp-11 dpkg-dev fakeroot fontconfig-config
  fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base javascript-common
  libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
  libasan6 libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0
  libcrypt-dev libdeflate0 libexpat1-dev libfakeroot libfontconfig1
  libgcc-11-dev libgd3 libgomp1 libisl23 libitm1 libjbig0 libjpeg-turbo8
  libjpeg8 libjs-jquery libjs-sphinxdoc libjs-underscore liblsan0 libmpc3
  libnsl-dev libpython3-dev libpython3.10-dev libquadmath0 libstdc++-11-dev
  libtiff5 libtirpc-dev libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev
  lto-disabled-list make manpages-dev python3-dev python3-distlib
  python3-filelock python3-pip python3-pip-whl python3-platformdirs
  python3-setuptools-whl python3-virtualenv python3-wheel python3-wheel-whl
  python3.10-dev rpcsvc-proto virtualenv zlib1g-dev
0 upgraded, 69 newly installed, 0 to remove and 3 not upgraded.
changed: [yandex_vm]

TASK [docker : Add Docker GPG apt Key] ****************************************************************************************************************
ok: [yandex_vm]

TASK [docker : Add Docker Repository] *****************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu focal stable

changed: [yandex_vm]

TASK [docker : Update apt and install docker-ce] ******************************************************************************************************
ok: [yandex_vm]

TASK [docker : Install docker-compose] ****************************************************************************************************************
included: /Users/ykozyrenko/Desktop/course3/Devops/S24-core-course-labs/app_python/ansible/roles/docker/tasks/install_compose.yaml for yandex_vm

TASK [docker : Install docker-compose plugin] *********************************************************************************************************
changed: [yandex_vm]

TASK [docker : Add user to docker group] **************************************************************************************************************
changed: [yandex_vm]

PLAY RECAP ********************************************************************************************************************************************
yandex_vm                  : ok=10   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Inventory Details

```text
{
    "_meta": {
        "hostvars": {
            "yandex_vm": {
                "ansible_host": "62.84.126.157"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "yandex_vm"
        ]
    }
}
```


## Output for Lab 6

```text
ansible-playbook playbooks/dev/main.yaml --tags "deploy,wipe" --diff

PLAY [Install Docker] **************************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [yandex_vm]

PLAY [Deploy Web Application] ******************************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Create directory for the app] **************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Deploy compose.yaml] ***********************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Install pip] *******************************************************************************************************************
ok: [yandex_vm]

TASK [web_app : Start the app] *****************************************************************************************************************
ok: [yandex_vm]

TASK [web_app : include_tasks] *****************************************************************************************************************
skipping: [yandex_vm]

PLAY RECAP *************************************************************************************************************************************
yandex_vm                  : ok=6    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   

```