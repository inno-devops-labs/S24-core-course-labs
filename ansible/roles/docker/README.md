# Docker Role

This Ansible role installs and configures Docker on target hosts.

## Requirements

- Ansible 2.9 or later
- Target hosts running Ubuntu 20.04 or Debian 10

## Role Variables

The following variables can be customized in your playbook:

- `docker_gpg_apt_key_url`: URL of the Docker GPG APT key
- `docker_apt_repository`: Docker APT repository URL
- `docker_pip_compose_version`:  The version of Docker Compose to install using
  pip

## Dependencies

- `apt`
- `python3`

## Example Playbook

```yaml
---
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker
```
