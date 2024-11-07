# Docker role

This is an Ansible role to install Docker and Docker Compose.

## Requirements for the hosts

- Ubuntu (any version0)
- Python 3
- Ansible 3.10+

## Usage

Add the 'mine docker' role to your playbook:
```yaml
  roles:
    - role: ../../roles/mine docker
      become: true
```