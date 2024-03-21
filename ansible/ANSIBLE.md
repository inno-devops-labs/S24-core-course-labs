# Ansible

1. Repository Structure: Done as advised

2. Installing Ansible
    ```sh
    python3 -m pip install --user ansible
    ```

3. Adding an existing role for Docker
    ```sh
    ansible-galaxy role install geerlingguy.docker
    ```
4. Running a playbook

    ```sh
    $ ansible-playbook playbooks/dev/main.yaml --diff

    PLAY [Install Docker and Docker Compose] ************************************************************************************************************************************************

    TASK [Gathering Facts] ******************************************************************************************************************************************************************
    ok: [ec2-18-170-41-216.eu-west-2.compute.amazonaws.com]

    TASK [docker : Download pip installation script] ****************************************************************************************************************************************
    ok: [ec2-18-170-41-216.eu-west-2.compute.amazonaws.com]

    TASK [docker : Install pip] *************************************************************************************************************************************************************
    ok: [ec2-18-170-41-216.eu-west-2.compute.amazonaws.com]

    TASK [docker : Refresh apt packages] ****************************************************************************************************************************************************
    ok: [ec2-18-170-41-216.eu-west-2.compute.amazonaws.com]

    TASK [docker : Install/Update docker.io] ************************************************************************************************************************************************
    ok: [ec2-18-170-41-216.eu-west-2.compute.amazonaws.com]

    TASK [docker : Install docker] **********************************************************************************************************************************************************
    ok: [ec2-18-170-41-216.eu-west-2.compute.amazonaws.com]

    TASK [docker : Install docker-compose] **************************************************************************************************************************************************
    ok: [ec2-18-170-41-216.eu-west-2.compute.amazonaws.com]

    PLAY RECAP ******************************************************************************************************************************************************************************
    ec2-18-170-41-216.eu-west-2.compute.amazonaws.com : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
    ```


5. Inventory details
    ```
        $ ansible-inventory --list
        {
            "_meta": {
                "hostvars": {
                    "ec2-18-170-41-216.eu-west-2.compute.amazonaws.com": {
                        "ansible_connection": "ssh",
                        "ansible_user": "ubuntu"
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
                    "ec2-18-170-41-216.eu-west-2.compute.amazonaws.com"
                ]
            }
        }
    ```

### Best practices
- Implements suggested repository structure
- Uses `ansible.cfg` for configurations
- Implements modular tasks