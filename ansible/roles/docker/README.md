# Docker and docker-compose role

Which tasks this role is responsible for:

- Install docker
- Install docker compose
- Meet all official documentation's requirements

## How to use

```sh
---
- name: Deploy Docker
hosts: all
become: true
roles:
    - role: ../../roles/docker
```
