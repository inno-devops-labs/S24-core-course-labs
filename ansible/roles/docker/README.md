# docker

This Ansible role facilitates the installation of Docker and Docker Compose on Ubuntu systems.

## Requirements

- Python 3
- Ansible
- apt

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
```

**Note:** Replace `all` with the appropriate hosts or group from your inventory. This example playbook integrates the `docker` role into your configuration, ensuring a streamlined installation of Docker and Docker Compose on your specified hosts.