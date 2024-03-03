## Docker role

The role installs and configures docker and docker compose on target hosts.

## Requirements

- Ansible 2.9 or later

## Requirements for the hosts

- Ubuntu (any verison)
- python3

## Usage

1. Set up the playbook

```bash
- name: Install docker manually
  hosts: all
  become: true

  roles:
    - role: docker
        become: true
```

2. Set up inventory file

```bash
my_hosts:
  hosts
    host_01:
      ansible_host: 84.201.130.157
      ansible_user: bulatok
```

3. Run the playbook

```bash
ansible-playbook playbooks/dev/main.yml
```