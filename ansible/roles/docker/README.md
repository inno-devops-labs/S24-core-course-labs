# Docker and docker-compose role

This role installs docker in the same manner as it is described
in [official manual](https://docs.docker.com/engine/install/ubuntu/).

Also, it installs docker-compose using pip.

## Requirements

+ Ubuntu
+ Meet all requirements from [official manual](https://docs.docker.com/engine/install/ubuntu/#prerequisites)

## Usage

```
- roles:
  - name: "Install docker and docker-compose"
    role: docker
```