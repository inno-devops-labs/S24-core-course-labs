# Lab 5: Ansible and Docker Deployment

## 2

1. Need to add yacloud_compute plugin. add file `plugins/inventory/yacloud_compute`
2. Add inventory `yacloud_compute.yml`:

    ```yaml
    plugin: yacloud_compute
    ```

3. Aquire yc token, put it in some file, add filename to `yacloud_compute.yml`

4. Run playbook:

```bash
$ ansible-playbook playbooks/dev/main.yaml --diff
...
  gcc-11-multilib apache2 | lighttpd | httpd glibc-doc bzr libgd-tools
  libstdc++-11-doc make-doc python3-doc python3-tk python3-venv
  python3.10-venv python3.10-doc binfmt-support
Recommended packages:
  libnss-nis libnss-nisplus
The following NEW packages will be installed:
  apt-transport-https build-essential bzip2 cpp cpp-11 dpkg-dev fakeroot
  fontconfig-config fonts-dejavu-core g++ g++-11 gcc gcc-11 gcc-11-base
  javascript-common libalgorithm-diff-perl libalgorithm-diff-xs-perl
  libalgorithm-merge-perl libasan6 libatomic1 libc-dev-bin libc-devtools
  libc6-dev libcc1-0 libcrypt-dev libdeflate0 libdpkg-perl libexpat1-dev
  libfakeroot libfile-fcntllock-perl libfontconfig1 libgcc-11-dev libgd3
  libgomp1 libisl23 libitm1 libjbig0 libjpeg-turbo8 libjpeg8 libjs-jquery
  libjs-sphinxdoc libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-pip python3-wheel python3.10-dev
  rpcsvc-proto zlib1g-dev
The following packages will be upgraded:
  gcc-12-base libc6 libexpat1 libgcc-s1 libpython3-stdlib libpython3.10
  libpython3.10-minimal libpython3.10-stdlib libstdc++6 python3
  python3-distutils python3-lib2to3 python3-minimal python3.10
  python3.10-minimal zlib1g
16 upgraded, 65 newly installed, 0 to remove and 194 not upgraded.
changed: [yandex-cloud]

TASK [docker : include_tasks] **************************************************
included: /home/roxy/Study/DevOps/ansible/roles/docker/tasks/install_docker.yml for yandex-cloud

TASK [docker : Add Docker apt key.] ********************************************
changed: [yandex-cloud]

TASK [docker : Add Docker repository.] *****************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [yandex-cloud]

TASK [docker : Install Docker packages.] ***************************************
skipping: [yandex-cloud]

TASK [docker : include_tasks] **************************************************
included: /home/roxy/Study/DevOps/ansible/roles/docker/tasks/install_compose.yml for yandex-cloud

TASK [docker : Install docker-compose using pip.] ******************************
changed: [yandex-cloud]

PLAY RECAP *********************************************************************
yandex-cloud               : ok=8    changed=4    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```

```bash
$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex-cloud": {
                "ansible_host": "178.154.223.174",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
                "ansible_user": "diana"
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
            "yandex-cloud"
        ]
    }
}
```

## Bonus Task: Dynamic Inventory

I've implemented dynamic inventory using [terraform-inventory](https://github.com/adammck/terraform-inventory), this tool simply creates ansible inventory from terraform state. So, I create my infrastructure with terraform and then using its state to create ansible inventory.

Here is `➜ ansible-inventory --list` output:

```bash
    {
        "_meta": {
            "hostvars": {
                "terraform1": {
                    "ansible_host": "178.154.223.174"
                }
            }
        },
        "all": {
            "children": [
                "ungrouped",
                "yacloud"
            ]
        },
        "yacloud": {
            "hosts": [
                "terraform1"
            ]
        }
    }
```

## Deploy python app

