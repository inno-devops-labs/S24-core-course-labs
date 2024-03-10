Firstly I tested with `geerlingguy.docker` acording to task 1, then I wrote the custom 
docker role. 

- `./inventory/default_yandex_cloud.yml`
Inventory defines one host machine `host_01` with IP address and `bulatok` user.
- `./playbooks/dev/main.yml` has one playbook for custom docker role
- `./roles/docker` - custom docker role
- `./ansible.ctg` - specifies the default inventory file to use 





### Deployment Output
```bash
ansible-playbook playbooks/dev/main.yml --diff
```
last 50 lines (according to the task)
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
0 upgraded, 64 newly installed, 0 to remove and 13 not upgraded.
changed: [host_01]

TASK [../../roles/docker : Install required system packages] *****************************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : Add Docker GPG key] *******************************************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : Add Docker Repository] ****************************************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : Install Docker] ***********************************************************************************************************************************
ok: [host_01]

TASK [../../roles/docker : Install Docker Compose] ***************************************************************************************************************************
changed: [host_01]

PLAY RECAP *******************************************************************************************************************************************************************
host_01                    : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory Details
```bash
ansible-inventory -i inventory --list
```
```
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "84.201.130.157",
                "ansible_user": "bulatok"
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

## Lab 6

### Task 1
```bash
ansible-playbook playbooks/dev/app_python/main.yml -i inventory
```

```
PLAY [Deploy python app] *****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [host_01]

TASK [../../../roles/web_app : Directory create] *****************************************************************************************************************************
changed: [host_01]

TASK [../../../roles/web_app : Docker compose file] **************************************************************************************************************************
changed: [host_01]

TASK [../../../roles/web_app : Start the app] ********************************************************************************************************************************
changed: [host_01]

PLAY RECAP *******************************************************************************************************************************************************************
host_01                    : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

Checking on server
```
bulatok@devops-lab-06:~$ sudo docker images
REPOSITORY            TAG       IMAGE ID       CREATED       SIZE
bulatok4/app_python   latest    6ce1b7549c02   2 weeks ago   118MB

bulatok@devops-lab-06:~$ sudo docker ps
CONTAINER ID   IMAGE                 COMMAND            CREATED              STATUS              PORTS                                       NAMES
09e1251c6519   bulatok4/app_python   "python main.py"   About a minute ago   Up About a minute   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   app_python-web_app-1

bulatok@devops-lab-06:~$ curl http://127.0.0.1:8080
{"time":"2024-03-10 20:39:44"}
```

## Task 2
Running only wipe 
```bash
ansible-playbook playbooks/dev/app_python/main.yml -i inventory --tags "wipe"
```
```bash
PLAY [Deploy python app] *****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [host_01]

TASK [../../../roles/web_app : Remove app image, container, volumes] *********************************************************************************************************
changed: [host_01]

TASK [../../../roles/web_app : Remove app directory] *************************************************************************************************************************
changed: [host_01]

PLAY RECAP *******************************************************************************************************************************************************************
host_01                    : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

All in one
```bash
ansible-playbook playbooks/dev/app_python/main.yml -i inventory
```

```bash
PLAY [Deploy python app] *****************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [host_01]

TASK [docker : Install `pip`] ************************************************************************************************************************************************
ok: [host_01]

TASK [docker : Install required system packages] *****************************************************************************************************************************
ok: [host_01]

TASK [docker : Add Docker GPG key] *******************************************************************************************************************************************
ok: [host_01]

TASK [docker : Add Docker Repository] ****************************************************************************************************************************************
ok: [host_01]

TASK [docker : Install Docker] ***********************************************************************************************************************************************
ok: [host_01]

TASK [docker : Install Docker Compose] ***************************************************************************************************************************************
ok: [host_01]

TASK [../../../roles/web_app : Directory create] *****************************************************************************************************************************
ok: [host_01]

TASK [../../../roles/web_app : Docker compose file] **************************************************************************************************************************
ok: [host_01]

TASK [../../../roles/web_app : Start the app] ********************************************************************************************************************************
ok: [host_01]

TASK [../../../roles/web_app : Remove app image, container, volumes] *********************************************************************************************************
changed: [host_01]

TASK [../../../roles/web_app : Remove app directory] *************************************************************************************************************************
changed: [host_01]

PLAY RECAP *******************************************************************************************************************************************************************
host_01                    : ok=12   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```