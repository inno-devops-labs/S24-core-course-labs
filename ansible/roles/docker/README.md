# Docker role

This is an Ansible role to install Docker and Docker Compose.

## Requirements for the hosts

- Ubuntu of any version;
- Python 3.

## Usage

```yaml
- hosts: all
- roles:
    - role: docker
      become: true # if not root already
```
