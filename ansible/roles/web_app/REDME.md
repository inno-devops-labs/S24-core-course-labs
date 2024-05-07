# web app role

role for depoloying docker image to remote machine

## requirements

- ubuntu virtual machine
- docker
- docker-compose
- python
- pip

## How to use for python

To deploy it is enough to run 

```sh
ansible-playbook playbooks/dev/app_python/main.yml --tags  "deploy"
```

from `/ansible` directory


To wipe you can run

```sh
ansible-playbook playbooks/dev/app_python/main.yml --tags  "wipe"
```

## How to run for dotnet

To deploy it is enough to run 

```sh
ansible-playbook playbooks/dev/app_dotnet/main.yml --tags  "deploy"
```

from `/ansible` directory


To wipe you can run

```sh
ansible-playbook playbooks/dev/app_dotnet/main.yml --tags  "wipe"
```