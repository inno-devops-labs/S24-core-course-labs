# Ansible

## Command Executions

``ansible-playbook playbooks/dev/main.yml --diff``

```console
ansible-playbook playbooks/dev/main.yml --diff

PLAY [Install Docker] **************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [terraform1]

TASK [docker : Update apt cache] ***************************************************************************************
changed: [terraform1]

TASK [docker : Install pip] ********************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker dependencies] ****************************************************************************
ok: [terraform1] => (item=apt-transport-https)
ok: [terraform1] => (item=ca-certificates)
ok: [terraform1] => (item=curl)
ok: [terraform1] => (item=gnupg-agent)
ok: [terraform1] => (item=software-properties-common)

TASK [docker : Remove conflicting Docker GPG keys] *********************************************************************
ok: [terraform1]

TASK [docker : Clear APT cache] ****************************************************************************************
ok: [terraform1]

TASK [docker : Create directory for apt keyrings] **********************************************************************
ok: [terraform1]

TASK [docker : Download Docker GPG key] ********************************************************************************
changed: [terraform1]

TASK [docker : Add Docker GPG key] *************************************************************************************
changed: [terraform1]

TASK [docker : Set permissions for Docker GPG key] *********************************************************************
ok: [terraform1]

TASK [docker : Ensure correct Docker repository configuration] *********************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable

changed: [terraform1]

TASK [docker : Install Docker] *****************************************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 18 not upgraded.
changed: [terraform1]

TASK [docker : Install Docker Compose] *********************************************************************************
changed: [terraform1]

TASK [docker : Add Docker GPG key] *************************************************************************************
ok: [terraform1]

TASK [docker : Add Docker repository] **********************************************************************************
ok: [terraform1]

TASK [docker : Install Docker] *****************************************************************************************
ok: [terraform1]

TASK [docker : Install Docker Compose] *********************************************************************************
ok: [terraform1]

PLAY RECAP *************************************************************************************************************
terraform1                 : ok=17   changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

``ansible-inventory -i inventory/yandex_cloud.yml --list``

```console
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "62.84.114.89",
                "ansible_user": "ubuntu"
            }
        }
    },
    "all": {
        "children": [
            "myhosts",
            "ungrouped"
        ]
    },
    "myhosts": {
        "hosts": [
            "terraform1"
        ]
    }
}
```

``terraform1`` is our Yandex Cloud host.
