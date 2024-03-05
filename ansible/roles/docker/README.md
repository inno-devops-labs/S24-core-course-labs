## Ansible roles
**docker**

This role installs Docker and Docker-compose on host specified.

**geerlinguy.docker**

This role is installed by `ansible-galaxy role install geerlingguy.docker` command for the 1.3 task.

## Requirements
- Host OS - Ubuntu

## Dependencies
- `python3`
- `apt`

## Example playbook
```
- name: Docker roles
  hosts: all
  become: true

  roles:
    - dockers
```
