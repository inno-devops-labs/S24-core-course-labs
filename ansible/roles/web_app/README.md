# web_app Ansible Role

This Ansible role is designed to deploy a Dockerized web application.

## Requirements

- Ansible
- Docker

## Role Variables

- `web_app_full_wipe`: (boolean) Determines whether to perform a full wipe of the application.

## Dependencies

This role depends on the Docker role.

## Example Playbook

```yaml
- name: Deploy Web Application
  hosts: servers
  roles:
    - web_app
