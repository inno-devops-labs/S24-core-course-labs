# Ansible Role: Docker

## Overview

This Ansible role automates the installation of Docker on Ubuntu systems. It ensures the presence of necessary system packages, adds the Docker GPG apt key, configures the Docker repository in the apt sources, and installs Docker Community Edition (docker-ce).

## Requirements

- Python 3
- Ansible

## Dependencies

- python3
- apt

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: docker
