# Ansible

## Process description

1. Process starts with /ansible/playbooks/dev/main.yml where we pull and deploy image
of our project. It uses role docker
2. Role docker is declared in ansible/roles/docker where all the docker and docker compose
logic described.
3. Docker is divided into several parts.
    * First with declaration of variables
    * Second with handlers
    * And last one with main tasks
4. Handlers are simple. They just validate that current user has Docker compose group access and restart docker.
5. Tasks are divided in main tasks and two its subtasks:
   * First subtask is installing pip and docker compose.
   * Second subtasks describes all logic to install docker through apt.

## Deployment output

### Input
```bash
sudo ansible-playbook --diff playbooks/dev/main.yml | tail -n 50
```
### Output
```text
[WARNING]: provided hosts list is empty, only localhost is available. Note that
the implicit localhost does not match 'all'

PLAY [Pull and deploy] *********************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [docker : APT Update] *****************************************************
changed: [localhost]

TASK [docker : Add Docker apt key.] ********************************************
ok: [localhost]

TASK [docker : Add Docker repository.] *****************************************
ok: [localhost]

TASK [docker : Install Docker] *************************************************
ok: [localhost]

TASK [docker : Install pip] ****************************************************
ok: [localhost]

TASK [docker : Install Docker Compose via pip] *********************************
ok: [localhost]

TASK [Pull Docker Image] *******************************************************
ok: [localhost]

TASK [Run Docker Container] ****************************************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
```

## Inventory details

```text
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

Inventory is empty because the deployment is local and described in playbooks/dev/main.yml.