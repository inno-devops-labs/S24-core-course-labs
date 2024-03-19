# Ansible Role: Docker

An Ansible Role that installs [Docker](https://www.docker.com) and [Docker Compose](https://docs.docker.com/compose/) on Ubuntu.

It uses `apt` Docker repository and installs Docker Compose via `pip`

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
ubuntu_version: "jammy"
```

Specifies Ubuntu version used for Docker repository.

```yaml
pip_package: "python3-pip"
```

Specifies the name of the `pip` package.

```yaml
docker_package: "docker-ce"
docker_repo_url: "https://download.docker.com/linux/ubuntu"
docker_release_channel: "stable"
```

`docker_package` specifies the name of Docker package, `docker_repo_url` and `docker_release_channel`
specify the repository URL and release channel for Docker respectively.

```yaml
docker_compose_pip_package: "docker-compose"
```

Specifies the name of the Docker Compose package for `pip`.

## Dependencies

None.
