## Ansible installation

### Docker role

```shell
ernest@DESKTOP-P1QFCL0:/mnt/c/Users/Ernest/Desktop/Matskevich/ansible$ ansible-playbook playbooks/dev/main.yaml --diff

TASK [../../roles/docker : Install pip3] *******************************************************************************The following additional packages will be installed:
  build-essential bzip2 cpp cpp-13 cpp-13-x86-64-linux-gnu
  cpp-x86-64-linux-gnu dpkg-dev fakeroot g++ g++-13 g++-13-x86-64-linux-gnu
  g++-x86-64-linux-gnu gcc gcc-13 gcc-13-base gcc-13-x86-64-linux-gnu
  gcc-x86-64-linux-gnu javascript-common libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libaom3 libasan8
  libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0 libcrypt-dev
  libde265-0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-13-dev libgd3 libgomp1 libheif-plugin-aomdec libheif-plugin-aomenc
  libheif-plugin-libde265 libheif1 libhwasan0 libisl23 libitm1 libjs-jquery
  libjs-sphinxdoc libjs-underscore liblsan0 libmpc3 libpython3-dev
  libpython3.12-dev libquadmath0 libstdc++-13-dev libtsan2 libubsan1 libxpm4
  linux-libc-dev lto-disabled-list make manpages-dev python3-dev python3-wheel
  python3.12-dev rpcsvc-proto zlib1g-dev
Suggested packages:
  bzip2-doc cpp-doc gcc-13-locales cpp-13-doc debian-keyring g++-multilib
  g++-13-multilib gcc-13-doc gcc-multilib autoconf automake libtool flex bison
  gdb gcc-doc gcc-13-multilib gdb-x86-64-linux-gnu apache2 | lighttpd | httpd
  glibc-doc bzr libgd-tools libheif-plugin-x265 libheif-plugin-ffmpegdec
  libheif-plugin-jpegdec libheif-plugin-jpegenc libheif-plugin-j2kdec
  libheif-plugin-j2kenc libheif-plugin-rav1e libheif-plugin-svtenc
  libstdc++-13-doc make-doc
The following NEW packages will be installed:
  build-essential bzip2 cpp cpp-13 cpp-13-x86-64-linux-gnu
  cpp-x86-64-linux-gnu dpkg-dev fakeroot g++ g++-13 g++-13-x86-64-linux-gnu
  g++-x86-64-linux-gnu gcc gcc-13 gcc-13-base gcc-13-x86-64-linux-gnu
  gcc-x86-64-linux-gnu javascript-common libalgorithm-diff-perl
  libalgorithm-diff-xs-perl libalgorithm-merge-perl libaom3 libasan8
  libatomic1 libc-dev-bin libc-devtools libc6-dev libcc1-0 libcrypt-dev
  libde265-0 libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl
  libgcc-13-dev libgd3 libgomp1 libheif-plugin-aomdec libheif-plugin-aomenc
  libheif-plugin-libde265 libheif1 libhwasan0 libisl23 libitm1 libjs-jquery
  libjs-sphinxdoc libjs-underscore liblsan0 libmpc3 libpython3-dev
  libpython3.12-dev libquadmath0 libstdc++-13-dev libtsan2 libubsan1 libxpm4
  linux-libc-dev lto-disabled-list make manpages-dev python3-dev python3-pip
  python3-wheel python3.12-dev rpcsvc-proto zlib1g-dev
0 upgraded, 66 newly installed, 0 to remove and 1 not upgraded.
changed: [localhost]

TASK [../../roles/docker : Install Docker Compose] *********************************************************************The following additional packages will be installed:
  python3-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-compose python3-docker python3-dockerpty
  python3-docopt python3-dotenv python3-texttable python3-websocket
0 upgraded, 8 newly installed, 0 to remove and 1 not upgraded.
changed: [localhost]

PLAY RECAP *************************************************************************************************************localhost                  : ok=10   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Inventory details

```shell
ernest@DESKTOP-P1QFCL0:/mnt/c/Users/Ernest/Desktop/Matskevich/ansible$ ansible-inventory -i inventory/default_aws_ec2.yml --list
[WARNING]: Ansible is being run in a world writable directory (/mnt/c/Users/Ernest/Desktop/Matskevich/ansible),
ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_connection": "local"
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
            "localhost"
        ]
    }
}
```
