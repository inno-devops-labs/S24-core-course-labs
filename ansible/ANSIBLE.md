## Deployment

```bash
ansible-playbook playbooks/dev/main.yml --diff
```

```
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
0 upgraded, 64 newly installed, 0 to remove and 13 not upgraded.
changed: [host_1]

TASK [../../roles/docker : Install required system packages] *****************************************************************************************************************
ok: [host_1]

TASK [../../roles/docker : Add Docker GPG key] *******************************************************************************************************************************
ok: [host_1]

TASK [../../roles/docker : Add Docker Repository] ****************************************************************************************************************************
ok: [host_1]

TASK [../../roles/docker : Install Docker] ***********************************************************************************************************************************
ok: [host_1]

TASK [../../roles/docker : Install Docker Compose] ***************************************************************************************************************************
changed: [host_1]

PLAY RECAP *******************************************************************************************************************************************************************
host_1                    : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory

```bash
ansible-inventory -i inventory --list
```

```json
{
    "_meta": {
        "hostvars": {
            "host_1": {
                "ansible_host": "82.97.244.125",
                "ansible_user": "metafates"
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
            "host_1"
        ]
    }
}
```