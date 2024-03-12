# Web App Role

Using Docker, this Ansible role is used to deploy and manage web applications. It also depends on the docker role.

## Requirements

- Ansible installed
- Target should be Debian-based host
- Target host should be with docker and docker-compose installed

### Usage

1. Define your playbook as it shown in the file
2. Define `inventory/hosts.yml` as the inventory file;
3. Launch the playbook from the `ansible-playbook playbooks/dev/main.yml` ansible folder.