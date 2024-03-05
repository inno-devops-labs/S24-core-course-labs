# Docker role

## Requirements for the hosts

- Ubuntu 
- Python 3

## Usage

1. Set up the playbook

```yaml
- name: Install docker manually
  hosts: all
  become: true

  roles:
    - role: docker
      become: true
```

2. Set up the inventory

```yaml
my_hosts:
  hosts:
    host_1:
      ansible_host: 82.97.244.125
      ansible_user: metafates
```

3. Run the playbook

```bash
ansible-playbook playbooks/dev/main.yml
```