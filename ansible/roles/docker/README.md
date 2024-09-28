# Docker Role

This Ansible role installs and configures Docker on target hosts. It simplifies the process of managing Docker installations and ensures consistent setup across multiple servers.

## Requirements

- Ansible installed on the control machine.
- Target hosts accessible via SSH.

## Role Variables

The following variables can be customized in your playbook or inventory:

- `docker_edition`: Choose between 'ce' (Community Edition) or 'ee' (Enterprise Edition).
- `docker_packages`: List of Docker packages to install.
- `docker_packages_state`: Desired state (e.g., `present` or `latest`).

Dependencies
------------

No specific dependencies are required for this role.

Example Playbook
----------------

Create a playbook that uses this role:
```yaml
    - hosts: localhost
  roles:
    - { role: ../../roles/docker }
  become: true

  vars:
    container_name: almetovkamil/app_python:v2

  tasks:
    - name: Pull default Docker image
      command: "docker pull {{ container_name }}"

    - name: Run docker container
      command: "docker run -d -p 5000:5000 {{ container_name }}"
```
License
-------

BSD