# Ansible Role: Docker

An Ansible Role that installs [Docker](https://www.docker.com) on Ubuntu/Debian.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```python
    # Edition can be one of: 'ce' (Community Edition) or 'ee' (Enterprise Edition).
    docker_edition: 'ce'
    docker_packages:
        - "docker-{{ docker_edition }}"
        - "docker-{{ docker_edition }}-cli"
        - "docker-{{ docker_edition }}-rootless-extras"
    docker_packages_state: present
```

The `docker_edition` should be either `ce` (Community Edition) or `ee` (Enterprise Edition).
You can also specify a specific version of Docker to install using the distribution-specific format: `docker-{{ docker_edition }}=<VERSION>` (Note: you have to add this to all packages).

You can control whether the package is installed, uninstalled, or at the latest version by setting `docker_packages_state` to `present`, `absent`, or `latest`, respectively. Note that the Docker daemon will be automatically restarted if the Docker package is updated. This is a side effect of flushing all handlers (running any of the handlers that have been notified by this and any other role up to this point in the play).

```python
    docker_service_manage: true
    docker_service_state: started
    docker_service_enabled: true
    docker_restart_handler_state: restarted
```

Variables to control the state of the `docker` service, and whether it should start on boot. If you're installing Docker inside a Docker container without systemd or sysvinit, you should set `docker_service_manage` to `false`.

```python
    docker_install_compose_plugin: false
    docker_compose_package: docker-compose-plugin
    docker_compose_package_state: present
```

Docker Compose Plugin installation options. These differ from the below in that docker-compose is installed as a docker plugin (and used with `docker compose`) instead of a standalone binary.

```python
    docker_install_compose: true
    docker_compose_version: "1.26.0"
    docker_compose_arch: "{{ ansible_architecture }}"
    docker_compose_path: /usr/local/bin/docker-compose
```

Docker Compose installation options.

```python
    docker_add_repo: true
```

Controls whether this role will add the official Docker repository. Set to `false` if you want to use the default docker packages for your system or manage the package repository on your own.

```python
    docker_repo_url: https://download.docker.com/linux
```

The main Docker repo URL:

```python
    docker_apt_release_channel: stable
    docker_apt_arch: "{{ 'arm64' if ansible_architecture == 'aarch64' else 'amd64' }}"
    docker_apt_repository: "deb [arch={{ docker_apt_arch }}] {{ docker_repo_url }}/{{ ansible_distribution | lower }} {{ ansible_distribution_release }} {{ docker_apt_release_channel }}"
    docker_apt_ignore_key_error: True
    docker_apt_gpg_key: "{{ docker_repo_url }}/{{ ansible_distribution | lower }}/gpg"
    docker_apt_filename: ""
```

You can switch the channel to `nightly` if you want to use the Nightly release.

You can change `docker_apt_gpg_key` to a different url if you are behind a firewall or provide a trustworthy mirror.
Usually in combination with changing `docker_apt_repository` as well.

## Example Playbook

```yaml
- hosts: all
  roles:
    - docker
```
