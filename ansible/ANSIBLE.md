# Ansible

```bash
$ ansible-playbook playbooks/dev/main.yml --diff --ask-become-pass
BECOME password: 

PLAY [Install docker] *********************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************
[WARNING]: Platform linux on host localhost is using the discovered Python interpreter at /usr/local/bin/python3.11, but future installation of
another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [localhost]

TASK [docker : include_tasks] *************************************************************************************************************************
included: /home/thecarrot/S24-core-course-labs/ansible/roles/docker/tasks/setup-Debian.yml for localhost

TASK [docker : Ensure old versions of Docker are not installed.] **************************************************************************************
ok: [localhost]

TASK [docker : Ensure dependencies are installed.] ****************************************************************************************************
ok: [localhost]

TASK [docker : Ensure directory exists for /etc/apt/keyrings] *****************************************************************************************
ok: [localhost]

TASK [docker : Add Docker apt key.] *******************************************************************************************************************
ok: [localhost]

TASK [docker : Ensure curl is present (on older systems without SNI).] ********************************************************************************
skipping: [localhost]

TASK [docker : Add Docker apt key (alternative for older systems without SNI).] ***********************************************************************
skipping: [localhost]

TASK [docker : Add Docker repository.] ****************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] *************************************************************************************************************************
included: /home/thecarrot/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Check current docker-compose version.] *************************************************************************************************
ok: [localhost]

TASK [docker : set_fact] ******************************************************************************************************************************
ok: [localhost]

TASK [docker : Delete existing docker-compose version if it's different.] *****************************************************************************
skipping: [localhost]

TASK [docker : Install Docker Compose (if configured).] ***********************************************************************************************
skipping: [localhost]

TASK [docker : Ensure handlers are notified now to avoid firewall conflicts.] *************************************************************************

TASK [docker : Get docker group info using getent.] ***************************************************************************************************
skipping: [localhost]

TASK [docker : Check if there are any users to add to the docker group.] ******************************************************************************
skipping: [localhost]

TASK [docker : include_tasks] *************************************************************************************************************************
skipping: [localhost]

PLAY RECAP ********************************************************************************************************************************************
localhost                  : ok=10   changed=0    unreachable=0    failed=0    skipped=7    rescued=0    ignored=0 
```

```json
$ ansible-inventory -i inventory/hosts --list
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "localhost"
        ]
    }
}
```
