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

---

# Web App Role

The Web App Role is an Ansible role that is designed to deploy and manage web applications using Docker. It is dependent on the Docker role.

## Requirements

To use this role, the following requirements must be met:

- Ansible must be installed on the system.
- The target host should be a Debian-based host.
- Docker and Docker Compose must be installed on the target host.

### Usage

To use the Web App Role, follow these steps:

1. Define your playbook using the provided template.
2. Define the inventory file at `inventory/hosts.yml`.
3. Launch the playbook by running `ansible-playbook playbooks/dev/main.yml` from the Ansible folder.

By following these steps, you can easily deploy and manage web applications using Docker with the help of the Web App Role.
