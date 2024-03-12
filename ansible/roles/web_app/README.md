# web_app

This Ansible role facilitates the deployment and management of a Flask-based web application running within a Docker container.

## Requirements
------------
This role has a dependency on the `docker` role. Ensure the `docker` role is included in your playbook or inventory file.

## Role Variables
--------------
The following variables can be configured:
- `docker_image_name`: Name of the Docker image to be used.
- `docker_container_name`: Name of the Docker container.
- `port`: Port to expose the web application.
- `web_app_full_wipe`: Boolean flag to determine whether to perform a full wipe (removing container and image).
- `service_name`: Name of the service defined in `docker-compose.yml`.

## Usage
1. Define role variables in your playbook or inventory files as needed.
2. Include the `docker` role in your playbook to ensure Docker and Docker Compose are installed or install them by yourself.
3. Include this role in your playbook.
4. Run your playbook to deploy and manage the Flask web application.

## Task Overview
- **Pull Docker Image**: Pulls the specified Docker image if not present locally.
- **Run Docker Container**: Starts a Docker container based on the specified image.
- **Deliver docker-compose.yml file**: Copies the `docker-compose.yml.j2` template file to the desired location.
- **Wipe Docker Container and Files**: Removes Docker container and image if `web_app_full_wipe` is set to true.

## Tags
Each task in this role is tagged for better control during playbook execution:

- `pulldocker`: Pulls the Docker image.
- `runcontainer`: Runs the Docker container.
- `deploy`: Handles deployment tasks.
- `createcompose`: Delivers the docker-compose.yml file.
- `wipe`: Performs wiping tasks if web_app_full_wipe is set to true.
- `stopcontainer`: Stops and removes the Docker container.
- `removedockerimage`: Removes the Docker image.
- `errorhandling`: Handles errors during wiping.

## Note
- Wiping actions are conditional on `web_app_full_wipe` to prevent accidental data loss.
