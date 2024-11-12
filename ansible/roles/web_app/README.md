# Docker role
Deploys a docker image on an apt-based linux machine using compose.

## Requirements
For hosts:
- Ubuntu/debian (apt package manager)
- No docker/docker-compose installed previously(optional)
- python3 installed

## Variables
- web_app_full_wipe: wipe the compose project directory? (default: false)
- docker_image: docker image to deploy (default: n0m1nd/moscow_time_python:latest)
- service_name: compose service name (default: web_app)
- docker_port_string: string to pass to "ports" in the compose file (default: 8080:8080)
- compose_dir: directory to put the docker-compose file (default: . - the home directory probably)

## Usage
Add to any playbook with the desired variable values.
