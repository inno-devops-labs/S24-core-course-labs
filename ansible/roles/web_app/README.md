# Web Application Ansible Deployment Role

## Overview
This Ansible role facilitates the deployment of a web application. It handles tasks such as installing necessary dependencies like pip, Docker, Docker Compose, and launching a web server using docker-compose. Additionally, it provides a feature to wipe previous containers if required. All dependencies for this role are specified in the `meta/main.yaml` file.

## Usage
To use this Ansible role, follow these steps:

1. Add the role to your playbook, for example:
   ```yaml
   - name: Deploy Docker
     hosts: all
     roles:
       - ../../roles/web_app
   ```

2. Run the playbook like:
   ```bash
   ansible-playbook playbooks/dev/main.yaml --diff
   ```

Make sure to configure the IP address and SSH connection correctly. After successful execution, you can access the web application at `xxx.xxx.xxx.xxx:5000`, which displays the current time in Moscow.

## Requirements
- The target machine must be a VM with a publicly accessible IP address.
- The operating system should be Ubuntu.
- Python should be pre-installed on the target machine.
- A Docker image from DockerHub must be available.
