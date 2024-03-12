## web_app role

The role installs the app image and starts the docker container

## Requirements

- Ubuntu
- Python 3

## Variables

| Variable            | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `app_dir`           | the directory, where to place docker-compose.yml file |
| `app_image`         | the docker image                                      |
| `app_port`          | port to map from host to docker                       |
| `web_app_full_wipe` | wtether to wipe or not                                |
