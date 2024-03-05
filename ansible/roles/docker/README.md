# Docker Configuration Role

This role facilitates the installation and configuration of Docker along with Docker Compose on designated hosts.

## Prerequisites

- Ansible version 2.9 or later

## Host Requirements

- Ubuntu (any version)
- Python3

## Implementation

1. Prepare the playbook:

```yaml
- name: Install Docker Manually
  hosts: all
  become: true

  roles:
    - role: docker
      become: true

2. Create an Inventory File:

```yaml
my_hosts:
  hosts:
    host_01:
      ansible_host: 51.250.72.152
      ansible_user: ubuntu
```

3. Execute the Playbook:

```bash
ansible-playbook playbooks/dev/main.yml
```

