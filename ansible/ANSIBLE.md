# Ansible
## Best Practices for Ansible:
- Implementation Version Control: storing playbooks and inventory files in a version control system.
- Maintenance of an Organized Directory Layout: the playbook directories are structured effectively.
- Utilization Dynamic Inventory for Cloud Environments: leveraging dynamic inventory scripts when working with cloud platforms.

## Description of the Work Done
Ansible connects to virtual machines created in VK Cloud for its operations. It uses a specific key for connection, the details of which are provided in the Ansible configuration file.

The inventory lists the VK Cloud hosts that Ansible will connect to.

The playbook is designed to initiate the deployment of Docker.

Within the roles, there is a dedicated Docker role responsible for installing and setting up Docker on the virtual machines.

## Command Outputs
### Deployment Output with `ansible-playbook playbooks/dev/main.yaml`:

```shell
PLAY [Deploy Docker] ************************************************************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************************************************************
ok: [vk01]

TASK [docker : Install pip] *****************************************************************************************************************************************************************
included: /home/ubuntu/S24-core-course-labs/ansible/roles/docker/tasks/install_pip.yml for vk01

TASK [docker : Update apt] ******************************************************************************************************************************************************************
changed: [vk01]

TASK [docker : Install python] **************************************************************************************************************************************************************
ok: [vk01]

TASK [docker : Install pip] *****************************************************************************************************************************************************************
ok: [vk01]

TASK [docker : Install docker] **************************************************************************************************************************************************************
included: /home/ubuntu/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vk01

TASK [docker : Install docker] **************************************************************************************************************************************************************
ok: [vk01]

TASK [docker : Install docker-compose] ******************************************************************************************************************************************************
included: /home/ubuntu/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vk01

TASK [docker : Install docker-compose] ******************************************************************************************************************************************************
changed: [vk01]

PLAY RECAP **********************************************************************************************************************************************************************************
vk01                       : ok=9    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

### Inventory Details with ` ansible-inventory -i <name_of_your_inventory_file>.yaml --list`:
```shell
{
    "_meta": {
        "hostvars": {
            "vk01": {
                "ansible_host": "212.111.84.102"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "vk_hosts"
        ]
    },
    "vk_hosts": {
        "hosts": [
            "vk01"
        ]
    }
}
```