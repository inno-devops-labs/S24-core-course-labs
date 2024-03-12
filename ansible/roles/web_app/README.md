# Application Deployment Role for Web Services

This role facilitates the installation of the application image and initiates the Docker container, with a prerequisite of the Docker role.

## Requirements

- Ansible version 2.9 or later

## Host Requirements

- Installed python3

## Variables
1) ```python_dir```: Specifies the directory path to place the compose.yml file.

2) ```app_port```: Indicates the port for mapping from Docker to the host.

3) ```app_image```: Refers to the Docker image of the application.

4) ```web_app_full_wipe```: Allows enabling or disabling of the wipe process via a variable.


## Usage

1) Configure the playbook as detailed in ```/playbooks/dev/main.yml```, ensuring that ```web_app_full_wipe``` is set to false for initial deployment.

2) Set up the inventory file at ```/inventory/default_aws_ec2.yml```.

3) Execute the playbook for deployment:
```bash
ansible-playbook playbooks/dev/main.yml -i inventory
```

4) If required, perform cleanup by setting ```web_app_full_wipe``` to ```true``` and run:

```bash
ansible-playbook playbooks/dev/main.yml -i inventory --tags "wipe"
```