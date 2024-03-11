## Docker Role

Ansible role that installs Docker and Docker Compose on the remote host

### Requirements
- Ubuntu 22.04
- Ansible 3.10+

### Usage

Add the following role to your playbook:
```yaml
roles:
  - role: docker
    become: true
```

Also, make sure that correct host from the inventory is specified for the role.