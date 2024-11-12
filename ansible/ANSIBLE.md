# Ansible

## Installing Ansible
- If using nix: `nix-shell` in repository root
- Otherwise: pip3 install ansible

## Playbook

- Running:
```console
.../ansible $ ansible-playbook playbooks/dev/main.yaml -K --diff
BECOME password:

PLAY [Install Docker] **************************************************************************************

TASK [Gathering Facts] *************************************************************************************                                                                                                                               ok: [host_01]

TASK [docker : Upgrade pip] ********************************************************************************
ok: [host_01]

TASK [docker : apt update] *********************************************************************************
changed: [host_01]

TASK [docker : Install containerd] *************************************************************************
The following packages were automatically installed and are no longer required:
  libfwupdplugin1 pigz shim slirp4netns
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  runc
The following packages will be REMOVED:
  containerd.io
The following NEW packages will be installed:
  containerd runc
0 upgraded, 2 newly installed, 1 to remove and 81 not upgraded.
changed: [host_01]

The following packages were automatically installed and are no longer required:*****************************
  libfwupdplugin1 shim slirp4netns
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  bridge-utils dns-root-data dnsmasq-base libidn11 ubuntu-fan
Suggested packages:
  ifupdown aufs-tools cgroupfs-mount | cgroup-lite debootstrap docker-doc
  rinse zfs-fuse | zfsutils
The following NEW packages will be installed:
  bridge-utils dns-root-data dnsmasq-base docker.io libidn11 ubuntu-fan
0 upgraded, 6 newly installed, 0 to remove and 81 not upgraded.
changed: [host_01]

TASK [docker : Install docker-compose] *********************************************************************
changed: [host_01]

PLAY RECAP *************************************************************************************************
host_01                    : ok=6    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

- Inventory details:
```console
.../ansible $ ansible-inventory -i inventory/inno-vm.yml --list
{
    "_meta": {
        "hostvars": {
            "host_01": {
                "ansible_host": "10.90.137.252",
                "ansible_user": "ansible"
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
}
```


## Playbook with app deployment
```console
.../ansible $ ansible-playbook playbooks/dev/main.yaml -K --diff --check
BECOME password:

PLAY [Install Docker] *********************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************************************************************************
ok: [host_01]

TASK [docker : Upgrade pip] ***************************************************************************************************************************************************************************************************************
ok: [host_01]

TASK [docker : Add Docker GPG Key] ********************************************************************************************************************************************************************************************************
ok: [host_01]

TASK [docker : Add Docker Repository] *****************************************************************************************************************************************************************************************************
ok: [host_01]

TASK [docker : apt update] ****************************************************************************************************************************************************************************************************************
changed: [host_01]

TASK [docker : Install Dependencies] ******************************************************************************************************************************************************************************************************
ok: [host_01] => (item=apt-transport-https)
ok: [host_01] => (item=ca-certificates)
ok: [host_01] => (item=curl)
ok: [host_01] => (item=gnupg-agent)
ok: [host_01] => (item=software-properties-common)
ok: [host_01] => (item=containerd)

TASK [docker : Install containerd] ********************************************************************************************************************************************************************************************************
ok: [host_01]

TASK [docker : Install docker.io] *********************************************************************************************************************************************************************************************************
ok: [host_01]

TASK [docker : Install docker-compose] ****************************************************************************************************************************************************************************************************
ok: [host_01]

TASK [web_app : Create compose directory] *************************************************************************************************************************************************************************************************
ok: [host_01]

TASK [web_app : Create docker-compose.yml from template] **********************************************************************************************************************************************************************************
ok: [host_01]

TASK [web_app : Bring up the compose] *****************************************************************************************************************************************************************************************************
changed: [host_01]

TASK [web_app : Bring down the compose] ***************************************************************************************************************************************************************************************************
skipping: [host_01]

TASK [web_app : Remove compose directory] *************************************************************************************************************************************************************************************************
skipping: [host_01]

PLAY RECAP ********************************************************************************************************************************************************************************************************************************
host_01                    : ok=12   changed=2    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```
