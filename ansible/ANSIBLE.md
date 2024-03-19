# Configuring Ansible 

### Best Practices
- ansible project structure is following ansible standards


## Docker role
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

## Web_app role

Is used to deploy MSK Time web application.

### Outputs
Both outputs are obtained while being in `ansible` folder.

When `web_app_full_wipe` is false:
```bash
$ ansible-playbook playbooks/dev/main.yaml --diff
LAY [Docker roles] *********************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************
ok: [host_01]

TASK [docker : Install python3-pip] *****************************************************************************************************************
ok: [host_01]

TASK [docker : include_tasks] ***********************************************************************************************************************
included: /home/anastasia/Documents/devops/ansible/roles/docker/tasks/install_docker.yml for host_01

TASK [docker : Docker installation] *****************************************************************************************************************
ok: [host_01]

TASK [docker : include_tasks] ***********************************************************************************************************************
included: /home/anastasia/Documents/devops/ansible/roles/docker/tasks/install_compose.yml for host_01

TASK [docker : Docker-compose installation] *********************************************************************************************************
ok: [host_01]

TASK [web_app : Stop and remove containers] *********************************************************************************************************
skipping: [host_01]

TASK [web_app : Ensure that directory exist] ********************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "app_python/",
-    "state": "absent"
+    "state": "directory"
 }

changed: [host_01]

TASK [web_app : Upload docker-compose.yml] **********************************************************************************************************
--- before
+++ after: /home/anastasia/.ansible/tmp/ansible-local-57140i36jj0d2/tmp0fj4tcl6/docker-compose.yml.j2
@@ -0,0 +1,4 @@
+services: 
+    web_app:
+        image: "vikono/devops:latest"
+        
\ No newline at end of file

changed: [host_01]

TASK [web_app : Pull image] *************************************************************************************************************************
changed: [host_01]

TASK [web_app : Start docker container] *************************************************************************************************************
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

PLAY RECAP ******************************************************************************************************************************************
host_01                    : ok=10   changed=4    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

When `web_app_full_wipe` is true:
```bash
$ ansible-playbook playbooks/dev/main.yaml --diff
-/-/-/-

TASK [web_app : Stop and remove containers] ***************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
-    "exists": true,
-    "running": true
+    "exists": false,
+    "running": false
 }

changed: [host_01]

TASK [web_app : Ensure that directory exist] **************************************************************************************************
ok: [host_01]

TASK [web_app : Upload docker-compose.yml] ****************************************************************************************************
ok: [host_01]

TASK [web_app : Pull image] *******************************************************************************************************************
ok: [host_01]

TASK [web_app : Start docker container] *******************************************************************************************************
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

PLAY RECAP ************************************************************************************************************************************
host_01                    : ok=11   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```