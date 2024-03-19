# Ansible Documentation (Lab 5)

## Project Structure

- `ansible/roles`: Directory containing Ansible roles.
- `ansible/playbooks`: Directory containing Ansible playbooks.
- `ansible/inventory`: Directory containing inventory files.

## Deploy Docker (Locally)

1. Ensure that Ansible is installed on your system.
2. Clone the project repository.
3. Navigate to the `ansible` directory.
4. Edit the `playbooks/dev/deploy_docker.yml` playbook if necessary.
5. Run the playbook using the following command:

```bash
ansible-playbook -i inventory/localhost.yaml  playbooks/dev/deploy_docker.yaml
```

### Output

```bash
root@ubuntu-ge:~/gh/S24-core-course-labs/ansible# ansible-playbook -i inventory/localhost.yaml  playbooks/dev/deploy_docker.yaml

PLAY [Deploy Docker] ******************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : Install pip] ***********************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : Install Docker dependencies] *******************************************************************************************************************
ok: [127.0.0.1] => (item=apt-transport-https)
ok: [127.0.0.1] => (item=ca-certificates)
ok: [127.0.0.1] => (item=curl)
ok: [127.0.0.1] => (item=gnupg-agent)
ok: [127.0.0.1] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] ****************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : Add Docker repository] *************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : Install Docker] ********************************************************************************************************************************
ok: [127.0.0.1]

TASK [docker : Install Docker Compose] ************************************************************************************************************************
ok: [127.0.0.1]

PLAY RECAP ****************************************************************************************************************************************************
127.0.0.1                  : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Inventory details

```bash
root@ubuntu-ge:~/gh/S24-core-course-labs/ansible# ansible-inventory -i inventory/localhost.yaml --list
{
    "_meta": {
        "hostvars": {
            "localhost": {
                "ansible_connection": "local"
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
            "localhost"
        ]
    }
}
```


# Ansible (Lab 6)

```
PLAY [Deploy Docker] ******************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************
ok: [localhost]

TASK [docker : Install pip] ***********************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker dependencies] *******************************************************************************************************************
ok: [localhost] => (item=apt-transport-https)
ok: [localhost] => (item=ca-certificates)
ok: [localhost] => (item=curl)
ok: [localhost] => (item=gnupg-agent)
ok: [localhost] => (item=software-properties-common)

TASK [docker : Add Docker GPG key] ****************************************************************************************************************************
ok: [localhost]

TASK [docker : Add Docker repository] *************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker] ********************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker Compose] ************************************************************************************************************************
ok: [localhost]

TASK [web_app : Pull the latest Docker image] *****************************************************************************************************************
[DEPRECATION WARNING]: The value of the "source" option was determined to be "pull". Please set the "source" option explicitly. Autodetection will be removed
in community.general 2.0.0. This feature will be removed from community.general in version 2.0.0. Deprecation warnings can be disabled by setting
deprecation_warnings=False in ansible.cfg.
ok: [localhost]

TASK [web_app : Run Docker container] *************************************************************************************************************************
[DEPRECATION WARNING]: The container_default_behavior option will change its default value from "compatibility" to "no_defaults" in community.general 3.0.0.
To remove this warning, please specify an explicit value for it now. This feature will be removed from community.general in version 3.0.0. Deprecation
warnings can be disabled by setting deprecation_warnings=False in ansible.cfg.
changed: [localhost]

PLAY RECAP ****************************************************************************************************************************************************
localhost                  : ok=9    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

root@ubuntu-ge:~/gh/S24-core-course-labs/ansible# docker ps
CONTAINER ID   IMAGE                       COMMAND                  CREATED         STATUS         PORTS                    NAMES
dbf583c665c5   tsepanx/app_python:latest   "uvicorn main:app --…"   2 minutes ago   Up 9 seconds   0.0.0.0:8000->8000/tcp   app_python-1
```
