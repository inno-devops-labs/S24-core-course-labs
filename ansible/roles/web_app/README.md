# Web App Ansible Role

## General description

- This role is used to deploy a web application using Docker Compose.
- It has two tasks (wipe and deploy) split into sub-tasks.
- Wipe task is used to remove the existing application and deploy task is used to deploy the new application.
- Deploy task is used to create a directory, create a docker-compose.yml file and deploy the application using Docker Compose.
- Logs for ansible-playbook playbooks/dev/web_app.yml are stored in ANSIBLE.MD
- It loosely follows suggested structure:

  ```sh
  .
  |-- defaults
  |   `-- main.yml
  |-- meta
  |   `-- main.yml
  |-- tasks
  |   `-- wipe.yml
  |   `-- deploy.yml
  |   `-- main.yml
  `-- templates
     `-- docker-compose.yml.j2
  ```

## Requirements

- This role requires premade Docker role and image hosted on Docker Hub.

## Usage

- To use this role, you need to include it in your playbook and provide the required variables.
