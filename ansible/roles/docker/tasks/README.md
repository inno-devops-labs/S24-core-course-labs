# Docker role

## Description

This is Docker ansible role. It installs Docker on Ubuntu 22.04.    

## Requirements

* `apt` must be pre-installed on the target machine.
* Configure variables in defaults.main.yml:

```shell
docker_compose_version: "latest"
docker_version: "latest"
```

## Usage

Include `docker` role in `playbooks/dev/main.yml`

```shell
- name: Deploy Docker
  hosts: all
  become: true
  roles:
    - docker
```