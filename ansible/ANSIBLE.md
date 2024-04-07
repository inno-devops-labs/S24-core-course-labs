# Ansible Documentation

## Prerequisites
Ansible should be installed.

## Creating a custom docker role
For creating a custom docker role, I used `ansible-galaxy init ansible/roles/docker`
Then I wrote tasks for the role: installing pip, docker, docker-compose


## Running a Playbook
Execute the playbook:

```bash
ansible-playbook ansible/playbooks/dev/main.yaml
```

## Output of --diff

```[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [localhost] ********************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************
ok: [localhost]

TASK [../../roles/docker : Install pip] *********************************************************************************************
ok: [localhost]

TASK [../../roles/docker : include_tasks] *******************************************************************************************
included: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [../../roles/docker : Install Docker packages] *********************************************************************************
ok: [localhost] => (item=docker-ce)
ok: [localhost] => (item=docker-ce-cli)
ok: [localhost] => (item=docker-ce-rootless-extras)

TASK [../../roles/docker : include_tasks] *******************************************************************************************
included: /mnt/c/Users/almet/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [../../roles/docker : Install Docker Compose using pip] ************************************************************************
ok: [localhost]

TASK [Pull default Docker image] ****************************************************************************************************
changed: [localhost]

TASK [Run docker container] *********************************************************************************************************
changed: [localhost]

PLAY RECAP **************************************************************************************************************************
localhost                  : ok=8    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Output of ansible-inventory
I used localhost

```
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    }
}
```