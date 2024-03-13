# Ansible

## Commands

Install ansible, docker role and aws collection:

```bash
ansible-galaxy role install geerlingguy.docker
ansible-galaxy collection install amazon.aws 
```

## Best practices

- Organized basing on provided template
- All tasks have proper naming
- `ansible.cfg` is used for configurations (including private key file)
