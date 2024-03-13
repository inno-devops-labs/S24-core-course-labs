# `Docker` Role
A role designed to deploy Docker and Docker Compose on a target host.

## Overview
This role automates the installation of Docker and Docker Compose on a host machine. It specifically utilizes the docker.io distribution for Docker and installs Docker Compose using pip.

## Requirements

- `Ubuntu`
- `Python`
- `pip`
- Ansible installed on the control machine.

## Usage
1. Clone the repository to your local machine.
2. Navigate to the `ansible` directory.
3. Update the inventory file (`inventory/default_aws_ec2.yml`) with your target hosts.
4. Modify the playbook (`playbooks/dev/main.yaml`) if needed.
5. Run the playbook to deploy Docker:
   ```bash
   ansible-playbook -i inventory/default_aws_ec2.yml playbooks/dev/main.yml