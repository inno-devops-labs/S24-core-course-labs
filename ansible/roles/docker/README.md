# Docker

## Steps: 

### 1. Install pip
- simply installs python3-pip using apt

### 2. Install Docker (install_docker.yml)
- install the dependencies specified in ``defaults`` with ``update_cache`` flag set to ``true`` to fetch the latest updates.
- Add docker apt key to apt.
- Add docker repository to apt.
- Install docker and all related packages.

### 3. Install Docker-compose (install_compose.yml)
- install the dependencies specified in ``defaults`` with ``update_cache`` flag set to ``true`` to fetch the latest updates.
- Upgrade ``pip`` to the latest version.
- Installs docker-compose via ``pip``.

## How to use
You can use it within your playbook with root privileges.

Example (from playbooks/dev/main.yml):
```
- name: Deploy docker
become: yes
hosts: all
roles:
    - docker
```

