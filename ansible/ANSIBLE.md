## Installation
1. Clone the repo.
2. Install Ansible by following the [installation guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html).
3. Update your `inventory/vm.yml` file with your vm machine ip, name, and password(install sshshmthing).
4. Run the Ansible playbook:

```bash
   ansible-playbook -i ansible/inventory/vm.yml ansible/playbooks/dev/main.yaml
```

deployment output here

```bash
(venv) smasiner@smasIners-MacBook-Pro ansible % ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml

PLAY [Install docker manually] ****************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
[WARNING]: Platform linux on host vm_name is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [vm_name]

TASK [../../roles/docker : include_tasks] *****************************************************************************************************************************
included: /Users/smasiner/Documents/GitHub/Iwanttodie/Untitled/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm_name

TASK [../../roles/docker : Install Docker dependencies] ***************************************************************************************************************
changed: [vm_name]

TASK [../../roles/docker : Add Docker’s official GPG key] *************************************************************************************************************
changed: [vm_name]

TASK [../../roles/docker : Set up Docker stable repository] ***********************************************************************************************************
changed: [vm_name]

TASK [../../roles/docker : Install Docker] ****************************************************************************************************************************
changed: [vm_name]

TASK [../../roles/docker : include_tasks] *****************************************************************************************************************************
included: /Users/smasiner/Documents/GitHub/Iwanttodie/Untitled/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm_name

TASK [../../roles/docker : Download Docker Compose] *******************************************************************************************************************
changed: [vm_name]

RUNNING HANDLER [../../roles/docker : Start Docker] *******************************************************************************************************************
ok: [vm_name]

PLAY RECAP ************************************************************************************************************************************************************
vm_name                    : ok=9    changed=5    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

ansible-inventory -i inventory --list

```bash
(venv) smasiner@smasIners-MacBook-Pro ansible % ansible-inventory -i inventory --list                                                                 
{
    "_meta": {
        "hostvars": {
            "vm_name": {
                "ansible_host": "5.42.101.243",
                "ansible_password": "censored",
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
            "vm_name"
        ]
    }
}

```
