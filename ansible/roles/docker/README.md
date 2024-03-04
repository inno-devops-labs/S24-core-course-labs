# Docker role

## Description

Ansible role that installs `docker` and `docker-compose` on target hosts.

## Requirements

 - `Ansible` 2.16
 - `python` 3.12
 - `Ubuntu` and `python3` on the target host

## Example playbook

```yaml
---
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker

  vars:
    ansible_ssh_private_key_file: <path_to_file>
    ansible_user: <username>
    ansible_python_interpreter: <python_interpreter_path>
```

In this playbook, you should specify the following variables:

 - `path_to_file` - path to the private ssh key on your machine.
 - `username` - name of the user on the host.
 - `python_interpreter_path` - path to the python interpreter on the host.

In inventory file you should specify the hosts that will be used.
