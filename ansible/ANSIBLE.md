# Ansible

### CLI Outputs

1. `ansible-playbook playbooks/dev/main.yaml --diff`

```text
PLAY [Install Docker] *******************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
ok: [host_01]

TASK [docker : include_tasks] ***********************************************************************************************************
included: /home/vladdan/Documents/GitHub/DevOps/ansible/roles/docker/tasks/install_docker.yml for host_01

TASK [docker : Install apt dependencies] ************************************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 210 not upgraded.
changed: [host_01]

TASK [docker : Add Docker’s GPG key] ****************************************************************************************************
changed: [host_01]

TASK [docker : Add Docker apt repository] ***********************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable

changed: [host_01]

TASK [docker : Install Docker specific version] *****************************************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 210 not upgraded.
changed: [host_01]

TASK [docker : include_tasks] ***********************************************************************************************************
included: /home/vladdan/Documents/GitHub/DevOps/ansible/roles/docker/tasks/install_compose.yml for host_01

TASK [docker : Install pip] *************************************************************************************************************
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
  libstdc++-11-dev libstdc++6 libtiff5 libtirpc-dev libtsan0 libubsan1
  libwebp7 libxpm4 linux-libc-dev lto-disabled-list make manpages-dev python3
  python3-dev python3-distutils python3-lib2to3 python3-minimal python3-wheel
  python3.10 python3.10-dev python3.10-minimal rpcsvc-proto zlib1g zlib1g-dev
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
  libpython3.10-minimal libpython3.10-stdlib libstdc++6 python3
  python3-distutils python3-lib2to3 python3-minimal python3.10
  python3.10-minimal zlib1g
16 upgraded, 64 newly installed, 0 to remove and 195 not upgraded.
changed: [host_01]

TASK [docker : Install Docker Compose] **************************************************************************************************
changed: [host_01]

RUNNING HANDLER [docker : Restart Docker] ***********************************************************************************************
changed: [host_01]

PLAY RECAP ******************************************************************************************************************************
host_01                    : ok=10   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

2. `ansible-inventory -i inventory/default_yandex.yml --list`

```json
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "51.250.10.113",
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

# Web app Deployment

1. `ansible-playbook playbooks/dev/main.yaml --diff`

```text
TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] ***********************************************
ok: [host_01]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ****************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Configure Docker daemon options.] *********************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ********************************************************
ok: [host_01]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ****************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ****************************************************************************
changed: [host_01]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Get docker group info using getent.] ******************************************************************
skipping: [host_01]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *********************************************
skipping: [host_01]

TASK [geerlingguy.docker : include_tasks] ****************************************************************************************
skipping: [host_01]

TASK [web_app : Add user to Docker group] ****************************************************************************************
changed: [host_01]

TASK [web_app : Pull the Docker image] *******************************************************************************************
changed: [host_01]

TASK [web_app : Run the Docker container] ****************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": false,
-    "running": false
+    "exists": true,
+    "running": true
 }

changed: [host_01]

PLAY RECAP ***********************************************************************************************************************
host_01                    : ok=15   changed=8    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   
```

You can check deployed web app at http://158.160.97.139:8000/