# Custom Docker role

## Description and requirements

### Deps
- `geerlingguy.pip`  
- `geerlingguy.docker`
- Only for Debian-based GNU/Linux distribution

### Role Variables
- `docker_gpg_apt_key_url`: docker GPG APT key URL
- `docker_apt_repository`: docker APT repository URL
- `docker_pip_compose_version`:  version of Docker Compose to install (via `pip`)

### Description
This role stands for deployment of `docker` and `docker-compose` to the targeted hosts with all required dependies. 
This role also turning on docker daemon and genneraly prepare target host os to run docker containers and build infrastructure of multi-docker containers with docker-compose utilization

## Usage
- Utilize this role by installing deps and adding it into your playbook, nothing in addition required

- Example of playbook:

    ```
    - name: AnsibleLab-05
      hosts: all
      become: true
      roles:
        - docker
    ```