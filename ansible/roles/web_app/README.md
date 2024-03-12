# Ansible Role: web_app 

This Ansible role is designed to deploy a Dockerized web application.

## Role Variables

- **web_app_full_wipe:** (boolean) Determines whether to perform a full wipe of the application.

## Example Playbook

```yaml
- name: Deploy Web Application
  hosts: servers
  roles:
    - web_app
