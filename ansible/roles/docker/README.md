# Ansible Role: Docker

## Overview

This Ansible role facilitates the installation of Docker and Docker Compose on Ubuntu systems. It streamlines the installation process by ensuring the presence of essential system packages, adding the Docker GPG apt key, configuring the Docker repository in the apt sources, and installing Docker Community Edition (docker-ce). Additionally, the role includes the flexibility to install Docker Compose with a specified package name.

## Requirements

- Python 3
- Ansible

## Role Variables

- `docker_pip_package`: The package name for Docker Compose. Default is set to "docker-compose."

## Dependencies

- python3
- apt

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: docker
```

**Note:** Replace `all` with the appropriate hosts or group from your inventory. This example playbook integrates the `docker` role into your configuration, ensuring a streamlined installation of Docker and Docker Compose on your specified hosts.