```bash
    +        "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
    +        "LANG=C.UTF-8",
    +        "PATH=/home/app/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    +        "PYTHON_GET_PIP_SHA256=dfe9fd5c28dc98b5ac17979a953ea550cec37ae1b47a5116007395bfacff2ab9",
    +        "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/dbf0c85f76fb6e1ab42aa672ffca6f0a675d9ee4/public/get-pip.py",
    +        "PYTHON_PIP_VERSION=23.0.1",
    +        "PYTHON_SETUPTOOLS_VERSION=58.1.0",
    +        "PYTHON_VERSION=3.9.18"
        ],
    -    "image": "sha256:51093643b14f456a2d8c9c0f06feda88d73e11be4c889d6a59e68a70d47c118d",
    +    "image": "sha256:0ab53fef5d599aa980830fd55209edcff9d9c057eda46df6b4203a5b0f4ab114",
        "running": true
    }

    [DEPRECATION WARNING]: The default value "ignore" for image_name_mismatch has been deprecated and will change to "recreate" in
    community.docker 4.0.0. In the current situation, this would cause the container to be recreated since the current 
    container's image name "dianatomiya/python_devops:latest" does not match the desired image name "dianatomiya/devops:p_v1.0". 
    This feature will be removed from community.docker in version 4.0.0. Deprecation warnings can be disabled by setting 
    deprecation_warnings=False in ansible.cfg.
    changed: [terraform1]

    TASK [web_app : Create a directory for docker-compose if it does not exist.] **************************************************
    --- before
    +++ after
    @@ -1,4 +1,4 @@
    {
        "path": "/tmp/dianatomiya/devops:p_v1.0",
    -    "state": "absent"
    +    "state": "directory"
    }

    changed: [terraform1]

    TASK [web_app : Deliver docker compose to the host.] **************************************************************************
    --- before
    +++ after: /home/roxy/.ansible/tmp/ansible-local-1830786z21853z/tmp9liu9es8/docker-compose.yml.j2
    @@ -0,0 +1,7 @@
    +version: '3.10'
    +
    +services:
    +  app:
    +    image: dianatomiya/devops:p_v1.0:latest
    +    ports:
    +      - "80:80"
    \ No newline at end of file

    changed: [terraform1]

    PLAY RECAP ********************************************************************************************************************
    terraform1                 : ok=14   changed=5    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

```

## Deploy go app

```bash
    +++ after
    @@ -1,20 +1,13 @@
    {
        "env": [
    -        "GPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568",
    -        "LANG=C.UTF-8",
    -        "PATH=/home/app/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    -        "PYTHON_GET_PIP_SHA256=dfe9fd5c28dc98b5ac17979a953ea550cec37ae1b47a5116007395bfacff2ab9",
    -        "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/dbf0c85f76fb6e1ab42aa672ffca6f0a675d9ee4/public/get-pip.py",
    -        "PYTHON_PIP_VERSION=23.0.1",
    -        "PYTHON_SETUPTOOLS_VERSION=58.1.0",
    -        "PYTHON_VERSION=3.9.18"
    +        "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        ],
        "exposed_ports": [
    -        "80/tcp"
    +        "8080/tcp"
        ],
    -    "image": "sha256:0ab53fef5d599aa980830fd55209edcff9d9c057eda46df6b4203a5b0f4ab114",
    +    "image": "sha256:ecfbab7f7f36ed36be4492989049d09f1c5e451a4c5b539946ecd60f164f15c4",
        "published_ports": {
    -        "80/tcp": [
    +        "8080/tcp": [
                {
                    "HostIp": "0.0.0.0",
                    "HostPort": "80"

    [DEPRECATION WARNING]: The default value "ignore" for image_name_mismatch has been deprecated and will change to "recreate" in
    community.docker 4.0.0. In the current situation, this would cause the container to be recreated since the current 
    container's image name "dianatomiya/devops:p_v1.0" does not match the desired image name "dianatomiya/devops:g_v1.0". This 
    feature will be removed from community.docker in version 4.0.0. Deprecation warnings can be disabled by setting 
    deprecation_warnings=False in ansible.cfg.
    changed: [terraform1]

    TASK [web_app : Create a directory for docker-compose if it does not exist.] **************************************************
    --- before
    +++ after
    @@ -1,4 +1,4 @@
    {
        "path": "/tmp/dianatomiya/devops:g_v1.0",
    -    "state": "absent"
    +    "state": "directory"
    }

    changed: [terraform1]

    TASK [web_app : Deliver docker compose to the host.] **************************************************************************
    --- before
    +++ after: /home/roxy/.ansible/tmp/ansible-local-265954opr1c8ge/tmppedy5rhd/docker-compose.yml.j2
    @@ -0,0 +1,7 @@
    +version: '3.10'
    +
    +services:
    +  app:
    +    image: dianatomiya/devops:g_v1.0:latest
    +    ports:
    +      - "80:80"
    \ No newline at end of file

    changed: [terraform1]

    TASK [web_app : include_tasks] ************************************************************************************************
    skipping: [terraform1]

    PLAY RECAP ********************************************************************************************************************
    terraform1                 : ok=14   changed=5    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
```
