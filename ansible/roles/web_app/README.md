# `web_app` role

This is the role that is deploying `brutaljesus/devops_lab_2` image to the server. 
This role also can wipe the deployment.

## Requirements

- Ubuntu server
- Python installed on that server
- `docker` role

## How to use

If we want to deploy, we have to run:
```
ansible-playbook playbooks/dev/playbook.yaml -i inventory/inventory.yaml --tags "deploy"
```

If we want to wipe the deployment, we have to run:
```
ansible-playbook playbooks/dev/playbook.yaml -i inventory/inventory.yaml --tags "wipe"
```