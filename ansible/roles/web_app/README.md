# Custom Ansible Role: Docker

This Ansible role is designed to install web application (Moscow time) on target hosts.

## Tasks

1. Install pip
2. Install Docker
3. Install Docker Compose

## Usage

1. Add this custom role to your Ansible roles directory.
2. Update your playbook to include this role.
3. Run your playbook to deploy install web application (Moscow time) on target hosts.

## Example Playbook

```bash
- hosts: all
  roles:
  - role: roles/docker
      become: yes
```

## Testing

You can test this role by running the playbook with the custom role included:
`ansible-playbook -i inventory playbook.yml`
Feel free to customize and expand upon this role to suit your specific requirements.
