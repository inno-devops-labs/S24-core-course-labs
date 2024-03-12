
## CLI Outputs

### Docker Deployment

1. `ansible-playbook playbooks/dev/main.yml --diff`

    ```text

      python3-distutils python3-keyring python3-keyrings.alt python3-lib2to3
      python3-secretstorage python3-setuptools python3-wheel python3-xdg
      python3.6-dev
    Suggested packages:
      binutils-doc cpp-doc gcc-7-locales debian-keyring g++-multilib
      g++-7-multilib gcc-7-doc libstdc++6-7-dbg gcc-multilib autoconf automake
      libtool flex bison gdb gcc-doc gcc-7-multilib libgcc1-dbg libgomp1-dbg
      libitm1-dbg libatomic1-dbg libasan4-dbg liblsan0-dbg libtsan0-dbg
      libubsan0-dbg libcilkrts5-dbg libmpx2-dbg libquadmath0-dbg glibc-doc bzr
      libstdc++-7-doc make-doc python-crypto-doc gnome-keyring libkf5wallet-bin
      gir1.2-gnomekeyring-1.0 python-secretstorage-doc python-setuptools-doc
    The following NEW packages will be installed:
      binutils binutils-common binutils-x86-64-linux-gnu build-essential cpp cpp-7
      dh-python dpkg-dev fakeroot g++ g++-7 gcc gcc-7 gcc-7-base
      libalgorithm-diff-perl libalgorithm-diff-xs-perl libalgorithm-merge-perl
      libasan4 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0 libcilkrts5
      libdpkg-perl libexpat1-dev libfakeroot libfile-fcntllock-perl libgcc-7-dev
      libgomp1 libisl19 libitm1 liblsan0 libmpc3 libmpfr6 libmpx2 libpython3-dev
      libpython3.6-dev libquadmath0 libstdc++-7-dev libtsan0 libubsan0
      linux-libc-dev make manpages-dev python-pip-whl python3-crypto python3-dev
      python3-distutils python3-keyring python3-keyrings.alt python3-lib2to3
      python3-pip python3-secretstorage python3-setuptools python3-wheel
      python3-xdg python3.6-dev
    0 upgraded, 58 newly installed, 0 to remove and 9 not upgraded.
    changed: [host_01]

    TASK [docker : Install Docker Compose using pip] *******************************
    changed: [host_01]

    TASK [web_app : Pull the Docker image] *****************************************
    changed: [host_01]

    TASK [web_app : Run the Docker container] **************************************
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

    RUNNING HANDLER [docker : Restart Docker] **************************************
    changed: [host_01]

    PLAY RECAP *********************************************************************
    host_01                    : ok=13   changed=9    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

    ```

2. `ansible-inventory --list`

    ```json
    {
        "_meta": {
            "hostvars": {
                "host_01": {
                    "ansible_host": "178.154.220.110",
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
    ```
