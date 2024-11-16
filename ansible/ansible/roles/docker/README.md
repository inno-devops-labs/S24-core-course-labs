# Ansible docker role

This is an Ansible role to install Docker and Docker Compose.

## Requirements 

- Ubuntu (any version0)
- Python 3
- pip3
- Ansible 3.10+

## Usage

Add role to your playbook:
```yaml
  roles:
    - role: ../../roles/docker
      become: true
```