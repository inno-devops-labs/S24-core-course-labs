# Docker & Docker-Compose installation role

A role for ansible to install the latest version of Docker community edition
(via apt) and the docker-compose plugin (via pip).

## Requirements

The role will only run on a machine running **Debian** or **Ubuntu**.

## Usage

As the role does not have any variables that its behavior depends on, to use
the role, you need to just include the following in your playbook:
```
roles:
  - name: "Install docker"
    role: docker
```
