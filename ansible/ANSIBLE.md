#  Ansible-related work
## Task 1
First, I installed [existing role](https://galaxy.ansible.com/ui/standalone/roles/geerlingguy/docker/) by executing the following command:
```bash
ansible-galaxy role install geerlingguy.docker
```
Next, I specified the newly installed role in the playbook located at `./ansible/playbooks/dev/main.yaml`:
```yaml
- name: Docker playbook
  hosts: localhost
  become: True
  roles:
   - geerlingguy.docker
```

Finally, I added task to pull my Docker image:
```yaml
  tasks:
    - name: Pull Docker image
      docker_image:
        name: glebuben/dev-ops-labs:latest
        source: pull
```

Subsequently, task for running the Docker container with specified ports to open:
```yaml
    - name: Run Docker container
      docker_container:
        name: my_container
        image: glebuben/dev-ops-labs:latest
        state: started
        ports:
          - "8000:5000"
```
## Task 2

To utilize a custom role, I needed to specify my ansible.cfg file:
```bash
export ANSIBLE_CONFIG=./ansible/ansible.cfg
```

In the playbook, I employed identical tasks as in Task 1. The only alteration was made in the roles section:
```yaml
  - name: Docker playbook
  hosts: localhost
  become: True
  roles:
    - docker
# Task 1
#    - geerlingguy.docker
  ...
```

To leverage additional details, please refer to `./ansible/roles/docker/README.md` for comprehensive instructions.
# Deployment command output (lab 5)
command:
```bash
ansible-playbook ./ansible/playbooks/dev/main.yaml
```
output:
```bash
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Docker playbook] ****************************************************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] *********************************************************************************************************************************************************
included: /mnt/c/Git/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Add Docker APT repository] *********************************************************************************************************************************************
ok: [localhost]

TASK [docker : Add Docker's official GPG key] *****************************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker dependencies] *******************************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker] ********************************************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] *********************************************************************************************************************************************************
included: /mnt/c/Git/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Install Docker Compose] ************************************************************************************************************************************************
ok: [localhost]

TASK [Pull Docker image] **************************************************************************************************************************************************************
ok: [localhost]

TASK [Run Docker container] ***********************************************************************************************************************************************************
ok: [localhost]

PLAY RECAP ****************************************************************************************************************************************************************************
localhost                  : ok=10   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```
# Deployment command output (lab 6)
command:
```bash
ansible-playbook ./ansible/playbooks/dev/main.yaml
```
output:
```bash
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Docker playbook] *****************************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] **********************************************************************************************************************************************************
included: /mnt/c/Git/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install pip] ************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : Add Docker APT repository] **********************************************************************************************************************************************
ok: [localhost]

TASK [docker : Add Docker's official GPG key] ******************************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker dependencies] ********************************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker] *********************************************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] **********************************************************************************************************************************************************
included: /mnt/c/Git/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for localhost

TASK [docker : Install Docker Compose] *************************************************************************************************************************************************
ok: [localhost]

TASK [web_app : Pull Docker image] *****************************************************************************************************************************************************
ok: [localhost]

TASK [web_app : Run Docker container] **************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP *****************************************************************************************************************************************************************************
localhost                  : ok=11   changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

glebass@LAPTOP-4V6LKT02:/mnt/c/Git/S24-core-course-labs$ ansible-playbook ./ansible/playbooks/dev/main.yaml 
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [Docker playbook] *****************************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : include_tasks] **********************************************************************************************************************************************************
included: /mnt/c/Git/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for localhost

TASK [docker : Install pip] ************************************************************************************************************************************************************
ok: [localhost]

TASK [docker : Add Docker APT repository] **********************************************************************************************************************************************
ok: [localhost]

TASK [docker : Add Docker's official GPG key] ******************************************************************************************************************************************
ok: [localhost]

TASK [docker : Install Docker dependencies] ********************************************************************************************************************************************
TASK [web_app : Pull Docker image] *****************************************************************************************************************************************************
ok: [localhost]

TASK [web_app : Run Docker container] **************************************************************************************************************************************************
ok: [localhost]

PLAY RECAP *****************************************************************************************************************************************************************************
localhost                  : ok=11   changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

# `ansible-inventory` command output
command:
```bash
ansible-inventory -i default_aws_ec2.yml --list
```
output:
```bash
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
This output reflects empty entities, as no virtual machines were utilized; the deployment was conducted locally.