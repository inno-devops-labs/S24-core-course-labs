# `docker` Role

A role to install docker and docker-compose on a host.

## Description

The role installs docker and docker-compose on a host. For docker, it uses the ubuntu distribution `docker.io`. For docker-compose, it uses `pip3` to install the package. If pip3 is not installed, the role will install it.

## Requirements

- Ubuntu 18.04 or later
- Python 3.6 or later
- `pip3` installed

## Prerequisites

This is more likely that there will be issues installing docker if previous version from different distributions (i.e. `docker-engine` and `docker-ce`) are installed. If you have any of these packages installed, remove them before running this role. However, having `docker.io` installed previously will not cause any issues.

The role also works on Debian-based distributions only where `apt` is the package manager.

## Example Playbook

There are no variable required for this role. However, your user must have the correct permissions to install packages on the host. Use `become: true` to run the role as root.

```yaml
- name: Install Docker and Docker Compose
  hosts: my_hosts
  roles:
    - role: docker
      become: true
```

## License

MIT License
