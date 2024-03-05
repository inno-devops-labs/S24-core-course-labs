# Ansible

## Initial setup

First, I create cloud server via my cloud provider. I use ssh connection, and setup ssh key.

Then, I create folder structure for ansible, setting up `inventory.yml` with my-server-specific data.

## Already made role

### Download geerlingguy.docker

First, I install already made docker role via `ansible-galaxy install geerlingguy.docker`
Then I setup playbook to use that role

### Use geerlingguy.docker

`ansible-playbook playbooks/dev/main.yml -i inventory/inventory.yml --diff` (with some stars cut):

```shell
... ~60 lines skipped ...

TASK [../../roles/geerlingguy.docker : Install Docker packages.] ********************************
skipping: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Install Docker packages (with downgrade option).] ********
The following additional packages will be installed:
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 1 not upgraded.
changed: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Install docker-compose plugin.] **************************
skipping: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] **
ok: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Ensure /etc/docker/ directory exists.] *******************
skipping: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Configure Docker daemon options.] ************************
skipping: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Ensure Docker is started and enabled at boot.] ***********
ok: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] 

RUNNING HANDLER [../../roles/geerlingguy.docker : restart docker] *******************************
changed: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : include_tasks] *******************************************
skipping: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Get docker group info using getent.] *********************
skipping: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : Check if there are any users to add to the docker group.] 
skipping: [92.255.77.211]

TASK [../../roles/geerlingguy.docker : include_tasks] *******************************************
skipping: [92.255.77.211]

PLAY RECAP **************************************************************************************
92.255.77.211              : ok=12   changed=4    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   
```

`ansible-inventory -i inventory/inventory.yml --list`:

```jsons
{
    "_meta": {
        "hostvars": {
            "92.255.77.211": {
                "ansible_connection": "ssh",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
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
            "92.255.77.211"
        ]
    }
}
```

## Custom docker role

### Usage

I changed the path to role in the playbook to the new, custom, role. Additionally, I reset the cloud VM state to default.

`ansible-playbook playbooks/dev/main.yml -i inventory/inventory.yml --diff` (with some stars cut):

```shell
... ~40 lines skipped ...
  libjs-underscore liblsan0 libmpc3 libnsl-dev libpython3-dev
  libpython3.10-dev libquadmath0 libstdc++-11-dev libtiff5 libtirpc-dev
  libtsan0 libubsan1 libwebp7 libxpm4 linux-libc-dev lto-disabled-list make
  manpages-dev python3-dev python3-pip python3-wheel python3.10-dev
  rpcsvc-proto zlib1g-dev
0 upgraded, 64 newly installed, 0 to remove and 1 not upgraded.
changed: [92.255.77.211]

TASK [../../roles/docker : Ensure old versions of Docker are not installed.] *******************************************************************************************************************************************************
ok: [92.255.77.211]

TASK [../../roles/docker : Ensure dependencies are installed.] *********************************************************************************************************************************************************************
ok: [92.255.77.211]

TASK [../../roles/docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *************************************************************************************************************************************
ok: [92.255.77.211]

TASK [../../roles/docker : Add Docker apt key.] ************************************************************************************************************************************************************************************
changed: [92.255.77.211]

TASK [../../roles/docker : Add Docker repository.] *********************************************************************************************************************************************************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/docker.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [92.255.77.211]

TASK [../../roles/docker : Install Docker] *****************************************************************************************************************************************************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 1 not upgraded.
changed: [92.255.77.211]

TASK [../../roles/docker : Ensure docker users are added to the docker group.] *****************************************************************************************************************************************************
skipping: [92.255.77.211]

TASK [../../roles/docker : Reset ssh connection to apply user changes.] ************************************************************************************************************************************************************

TASK [../../roles/docker : Install Docker-Compose] *********************************************************************************************************************************************************************************
changed: [92.255.77.211]

PLAY RECAP *************************************************************************************************************************************************************************************************************************
92.255.77.211              : ok=9    changed=5    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```

`ansible-inventory -i inventory/inventory.yml --list`:

```json
{
    "_meta": {
        "hostvars": {
            "92.255.77.211": {
                "ansible_connection": "ssh",
                "ansible_ssh_private_key_file": "~/.ssh/id_ed25519",
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
            "92.255.77.211"
        ]
    }
}
```
