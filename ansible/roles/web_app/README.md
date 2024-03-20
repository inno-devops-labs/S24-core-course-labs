# Overview
This role serves the purpose of setting up Docker using the APT package manager, configuring it with Docker Compose via pip, and then pulling the "xdrdvd/app_{python/golang}" image to run it on the server.

## Role Tasks
1. Stop: Stop the running containers, Verify the existence of Docker Compose.
2. Wipe: Completely remove all data associated with the containers 
3. Deploy: Deploy the "xdrdvd/app_{python/golang}" image with default settings. Optionally, allow the deployment of the bonus task with custom variables.
4. Include Task Files: Include all the individual task files in the main.yml for seamless execution.

## Usage
Utilize this role to configure Docker on managed nodes via Ansible and fetch the "xdrdvd/app_{python/golang}" image for execution.


## Dependencies
- Ansible
- Ubuntu
- Ensure the availability of the "../docker" role for proper role execution.
