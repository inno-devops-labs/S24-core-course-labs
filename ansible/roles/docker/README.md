# `docker` Role
A role to install docker and docker-compose on a host.

## Description
The role installs docker and docker-compose on a host. For docker, it uses the ubuntu distribution `docker.io`. For docker-compose, it uses `pip` to install the package.

## Requirements

- Ubuntu 18.0 or later
- Python 3.5 or later
- `pip` installed

## Prerequisites
Make sure a different distribution for docker such as `docker-engine` or `docker-ce` are not installed.The desired distribution is `docker.io` and if it was installed previously it will not cause a problem.

For this role to work, `apt` should be the package manager.

## Example Playbook

```yaml
- name: Install Docker and Docker Compose
  hosts: all
  roles:
    - role: <path-to-custom-role>
      become: true
```
