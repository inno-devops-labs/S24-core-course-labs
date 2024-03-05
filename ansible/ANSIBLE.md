
# Console Outputs

## Deployment
> Using custom docker role
```console
$ ansible-playbook playbooks/dev/main.yml --diff | tail -50
PLAY [Install Docker] **********************************************************

TASK [Gathering Facts] *********************************************************
ok: [yandex_cloud_vm]

TASK [docker : Install Docker] *************************************************
included: /home/nabuki/repos/study/devops-labs/ansible/roles/docker/tasks/install_docker.yml for yandex_cloud_vm

TASK [docker : Install aptitude] ***********************************************
ok: [yandex_cloud_vm]

TASK [docker : Install required system packages] *******************************
ok: [yandex_cloud_vm]

TASK [docker : Add Docker GPG apt Key] *****************************************
changed: [yandex_cloud_vm]

TASK [docker : Add Docker Repository] ******************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu focal stable

changed: [yandex_cloud_vm]

TASK [docker : Update apt and install docker-ce] *******************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 3 not upgraded.
changed: [yandex_cloud_vm]

TASK [docker : Install docker-compose] *****************************************
included: /home/nabuki/repos/study/devops-labs/ansible/roles/docker/tasks/install_compose.yml for yandex_cloud_vm

TASK [docker : Install docker-compose] *****************************************
changed: [yandex_cloud_vm]

TASK [docker : Add user to docker group] ***************************************
changed: [yandex_cloud_vm]

PLAY RECAP *********************************************************************
yandex_cloud_vm            : ok=10   changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Inventory

### Details

Inventory is simple static defined

### Console Output

```console
$ ansible-inventory -i inventory/main.yml --list
{
    "_meta": {
        "hostvars": {
            "yandex_cloud_vm": {
                "ansible_host": "51.250.14.193"
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
            "yandex_cloud_vm"
        ]
    }
}
```