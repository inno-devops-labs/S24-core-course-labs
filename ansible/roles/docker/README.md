# Docker

An Ansible Role that installs Docker on Linux.

This Ansible role automates the installation and configuration of Docker on Ubuntu systems. It ensures that Docker
Community Edition (CE) along with Docker Compose is set up correctly.

## Requirements

* Ubuntu operating system
* Ansible installed on the control node
* Internet connectivity to download Docker packages
* User with sudo privileges on the target host

## Usage

1. Clone the repository containing the Ansible playbook and roles.
2. Update the inventory file (`ansible/inventory/default_yc_ec2.yml`) with the IP addresses or hostnames of your target
   hosts.
3. Modify the `ansible/playbooks/dev/main.yaml` playbook to include the docker role.
4. Run the playbook with the following command:

   ```bash
   ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml 
   ```

5. Let Ansible automate the installation and configuration of Docker on your target hosts.
