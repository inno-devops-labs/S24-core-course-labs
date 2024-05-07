# Documentation

## components

### Inventory

This part contains `yandex_cloud.yml` file, which contains infomation about my VM in yandex cloud. 

The hostname there is called devops, with 51.250.104.24 as IPv4 address, and ubuntu system.

### Roles/Docker

This part contain some commads to download docker copose and docker on Linux VM.

- `install_compose.yml`: Contains information about for installing docker compose with the latest version

- `install_docker.yml`: install docker on linux with the current version

- `main.yml`: installs python3 and pip3, installs docker using install_docker.yml file, and install docker compose using docker_compose.yml file.

### Playbooks/Dev

This part contains the instructions to  instll docker compose and docker on the given VM.