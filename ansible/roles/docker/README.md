# Docker Role

## Overview

This Ansible role sets up Docker on Ubuntu by installing it, managing system packages, setting up the Docker repository, and installing Docker Community Edition.
## Requirements

- Python 3 or later
- Ansible 2.16 or later
- Ubuntu 18.0 or later
- pip installed

## Role Variables

- `docker_pip_package`: The Docker Compose package name to be installed.


## Example Playbook

```yaml
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker