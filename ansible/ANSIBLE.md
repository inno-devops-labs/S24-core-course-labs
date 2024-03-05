# ANSIBLE

## 1. INSTALLING DOCKER ROLE

```bash
ansible-galaxy role install geerlingguy.docker
```

## 2. ANSIBLE INVENTORY

```bash
ansible-inventory --list
```

Output:  
```
{
    "_meta": {
        "hostvars": {
            "ec2-3-71-79-119.eu-central-1.compute.amazonaws.com": {
                "ansible_connection": "ssh",
                "ansible_ssh_private_key_file": "~/.ssh/ansible-docker.pem",
                "ansible_user": "ubuntu",
                "docker_user": "ubuntu"
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
            "ec2-3-71-79-119.eu-central-1.compute.amazonaws.com"
        ]
    }
}
```

## 3. RUNNING ANSIBLE

```bash
ansible-playbook playbook/dev/main.yaml --diff
```

Output:  

```
(venv) tanmay@tanmay-ubuntu:~/Tanmay/Courses/Devops/S24-core-course-labs/ansible$ ansible-playbook playbook/dev/main.yaml --diff

PLAY [Install Docker and Docker Compose] *********************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************
ok: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install pip] **********************************************************************************************************************************
fatal: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]: FAILED! => {"changed": false, "msg": "No package matching 'python3-pip' is available"}

PLAY RECAP ***************************************************************************************************************************************************
ec2-3-71-79-119.eu-central-1.compute.amazonaws.com : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0   

(venv) tanmay@tanmay-ubuntu:~/Tanmay/Courses/Devops/S24-core-course-labs/ansible$ ansible-playbook playbook/dev/main.yaml --diff

PLAY [Install Docker and Docker Compose] *********************************************************************************************************************

TASK [Gathering Facts] ***************************************************************************************************************************************
ok: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : APT Update] ***********************************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install pip] **********************************************************************************************************************************
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
0 upgraded, 64 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install Docker dependencies] ******************************************************************************************************************
The following NEW packages will be installed:
  apt-transport-https gnupg-agent
0 upgraded, 2 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Add Docker's official GPG key] ****************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Add Docker's APT repository] ******************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu jammy stable

changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install Docker] *******************************************************************************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 35 not upgraded.
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

TASK [docker : Install Docker Compose via pip] ***************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

RUNNING HANDLER [docker : Ensure ubuntu has Docker group access] *********************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

RUNNING HANDLER [docker : Restart Docker] ********************************************************************************************************************
changed: [ec2-3-71-79-119.eu-central-1.compute.amazonaws.com]

PLAY RECAP ***************************************************************************************************************************************************
ec2-3-71-79-119.eu-central-1.compute.amazonaws.com : ok=10   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## BEST PRACTICES

1. ```ansible.cfg``` was used for settings.
2. Tasks were named before using.
3. Folder structure mentioned in the lab was used.