# Docker role

Tasks:

- Setup repo
- Install dependencies
- Setup folder
- Add Docker apt key and docker repository
- Disable Unattended Upgrades
- Install pip
- Install Docker using apt and Docker Compose using pip

## How to use

```yaml
---
- name: Deploy Docker on Yandex Cloud
  hosts: all
  remote_user: user
  become: true

  roles:
    - <path-to-roles>/docker
```