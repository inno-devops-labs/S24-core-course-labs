- `ansible-playbook playbooks/dev/main.yml --diff`

    ```text
   PLAY [Install Docker] **********************************************************************************************************************************************************
   
   TASK [Gathering Facts] *********************************************************************************************************************************************************
   Enter passphrase for key '/Users/evgeniygerasimov/.ssh/id_ed25519': 
   ok: [host_01]
   
   TASK [geerlingguy.docker : Load OS-specific vars.] *****************************************************************************************************************************
   ok: [host_01]
   
   TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
   skipping: [host_01]
   
   TASK [geerlingguy.docker : include_tasks] **************************************************************************************************************************************
   included: /Users/evgeniygerasimov/Documents/Homeworks/S24-DevOps-labs/ansible/roles/geerlingguy.docker/tasks/setup-Debian.yml for host_01
   
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

- `ansible-inventory -i inventory/default_yandex_vm.yml --list`

    ```json
    {
        "_meta": {
            "hostvars": {
                "host_01": {
                    "ansible_host": "84.201.157.197",
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