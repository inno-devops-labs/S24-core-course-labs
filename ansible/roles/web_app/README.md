# Web App Role

## Overview

This Ansible role deploys a docker-compose file with defined services. With the wipe flag on, it stops running containers and deletes associated images from the host.
## Requirements

- Python 3 or later
- Ansible 2.16 or later
- Ubuntu 18.0 or later
- pip installed


## Example Playbook

```yaml
---
- name: Install Docker
  hosts: all
  become: true
  roles:
    - docker

- name: Deploy Web App
  hosts: all
  become: true
  roles:
    - web_app
```

### The playbook with the role can be ran inside the ansible folder with the following command:
```bash
ansible-playbook playbooks/dev/main.yml
```