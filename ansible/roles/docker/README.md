## Docker role

This folder contains Ansible role that installs docker and docker-compose 

### Requirements 

- Python 3
- Ubuntu

## Example of usage
```yaml
- name: Install Docker using existing role
  hosts: all
  become: true
  roles:
    - docker
```
