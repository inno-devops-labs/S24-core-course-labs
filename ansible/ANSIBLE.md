# Ansible lab results

<br> <br/>

# Best practicies

- Document playbooks and roles effectively to provide clear understanding and usage instructions
- Use Fully Qualified Class Names (FQCN) for builtin module actions to provide clear and unambiguous references to the modules being used in Ansible playbooks
- Use `ansible-lint` to check Ansible playbooks and roles for style violations
- Secrets in Ansible can be stored and managed using Ansible Vault, which provides encryption for sensitive data such as passwords, API keys, and other credentials
- Organize the directory layout in Ansible effectively to improve readability, maintainability, and reusability of playbooks, roles, and associated resources

<br> <br/>
<br> <br/>
<br> <br/>

# Main task

## `ansible-playbook playbooks/dev/main.yml --diff` output:

```text

PLAY [Install Docker on cloud] **************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************
ok: [host1]

TASK [docker : Install pip] *****************************************************************************************************************************************************
included: /Users/timur/develop/labs/devops/S24-core-course-labs/ansible/roles/docker/tasks/install_pip.yml for host1

TASK [docker : Update apt] ******************************************************************************************************************************************************
changed: [host1]

TASK [docker : Upgrade apt] *****************************************************************************************************************************************************
Calculating upgrade...
The following packages will be upgraded:
  python3-cryptography
1 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
changed: [host1]

TASK [docker : Install python] **************************************************************************************************************************************************
ok: [host1]

TASK [docker : Install pip] *****************************************************************************************************************************************************
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
changed: [host1]

TASK [docker : Install docker] **************************************************************************************************************************************************
included: /Users/timur/develop/labs/devops/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for host1

TASK [docker : Install docker] **************************************************************************************************************************************************
The following additional packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base pigz runc ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils containerd dns-root-data dnsmasq-base docker.io pigz runc
  ubuntu-fan
0 upgraded, 8 newly installed, 0 to remove and 0 not upgraded.
changed: [host1]

TASK [docker : Install docker-compose] ******************************************************************************************************************************************
included: /Users/timur/develop/labs/devops/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for host1

TASK [docker : Install docker compose] ******************************************************************************************************************************************
The following additional packages will be installed:
  python3-docker python3-dockerpty python3-docopt python3-dotenv
  python3-texttable python3-websocket
The following NEW packages will be installed:
  docker-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-texttable python3-websocket
0 upgraded, 7 newly installed, 0 to remove and 0 not upgraded.
changed: [host1]

PLAY RECAP **********************************************************************************************************************************************************************
host1                      : ok=10   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  

```

<br> <br/>

## `ansible-inventory -i inventory/default_cloud.yml --list` output:

```json

{
    "_meta": {
        "hostvars": {
            "host1": {
                "ansible_host": "188.225.76.110",
                "ansible_user": "root"
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
            "host1"
        ]
    }
}

```
<br> <br/>

Proof of installed using ssh:

![](./images/screen.png)

<br> <br/>
<br> <br/>
<br> <br/>

# Dynamic Inventory

I studies all CLI commands, but TimeWeb.cloud doesn't have dynamic inventory
https://timeweb.cloud/docs/twc-cli

BUT, lector said that if you cloud service doesn't have it, we will give you bonus points if you tried

It is because they are selling their own mechanism to increase raising the load level
https://timeweb.com/ru/docs/virtualnyj-hosting/voprosy-po-nagruzke/uvelichenie-limita-nagruzki/

## `ansible-inventory -e timeweb_token=$SECRET --list` output:

```json

    empty :(

```