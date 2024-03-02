# Docker role for Ansible

This is simple custom Docker role for Ansible.

## Usage

```
    - hosts: web_server
      roles:
        - role: ../../roles/docker
        become: true
```