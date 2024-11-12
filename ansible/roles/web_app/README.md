# Ansible web_app role

Install qexik1/flask-time-server docker image and run it on port 5000.

# Requirements

## Control node requirements

Host requirements are described in the [docs](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#control-node-requirements).

Basically, any UNIX machine with Python installed will suffice.

## Managed node requirements

Basic managed node requirements are described in the [docs](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#managed-node-requirements).

Current implementation also assumes that apt is present. Therefore, docker could only be installed on debian-based distros using this role.
