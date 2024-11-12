## Installation
1. Clone the repo.
2. Install Ansible by following the [installation guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html).
3. Update your `inventory/vm.yml` file with your vm machine ip, name, and password(install sshshmthing).
4. Run the Ansible playbook:


creating web app through ancible in docker on vm, then wiping it:
```bash
(venv) smasiner@smasIners-MacBook-Pro ansible % ansible-playbook -i inventory/vm.yml playbooks/dev/main.yaml                                          

PLAY [Install docker manually] ****************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
[WARNING]: Platform linux on host vm_name is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [vm_name]

TASK [../../roles/docker : include_tasks] *****************************************************************************************************************************
included: /Users/smasiner/Documents/GitHub/Iwanttodie/Untitled/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm_name

TASK [../../roles/docker : Install Docker dependencies] ***************************************************************************************************************
ok: [vm_name]

TASK [../../roles/docker : Add Docker’s official GPG key] *************************************************************************************************************
ok: [vm_name]

TASK [../../roles/docker : Set up Docker stable repository] ***********************************************************************************************************
ok: [vm_name]

TASK [../../roles/docker : Install Docker] ****************************************************************************************************************************
ok: [vm_name]

TASK [../../roles/docker : include_tasks] *****************************************************************************************************************************
included: /Users/smasiner/Documents/GitHub/Iwanttodie/Untitled/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm_name

TASK [../../roles/docker : Download Docker Compose] *******************************************************************************************************************
ok: [vm_name]

TASK [docker : include_tasks] *****************************************************************************************************************************************
included: /Users/smasiner/Documents/GitHub/Iwanttodie/Untitled/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for vm_name

TASK [docker : Install Docker dependencies] ***************************************************************************************************************************
ok: [vm_name]

TASK [docker : Add Docker’s official GPG key] *************************************************************************************************************************
ok: [vm_name]

TASK [docker : Set up Docker stable repository] ***********************************************************************************************************************
ok: [vm_name]

TASK [docker : Install Docker] ****************************************************************************************************************************************
ok: [vm_name]

TASK [docker : include_tasks] *****************************************************************************************************************************************
included: /Users/smasiner/Documents/GitHub/Iwanttodie/Untitled/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for vm_name

TASK [docker : Download Docker Compose] *******************************************************************************************************************************
ok: [vm_name]

TASK [../../roles/web_app : Create compose directory] *****************************************************************************************************************
ok: [vm_name]

TASK [../../roles/web_app : Create docker-compose.yml from template] **************************************************************************************************
ok: [vm_name]

TASK [../../roles/web_app : Bring up the compose] *********************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential
confusion
changed: [vm_name]

TASK [../../roles/web_app : Bring down the compose] *******************************************************************************************************************
skipping: [vm_name]

TASK [../../roles/web_app : Remove compose directory] *****************************************************************************************************************
skipping: [vm_name]

PLAY RECAP ************************************************************************************************************************************************************
vm_name                    : ok=18   changed=1    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   

(venv) smasiner@smasIners-MacBook-Pro ansible % curl http://5.42.101.243:8080                                                                         
^C
(venv) smasiner@smasIners-MacBook-Pro ansible % curl http://5.42.101.243:8080
<h1>Moscow Time: 2024-11-12 20:17:47</h1>%                                                                                                                             (venv) smasiner@smasIners-MacBook-Pro ansible % ansible-playbook -i inventory/vm.yml playbooks/dev/main.yaml --tags "wipe" -e "web_app_full_wipe=true"

PLAY [Install docker manually] ****************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************************
[WARNING]: Platform linux on host vm_name is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter
could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ok: [vm_name]

TASK [../../roles/web_app : Bring down the compose] *******************************************************************************************************************
[WARNING]: Docker compose: unknown None: /opt/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential
confusion
changed: [vm_name]

TASK [../../roles/web_app : Remove compose directory] *****************************************************************************************************************
changed: [vm_name]

PLAY RECAP ************************************************************************************************************************************************************
vm_name                    : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

(venv) smasiner@smasIners-MacBook-Pro ansible % curl http://5.42.101.243:8080                                                                         
curl: (56) Recv failure: Connection reset by peer
(venv) smasiner@smasIners-MacBook-Pro ansible % 
```

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
