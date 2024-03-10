## web_app role for application

The role installs the app image and starts the docker container (having docker role as dependency)

## Requirements

- Ansible 2.9 or later

## Requirements for the hosts

- Ubuntu (any verison)
- python3

## Variables
```app_dir``` - the directory, where to place compose.yml file

```app_image``` - the docker image of app

```app_port``` - port to map from to docker to host

```web_app_full_wipe``` - wipe process can be enabled or disabled by using a variable


## Usage

1. Set up the playbook (example for python app, could be any)

```bash
- name: Deploy python app
  hosts: all
  become: true

  roles:
    - role: ../../../roles/web_app
  vars:
    app_dir: app_python
    app_image: bulatok4/app_python
    app_port: 8080
    web_app_full_wipe: true
```

2. Set up inventory file

```bash
my_hosts:
  hosts
    host_01:
      ansible_host: 84.201.130.157
      ansible_user: bulatok
```

3. Run the playbook to deploy only by setting ```web_app_full_wipe``` to ```false```

```bash
ansible-playbook playbooks/dev/app_python/main.yml -i inventory
```

4. Destroy after if needed (```web_app_full_wipe``` to ```true```)

```bash
ansible-playbook playbooks/dev/app_python/main.yml -i inventory --tags "wipe"
```