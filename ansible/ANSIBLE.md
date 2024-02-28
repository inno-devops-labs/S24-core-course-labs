# Deployment

## Output

```shell
$ ansible-playbook playbooks/dev/main.yml -i inventory

PLAY [Deploy Docker] ***************************************************************************************************
TASK [Gathering Facts] *************************************************************************************************
ok: [178.154.207.34]

TASK [../../roles/docker : include_tasks] ******************************************************************************
included: /mnt/c/Users/under/Documents/GitHub/S24-core-course-labs/ansible/roles/docker/tasks/setup_repo_debian.yml for 178.154.207.34

TASK [../../roles/docker : Install Dependencies] ***********************************************************************
ok: [178.154.207.34]

TASK [../../roles/docker : keyrings] ***********************************************************************************
changed: [178.154.207.34]

TASK [../../roles/docker : Add Docker apt key.] ************************************************************************
ok: [178.154.207.34]

TASK [../../roles/docker : Add Docker repository.] *********************************************************************
ok: [178.154.207.34]

TASK [../../roles/docker : Disable Unattended Upgrades] ****************************************************************
ok: [178.154.207.34]

TASK [../../roles/docker : Install pip] ********************************************************************************
ok: [178.154.207.34]

TASK [../../roles/docker : Install Docker] *****************************************************************************
ok: [178.154.207.34]

TASK [../../roles/docker : Install Docker Compose with pip] ************************************************************
ok: [178.154.207.34]

TASK [Run container] ***************************************************************************************************
changed: [178.154.207.34]

PLAY RECAP *************************************************************************************************************
178.154.207.34             : ok=11   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Deployment

```shell
$ ansible-playbook playbooks/dev/app_python/main.yml -i inventory/vm.yacloud_compute.yml

PLAY [Deploy Docker] ***************************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [test-vm]

TASK [docker : include_tasks] ******************************************************************************************
included: /mnt/c/Users/under/Documents/GitHub/S24-core-course-labs/ansible/roles/docker/tasks/setup_repo_debian.yml for test-vm

TASK [docker : Install Dependencies] ***********************************************************************************
ok: [test-vm]

TASK [docker : Setup keyrings folder] **********************************************************************************
changed: [test-vm]

TASK [docker : Add Docker apt key] *************************************************************************************
ok: [test-vm]

TASK [docker : Add Docker repository] **********************************************************************************
ok: [test-vm]

TASK [docker : Disable Unattended Upgrades] ****************************************************************************
ok: [test-vm]

TASK [docker : Install pip] ********************************************************************************************
ok: [test-vm]

TASK [docker : Install Docker] *****************************************************************************************
ok: [test-vm]

TASK [docker : Install Docker Compose with pip] ************************************************************************
ok: [test-vm]

TASK [../../../roles/web_app : Get image] ******************************************************************************
ok: [test-vm]

TASK [../../../roles/web_app : Run container] **************************************************************************
changed: [test-vm]

PLAY RECAP *************************************************************************************************************
test-vm                    : ok=12   changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory

```shell
$ ansible-inventory -i inventory/default_aws_ec2.yml --list
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped",
            "vms"
        ]
    },
    "vms": {
        "hosts": [
            "178.154.207.34"
        ]
    }
}
```

### With dynamic inventory using `yacloud_compute`

```shell
$ ansible-inventory -i inventory/vm.yacloud_compute.yml --list
{
    "_meta": {
        "hostvars": {
            "test-vm": {
                "ansible_host": "158.160.102.55"
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
            "test-vm"
        ]
    }
}
```
