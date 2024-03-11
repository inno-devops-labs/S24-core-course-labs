## Commands Output

`ansible-playbook playbooks/dev/main.yaml --diff`:

```bash
PLAY [Docker role] *****************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [terraform1]

TASK [docker : Update apt] *********************************************************************************************
changed: [terraform1]

TASK [docker : install dependencies] ***********************************************************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 199 not upgraded.
changed: [terraform1] => (item=apt-transport-https)
ok: [terraform1] => (item=ca-certificates)
ok: [terraform1] => (item=curl)
The following NEW packages will be installed:
  gnupg-agent
0 upgraded, 1 newly installed, 0 to remove and 199 not upgraded.
changed: [terraform1] => (item=gnupg-agent)
ok: [terraform1] => (item=software-properties-common)

TASK [docker : add GPG key] ********************************************************************************************
changed: [terraform1]

TASK [docker : add docker repository to apt] ***************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb https://download.docker.com/linux/ubuntu jammy stable

changed: [terraform1]

TASK [docker : install docker] *****************************************************************************************
The following packages were automatically installed and are no longer required:
  bridge-utils dns-root-data dnsmasq-base ubuntu-fan
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following packages will be REMOVED:
  containerd docker.io runc
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0
  slirp4netns
0 upgraded, 9 newly installed, 3 to remove and 199 not upgraded.
changed: [terraform1] => (item=docker-ce)
ok: [terraform1] => (item=docker-ce-cli)
ok: [terraform1] => (item=containerd.io)

TASK [docker : Install Docker Compose] *********************************************************************************
The following packages were automatically installed and are no longer required:
  bridge-utils dns-root-data dnsmasq-base ubuntu-fan
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  python3-docker python3-dockerpty python3-docopt python3-dotenv
  python3-texttable python3-websocket
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-docker python3-dockerpty python3-docopt
  python3-dotenv python3-texttable python3-websocket
0 upgraded, 7 newly installed, 0 to remove and 199 not upgraded.
changed: [terraform1]

PLAY RECAP *************************************************************************************************************
terraform1                 : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

`ansible-inventory -i inventory/default_yandex_cloud.yml --list`:

```bash
{
    "_meta": {
        "hostvars": {
            "terraform1": {
                "ansible_host": "158.160.115.31",
                "ansible_user": "ubuntu"
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
            "terraform1"
        ]
    }
}
```