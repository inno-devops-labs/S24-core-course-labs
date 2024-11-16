## Docker role

Ansible role to install Docker and Docker Compose.

## Requirements

- Ubuntu/WSL
- Python 3
- Ansible 3.10+

## Usage

Add the the role to your playbook:
  roles:
    - role: ../../roles/docker
      become: true