
## CLI Outputs

### Docker Deployment

1. `ansible-playbook playbooks/dev/main.yml --diff`

    ```text

    PLAY [Install Docker using existing role] **************************************

    TASK [Gathering Facts] *********************************************************
    ok: [host_01]

    TASK [docker : include_tasks] **************************************************
    included: /home/REDACTED/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for host_01

    TASK [docker : Install required packages] **************************************
    ok: [host_01]

    TASK [docker : Add Docker’s official GPG key] **********************************
    changed: [host_01]

    TASK [docker : Set up the stable repository] ***********************************
    changed: [host_01]

    TASK [docker : Install Docker Engine] ******************************************
    changed: [host_01]

    TASK [docker : Add user to Docker group] ***************************************
    changed: [host_01]

    TASK [docker : include_tasks] **************************************************
    included: /home/REDACTED/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for host_01

    TASK [docker : Install pip for docker compose] *********************************
    changed: [host_01]

    TASK [docker : Install Docker Compose using pip] *******************************
    changed: [host_01]

    RUNNING HANDLER [docker : Restart Docker] **************************************
    changed: [host_01]

    PLAY RECAP *********************************************************************
    host_01                    : ok=11   changed=7    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
    ```

2. `ansible-inventory -i inventory/default_yandex_vm.yml --list`

    ```json
    {
        "_meta": {
            "hostvars": {
                "host_01": {
                    "ansible_host": "178.154.220.110",
                    "ansible_user": "ubuntu"
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
