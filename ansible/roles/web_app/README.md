# web_app role

## Overview
It's an ansible role pulls vectorsmaster/flask-app image, run it, wipe docker container if stated

## Requirements

1. `ubuntu`.
2. `python`.
3. `docker` role.

## Usage (navigate into ansible directory)

1. `ansible-playbook playbooks/dev/main.yml -i inventory/yandex_cloud.yml`.
    - pull the image and run it inside container.
    - wipe the container.

2. `ansible-playbook playbooks/dev/main.yml -i inventory/yandex_cloud.yml --tags "deploy"`.
    - pull the image and run it inside container.

3. `ansible-playbook playbooks/dev/main.yml -i inventory/yandex_cloud.yml --tags "wipe"`.
    - wipe the container.

## Notes

- The container will be deployed at http://<host_ip>:5000

- You may need to upgrade ansible `pip install --upgrade ansible`. 

