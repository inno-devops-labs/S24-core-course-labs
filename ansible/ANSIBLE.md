# Ansible Documentation

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
