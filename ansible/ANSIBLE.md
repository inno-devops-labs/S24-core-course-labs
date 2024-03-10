# Lab 5 - Ansible Setup

## Best practicies
- I configured and init all folders using ```ansible init``` to create automatically folders and project architecture.
- Documenting and use naming in ```.yml``` files
- Project structure according to Ansible standarts


## Steps of implementation

1. Initialize /roles/docker and /roles/web_server directories using ```ansible init``` to create a strcuture of the project.
2. Set up my ssh in the AWS terminal.
3. Add inventor ec2 file with server public IP.
3. Add necessary code and files to install docker and docker compose.
4. Add main.yaml in playbooks with roles.
4. Add Ansible.cfg.
5. Test outputs (The result will be in the next paragraph)


## Outputs

```
ansible-playbook playbooks/dev/main.yaml --diff 
```
```
BECOME password: 

PLAY [Setup docker] ******************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************************
ok: [web_server]

TASK [../../roles/docker : Update apt] *************************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Python3 and pip3 installation] ******************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Docker installation] ****************************************************************************************************************************
changed: [web_server]

TASK [../../roles/docker : Docker-compose installation] ********************************************************************************************************************
changed: [web_server]

PLAY RECAP *****************************************************************************************************************************************************************
web_server                 : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```

```
ansible-inventory -i inventory/default_aws_ec2.yml --list 
```

```
{
    "_meta": {
        "hostvars": {
            "web_server": {
                "ansible_host": "16.171.41.136",
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

Updated output from lab 6

Succesfully deployed web_app to server via ansible

```
ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yaml -K
```

```
BECOME password:

PLAY [all] *****************************************************************************************

TASK [Gathering Facts] *****************************************************************************
ok: [web_server]

TASK [geerlingguy.docker : Load OS-specific vars.] *************************************************
ok: [web_server]

TASK [geerlingguy.docker : include_tasks] **********************************************************
skipping: [web_server]

TASK [geerlingguy.docker : include_tasks] **********************************************************
included: /Users/alexandrachupkova/.ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for web_server

TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***********************
ok: [web_server]

TASK [geerlingguy.docker : Ensure dependencies are installed.] *************************************
ok: [web_server]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ***
skipping: [web_server]

TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *****
ok: [web_server]

TASK [geerlingguy.docker : Add Docker apt key.] ****************************************************
ok: [web_server]

TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *****************
skipping: [web_server]

TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ********
skipping: [web_server]

TASK [geerlingguy.docker : Add Docker repository.] *************************************************
ok: [web_server]

TASK [geerlingguy.docker : Install Docker packages.] ***********************************************
skipping: [web_server]

TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***********************
ok: [web_server]

TASK [geerlingguy.docker : Install docker-compose plugin.] *****************************************
skipping: [web_server]

TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *****************
ok: [web_server]

TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **********************************
skipping: [web_server]

TASK [geerlingguy.docker : Configure Docker daemon options.] ***************************************
skipping: [web_server]

TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] **************************
ok: [web_server]

TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **********

TASK [geerlingguy.docker : include_tasks] **********************************************************
skipping: [web_server]

TASK [geerlingguy.docker : Get docker group info using getent.] ************************************
skipping: [web_server]

TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] ***************
skipping: [web_server]

TASK [geerlingguy.docker : include_tasks] **********************************************************
skipping: [web_server]

TASK [docker : Apt] ********************************************************************************
changed: [web_server]

TASK [docker : Install python3 and pip] ************************************************************
ok: [web_server]

TASK [docker : Docker installation] ****************************************************************
ok: [web_server]

TASK [docker : Docker-compose installation] ********************************************************
ok: [web_server]

TASK [../../../roles/web_app : Ensure that directory exist] ****************************************
ok: [web_server]

TASK [../../../roles/web_app : Upload docker-compose.yaml] *****************************************
ok: [web_server]

TASK [../../../roles/web_app : Launch app] *********************************************************
ok: [web_server]

TASK [../../../roles/web_app : Clean up docker compose project] ************************************
skipping: [web_server]

TASK [../../../roles/web_app : Clean up project files] *********************************************
skipping: [web_server]

PLAY RECAP *****************************************************************************************
web_server                 : ok=18   changed=1    unreachable=0    failed=0    skipped=14   rescued=0    ignored=0
```

