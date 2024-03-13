# The `web_app` Role

This role installs the Python web application (Moscow time) using Docker.

## Requirements

- Ubuntu 22 or later is used
- Python 3.8+ installed
- pip installed
- apt installed

## Example Playbook

```yaml
- name: Moscow Time Web App
  hosts: all
  roles:
    - role: roles/web_app
      become: yes
```
