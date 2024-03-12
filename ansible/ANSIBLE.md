# Documentation

### inventory/default_yc_ec2.yml file

Using the IP address ```51.201.12.197``` and the user ```ubuntu```, Ansible inventory file defines a single host called ```host_01``` as the target for Ansible operations.

### playbooks/dev/main.yml file

A series of tasks that should be applied to all hosts is described in this Ansible playbook. One role in particular, ```docker```, has to be run with elevated privileges (become: true). 

Also, it defines a variable called ```ansible_ssh_private_key_file``` that points to the SSH private key file's location (~/.ssh/id_ed25519) that should be used for SSH connections.

### roles/docker file

#### 1.default/main.yml file

This Ansible file, which was extracted from the sample given, specifies how to install and use Docker and Docker Compose.

#### 2. handlers/main.yml file

This file defines "Restart" handler that uses the service module to restart docker.

#### 3. tasks/install_compose.yml file

This Ansible file, which was extracted from the sample given, specifies how to install and use Docker and Docker Compose.

#### 4. tasks/install_docker.yml file

Using the ```apt``` module, this Ansible task installs Docker on a Debian-based machine. It verifies that the destination system has the docker.io package installed.

#### 5. tasks/main.yml file

Tasks to install ```Python 3``` and ```pip3```, update the apt cache, import and run tasks from separate files to install Docker and Docker Compose are defined in this Ansible playbook. 
```docker``` is a tag used for organising tasks linked to Docker, which can be used to execute them selectively.

### roles/web_app files

#### 1. default/main.yml file

The Docker image and container parameters for a Python application are defined by the variables.

#### 2. handlers/main.yml file

Restarting the web application's Docker container is done with this handler.

#### 3. mata/main.yml file

The `web_app` Ansible role's requirements are specified in this file.

#### 4. tasks/O-wipe.yml file

The web application's wipe logic, which entails pausing and deleting the Docker container, is defined by this Ansible task block.

#### 5. tasks/main.yml file

The tasks associated with maintaining the web application's Docker image and container are included in this Ansible task block.

#### 6. templates/docker-compose.yml.j2 file

This file is a Docker Compose template that specifies the web application container's configuration.

### ansible.ctg file

The default parameters for Ansible are specified in this Ansible configuration file ```ansible.cfg```. By configuring Ansible to utilise particular directories and settings by default, these options assist minimise the need to define them in each playbook. The main configurations are broken down as follows:

- ```inventory```: Indicates the directory containing the inventory file.
- ```roles_path```: Indicates the path in which Ansible roles are stored.
- ```private key file```: Indicates the location of the SSH private key, which is located at `~/.ssh/id_ed25519`.
- ```control_path```: Indicates the path template for the SSH connection's control path.


# Outputs for docker role

- `ansible-playbook playbooks/dev/main.yml --diff`

    ```text
   PLAY [Install Docker] **********************************************************************************************************************************************************
   
   TASK [Gathering Facts] *********************************************************************************************************************************************************
   Enter passphrase for key '/Users/nikitagrigorenko/.ssh/id_ed25519': 
   ok: [host_01]
   
   TASK [geerlingguy.docker : Load OS-specific vars.] *****************************************************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
   included: /Users/nikitagrigorenko/Documents/Homeworks/DevOps/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for host_01
   
   TASK [geerlingguy.docker : Ensure old versions of Docker are not installed.] ***************************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : Ensure dependencies are installed.] *****************************************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu < 20.04 and any other systems).] ************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Ensure additional dependencies are installed (on Ubuntu >= 20.04).] *********************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : Add Docker apt key.] ********************************************************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : Ensure curl is present (on older systems without SNI).] *********************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Add Docker apt key (alternative for older systems without SNI).] ************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Add Docker repository.] *****************************************************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : Install Docker packages.] ***************************************************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Install Docker packages (with downgrade option).] ***************************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : Install docker-compose plugin.] *********************************************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Install docker-compose-plugin (with downgrade option).] *********************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : Ensure /etc/docker/ directory exists.] **************************************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Configure Docker daemon options.] *******************************************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Ensure Docker is started and enabled at boot.] ******************************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : Ensure handlers are notified now to avoid firewall conflicts.] **************************************************************************************
   
   TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Get docker group info using getent.] ****************************************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : Check if there are any users to add to the docker group.] *******************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
   skipping: [host_01]
   
   PLAY RECAP *********************************************************************************************************************************************************************
   host_01                    : ok=11   changed=0    unreachable=0    failed=0    skipped=12   rescued=0    ignored=0   
    ```

# Outputs for docker and web_app roles
```
ansible-playbook playbooks/dev/main.yml

PLAY [all] *********************************************************************

TASK [Gathering Facts] *********************************************************
Enter passphrase for key '/Users/nikitagrigorenko/.ssh/id_ed25519': 
Enter passphrase for key '/Users/nikitagrigorenko/.ssh/id_ed25519': 
ok: [host_01]

TASK [docker : Update apt] *****************************************************
ok: [host_01]

TASK [docker : Python3 and pip3 installation] **********************************
ok: [host_01]

TASK [docker : Install docker] *************************************************
ok: [host_01]

TASK [docker : Install docker compose] *****************************************
ok: [host_01]

TASK [web_app : Pull Docker image] *********************************************
changed: [host_01]

TASK [web_app : Run Docker container] ******************************************
changed: [host_01]

PLAY RECAP *********************************************************************
host_01                      : ok=7    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

- `ansible-inventory -i inventory/default_yandex_vm.yml --list`

    ```json
    {
        "_meta": {
            "hostvars": {
                "host_01": {
                    "ansible_host": "51.201.12.197",
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