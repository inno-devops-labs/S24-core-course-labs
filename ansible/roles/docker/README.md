# Docker Ansible Role

This Ansible role is used for installing Docker and Docker Compose on Ubuntu systems.

## Requirements

- Ansible 2.0+
- Ubuntu operating system

## Role Variables

This role does not have any configurable variables.

## Dependencies

This role has no external dependencies.

## Example Playbook

```yaml
- name: Deploy Docker
  hosts: all
  become: true
  roles:
    - docker
```
