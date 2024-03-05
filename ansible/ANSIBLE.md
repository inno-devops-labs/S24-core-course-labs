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
