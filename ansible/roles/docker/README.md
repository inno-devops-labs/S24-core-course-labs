# The `docker` Role

This role installs docker and docker-compose on a host.

## Requirements

- Ubuntu 22 or later is used
- Python 3.8+ installed
- pip installed
- apt installed

## Example Playbook

```yaml
- name: Install Docker and Docker Compose
  hosts: all
  roles:
    - role: docker
      become: true
```
