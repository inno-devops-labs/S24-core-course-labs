# Docker Role for Ansible

This role installs and configures Docker on your target hosts. It's designed to make it easier to manage Docker installations and ensure a consistent setup across different environments.

## Requirements

- Target hosts should be running Ubuntu 18.04 or higher.
- Python 3.6 or higher should be installed on the target hosts.
- `pip3`

## Example Playbook

Including the Docker role in your playbook is straightforward:

```yaml
- hosts: all
  roles:
    - { role: docker, docker_users: ['ubuntu'] }
```

This playbook runs the Docker role on all hosts, adding the `ubuntu` user to the `docker` group.