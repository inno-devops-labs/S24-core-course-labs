# Role

- Install Docker repository to apt
- Install pip, Docker, Docker Compose

## Usage

```
---
- name: Install Docker
  hosts: all
  remote_user: user
  become: true

  roles:
    - <...>/docker
```