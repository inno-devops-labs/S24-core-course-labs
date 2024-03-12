# Ansible

Real server ip address is `redacted` using `/etc/hosts`. 

## Output of `ansible-playbook playbooks/dev/main.yml --diff`:

```

PLAY [Install docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [redacted]

TASK [docker : Install required system packages] *******************************
ok: [redacted]

TASK [docker : Add Docker's GPG key] *******************************************
changed: [redacted]

TASK [docker : Add Docker Repository] ******************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [redacted]

TASK [docker : Install Docker] *************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 2 not upgraded.
changed: [redacted]

TASK [docker : Install pip] ****************************************************
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
changed: [redacted]

TASK [docker : Install docker-compose] *****************************************
changed: [redacted]

PLAY RECAP *********************************************************************
redacted                   : ok=7    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

## Output of `ansible-inventory --list`

```
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "redacted"
        ]
    }
}
```

## Output of `ansible-playbook playbooks/dev/app_python/main.yml --diff`

```

PLAY [Install docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [redacted]

TASK [docker : Install required system packages] *******************************
ok: [redacted]

TASK [docker : Add Docker's GPG key] *******************************************
ok: [redacted]

TASK [docker : Add Docker Repository] ******************************************
ok: [redacted]

TASK [docker : Install Docker] *************************************************
ok: [redacted]

TASK [docker : Install pip] ****************************************************
ok: [redacted]

TASK [docker : Install docker-compose] *****************************************
ok: [redacted]

TASK [web_app : Create directory for web app] *******************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "app_python",
-    "state": "absent"
+    "state": "directory"
 }

changed: [redacted]

TASK [web_app : Render templated compose.yaml] ******************
--- before
+++ after: /home/user/.ansible/tmp/ansible-local-372619n03ho7rh/tmp57309pkm/docker-compose.yml.j2
@@ -0,0 +1,5 @@
+services:
+  web_app:
+    image: "masterlogick/devops-py-img"
+    ports:
+      - "8080:8080"

changed: [redacted]

TASK [web_app : Start web app] **********************************
changed: [redacted]

TASK [web_app : Remove web app artefacts] ***********************
skipping: [redacted]

TASK [web_app : Remove web app directory] ***********************
skipping: [redacted]

PLAY RECAP *********************************************************************
redacted                   : ok=10   changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

```

## Best practices

+ Use state where it is possible
+ Name all tasks
+ Use full task name
+ Explicit file mode and checksum validation for docker repo gpg key