# `web_app` Role

## Overview

The `web_app` role is designed to facilitate the deployment of web apps Docker images to remote machines.

## Requirements

To use this role, ensure the following prerequisites are met on your Ubuntu virtual machine:

- `Ubuntu`
- `Python`
- `Pip`
- Ansible installed on the host machine.
- `npm` for JS app

## Configuration Variables

The `web_app` role uses the following variables:

- **`app_port`**: The port on which the Python web application will run.
- **`app_name`**: The name of the web application.
- **`app_dir`**: The directory where the application will be deployed.
- **`image_tag`**: The tag of the Docker image to be deployed. Default value: `latest`.
- **`host_name`**: The hostname of the remote machine. It is the ansible host name: `(ansible_host)`.
- **`image_name`**: The name of the Docker image. The default value: `ghadeero/(app_name)`.
- **`web_app_full_wipe`**: A boolean indicating whether to perform a full wipe of the web application.

## Usage

To deploy the web Python application, execute the following command from the `/ansible` directory:

```sh
ansible-playbook playbooks/dev/python_app/main.yml --tags "deploy"
```

To do a full wipe of the deployment, run:

```sh
ansible-playbook playbooks/dev/python_app/main.yml --tags "wipe"
```