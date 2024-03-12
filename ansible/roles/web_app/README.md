# "web_app" ansible role

This role installs docker-compose and app image and starts docker container (having docker role as dependency)

## Requirements

- Ansible 2.9 or later

## Requirements for the hosts

- Ubuntu (any verison)
- python3

## Variables

```app_image``` - the docker image

```dir``` - work directory, where `compose.yml` is placed

```app_port``` - port

```web_app_full_wipe``` - flag for wipe process

## Usage

1. Configure the playbook:

    ```bash
    - name: Deploy
      hosts: all
      become: true

      roles:
        - role: ../../../roles/web_app
      vars:
        dir: app_python
        app_image: pgrammer/app_python
        app_port: 5000
        web_app_full_wipe: false
    ```

2. Configure inventory file

    ```bash
    my_hosts:
      hosts
        host_01:
          ansible_host: 178.154.223.167
          ansible_user: ubuntu
    ```

3. Run the playbook to deploy and set `web_app_full_wipe` to `false`

    ```bash
    ansible-playbook playbooks/dev/app_python/main.yml -i inventory/default_yc_ec2.yml
    ```

4. Destroy after if needed (`web_app_full_wipe` to `true`)

    ```bash
    ansible-playbook playbooks/dev/app_python/main.yml -i inventory/default_yc_ec2.yml --tags "wipe"
    ```

