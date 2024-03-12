# Ansible.md

I tested `geerlingguy.docker` (task 1)

Then I create my own similar docker role (task 2)

- `./inventory/default_yc_ec_2.yml`
Inventory has a host machine `host_01` with IP address and `ubuntu` user.
- `./playbooks/dev/main.yml` contains a playbook for my docker role
- `./roles/docker` - custom docker role

## Deployment Output

Last 50 lines of `ansible-playbook playbooks/dev/main.yml --diff -i inventory/default_yc_ec2.yml`:

```text
PLAY [Install docker and pip] ****************************************************************

TASK [Gathering Facts] ***********************************************************************
ok: [host_01]

TASK [../../roles/docker : Install pip] ******************************************************
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
0 upgraded, 64 newly installed, 0 to remove and 0 not upgraded.
changed: [host_01]

TASK [../../roles/docker : Install dependencies] *********************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

TASK [../../roles/docker : Add Docker GPG key] ***********************************************
changed: [host_01]

TASK [../../roles/docker : Add Docker repository] ********************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable

changed: [host_01]

TASK [../../roles/docker : Install Docker] ***************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 3 not upgraded.
changed: [host_01]

TASK [../../roles/docker : Install Docker Compose] *******************************************
changed: [host_01]

PLAY RECAP ***********************************************************************************
host_01                    : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Inventory Details

Output of `ansible-inventory -i inventory/default_yc_ec2.yml --list`

```text
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "51.250.95.217",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "my_hosts"
        ]
    },
    "my_hosts": {
        "hosts": [
            "host_01"
        ]
    }
}
```

## Lab 6, Task 1: Application Deployment

The last 50 lines of the output from your deployment command:

```bash
ansible-playbook playbooks/app_python/main.yml --diff -i inventory/default_yc_ec2.yml
```

```text
PLAY [Deploy python app to yandex cloud] ****************************************************

TASK [Gathering Facts] **********************************************************************
ok: [host_01]

TASK [docker : Install pip] *****************************************************************
ok: [host_01]

TASK [docker : Install dependencies] ********************************************************
ok: [host_01]

TASK [docker : Add Docker GPG key] **********************************************************
ok: [host_01]

TASK [docker : Add Docker repository] *******************************************************
ok: [host_01]

TASK [docker : Install Docker] **************************************************************
ok: [host_01]

TASK [docker : Install Docker Compose] ******************************************************
ok: [host_01]

TASK [../../../roles/web_app : Make workdir] ************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "app_python/",
-    "state": "absent"
+    "state": "directory"
 }

changed: [host_01]

TASK [../../../roles/web_app : Docker-compose file] *****************************************
--- before
+++ after: /home/anron/.ansible/tmp/ansible-local-848602xkqmcpom/tmpjpk6v82_/docker-compose.yml.j2
@@ -0,0 +1,6 @@
+version: '3'
+services:
+  web_app:
+    image: "pgrammer/app_python"
+    ports:
+      - "5000:5000"

changed: [host_01]

TASK [../../../roles/web_app : Launch the app] **********************************************
changed: [host_01]

TASK [../../../roles/web_app : Wipe Logic] **************************************************
skipping: [host_01]

TASK [../../../roles/web_app : Delete app dir] **********************************************
skipping: [host_01]

PLAY RECAP **********************************************************************************
host_01                    : ok=10   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

