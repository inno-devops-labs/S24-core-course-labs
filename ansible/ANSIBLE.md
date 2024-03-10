# Ansible lab

- I installed Ansible
- I initiated directory with `ansible-galaxy init ansible/roles/docker`
- I installed deps. `ansible-galaxy install geerlingguy.docker`

## Working stages

### Machine configuration

I confidured ssh on both my machine and remote Amazon AWS.

### Working with ansible

- I configured ansible configuration files.

Then I ran: 

```
(Myenv) @blinikar ➜ /workspaces/S24-core-course-labs/ansible (lab4) $ ansible-playbook -i inverntory/default_aws_ec2.yml playbooks/dev/main.yaml -K 
[WARNING]: Ansible is being run in a world writable directory (/workspaces/S24-core-course-labs/ansible), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
BECOME password: 

PLAY [web_server] ***********************************************************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Update apt] **************************************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Python3 and pip3 installation] *******************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Docker installation] *****************************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Docker-compose installation] *********************************************************************************************************************************
changed: [web_server]

PLAY RECAP ******************************************************************************************************************************************************************************
web_server                 : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

Result of list command:

```
(Myenv) @blinikar ➜ /workspaces/S24-core-course-labs/ansible (lab4) $ ansible-inventory -i inverntory/default_aws_ec2.yml --list 
[WARNING]: Ansible is being run in a world writable directory (/workspaces/S24-core-course-labs/ansible), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "18.237.114.36",
                "ansible_user": "ansible-user"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "virtual_machines"
        ]
    },
    "virtual_machines": {
        "hosts": [
            "web_server"
        ]
    }
}
```

# Ansible lab PART II (LAB VI)

The result of command

```
@blinikar ➜ /workspaces/S24-core-course-labs/ansible (lab5) $ ansible-playbook ./playbooks/dev/main.yaml -i ./inverntory/default_aws_ec2.yml -K
[WARNING]: Ansible is being run in a world writable directory (/workspaces/S24-core-course-labs/ansible), ignoring it as an ansible.cfg source. For more information see
https://docs.ansible.com/ansible/devel/reference_appendices/config.html#cfg-in-world-writable-dir
BECOME password: 

PLAY [web_server] ************************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Update apt] ***************************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Python3 and pip3 installation] ********************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Docker installation] ******************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Docker-compose installation] **********************************************************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : Load OS-specific vars.] ***************************************************************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************************************
included: /home/codespace/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for web_server

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] *************************************************************************************************
changed: [web_server]

TASK [geerlingguy.docker : Ensure dependencies are installed.] ***************************************************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] **********************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *******************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : Add Docker apt key.] ******************************************************************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *******************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] **********************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Add Docker repository.] ***************************************************************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : Install Docker packages.] *************************************************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] *************************************************************************************************
changed: [web_server]

TASK [geerlingguy.docker : Install docker-compose plugin.] *******************************************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *******************************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] ************************************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Configure Docker daemon options.] *****************************************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ****************************************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] ************************************************************************************

RUNNING HANDLER [geerlingguy.docker : restart docker] ************************************************************************************************************************
changed: [web_server]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Get docker group info using getent.] **************************************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *****************************************************************************************
skipping: [web_server]

TASK [geerlingguy.docker : include_tasks] ************************************************************************************************************************************
skipping: [web_server]

TASK [../../../roles/web_app : Ensure that directory exist] ******************************************************************************************************************
changed: [web_server]

TASK [../../../roles/web_app : Upload docker-compose.yaml] *******************************************************************************************************************
changed: [web_server]

TASK [../../../roles/web_app : Launch app] ***********************************************************************************************************************************
changed: [web_server]

TASK [../../../roles/web_app : Clean up docker compose project] **************************************************************************************************************
skipping: [web_server]

TASK [../../../roles/web_app : Clean up project files] ***********************************************************************************************************************
skipping: [web_server]

PLAY RECAP *******************************************************************************************************************************************************************
web_server                 : ok=19   changed=7    unreachable=0    failed=0    skipped=14   rescued=0    ignored=0   
```
