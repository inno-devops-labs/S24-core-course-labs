# Role for webapp deployment

Depends on Docker role

## Requirements

Tested only on Ubuntu 22.04

## Effects

1. Creation of a folder for webapp
2. Setting up parametrized docker-compose file (from templates folder) there
3. Applying docker-compose

## Variables

- `web_app_image`: remote web-app image (e.g. `dirakon/devops-py:latest`)
- `web_app_folder`: folder on host machine to put docker-compose file in
- `web_app_host_port`: host port for webapp
- `web_app_container_port`: in-container port for webapp
- `web_app_full_wipe`: true/false (wipe or no wipe)

## Wipe

Wipe is unlocked with variable above. You can run wipe specifically with tag `wipe`.

I.e., run the usual playbook command with `--tags "wipe"`

## Usage