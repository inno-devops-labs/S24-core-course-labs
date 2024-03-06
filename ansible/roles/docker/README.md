# Ansible Role: Docker

This Ansible role installs Docker and Docker Compose on Ubuntu systems.

## Requirements

- Ansible installed on the control machine.
- Target hosts running Ubuntu.

## Role Variables

- `docker_repo_changed`: Variable to check if Docker repository configuration has changed. (Default: false)

## Dependencies

None

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: ansible/roles/docker
