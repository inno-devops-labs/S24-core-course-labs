# Web_app

## Requirements:
Role: `docker`
The `docker` role is responsible for ensuring that Docker is installed on the target system.

Tasks:
1. Get Image and Run Container (tag: `run`)
- Retrieve Docker image specified by the `username` and `image` variables.
- Launch a container using the specified image (defined by variables `username`/`imagee` and `name` for the container).

2. Deliver Docker Compose (tag: `compose`)
- Create a directory at `/tmp/compose/`.
- Copy the Docker Compose configuration file (`docker-compose.yml.j2`) to `/tmp/compose/{{ name }}.docker-compose.yml`.

3. Wipe Image and Container (tag: `wipe`)
- Remove the container (using the same variables as for the Run docker container task).
- Remove the Docker image.

## Playbook

```yaml
---
- name: Deploy Docker on Yandex Cloud
  hosts: all
  become: true

  roles:
    - role: ../../../roles/web_app

```

Optionally, the values of variables can be specified explicitly in playbook

```
name: "app"

web_app_full_wipe: true

username: "mierley4041"
image: "devops-flask:latest"
ports: "80:5000"
```

Output 
```
PLAY [Deploy Docker on Yandex Cloud] ***********************************************************************************************

TASK [Gathering Facts] *************************************************************************************************************
ok: [51.250.77.205]

TASK [docker : include_tasks] ******************************************************************************************************
included: /mnt/c/MINE/Programming/Devops/S24-core-course-labs/ansible/roles/docker/tasks/setup_repo.yml for 51.250.77.205

TASK [docker : Install Dependencies] ***********************************************************************************************
ok: [51.250.77.205]

TASK [docker : Setup keyrings folder] **********************************************************************************************
changed: [51.250.77.205]

TASK [docker : Add Docker apt key] *************************************************************************************************
ok: [51.250.77.205]

TASK [docker : Add Docker repository] **********************************************************************************************
ok: [51.250.77.205]

TASK [docker : Disable Unattended Upgrades] ****************************************************************************************
ok: [51.250.77.205]

TASK [docker : Install dependencies] ***********************************************************************************************
ok: [51.250.77.205]

TASK [docker : include_tasks] ******************************************************************************************************
included: /mnt/c/MINE/Programming/Devops/S24-core-course-labs/ansible/roles/docker/tasks/install_docker.yml for 51.250.77.205

TASK [docker : Install Docker] *****************************************************************************************************
ok: [51.250.77.205]

TASK [docker : include_tasks] ******************************************************************************************************
included: /mnt/c/MINE/Programming/Devops/S24-core-course-labs/ansible/roles/docker/tasks/install_compose.yml for 51.250.77.205

TASK [docker : Install Docker Compose with pip] ************************************************************************************
ok: [51.250.77.205]

TASK [../../../roles/web_app : Get docker image] ***********************************************************************************
ok: [51.250.77.205]

TASK [../../../roles/web_app : Run docker container] *******************************************************************************
changed: [51.250.77.205]

TASK [../../../roles/web_app : Deliver docker compose] *****************************************************************************
included: /mnt/c/MINE/Programming/Devops/S24-core-course-labs/ansible/roles/web_app/tasks/docker-compose.yml for 51.250.77.205

TASK [../../../roles/web_app : Create directory] ***********************************************************************************
ok: [51.250.77.205]

TASK [../../../roles/web_app : Deliver compose] ************************************************************************************
ok: [51.250.77.205]

TASK [../../../roles/web_app : Wipe docker image and container] ********************************************************************
included: /mnt/c/MINE/Programming/Devops/S24-core-course-labs/ansible/roles/web_app/tasks/wipe.yml for 51.250.77.205

TASK [../../../roles/web_app : Remove container] ***********************************************************************************
changed: [51.250.77.205]

TASK [../../../roles/web_app : Remove image] ***************************************************************************************
ok: [51.250.77.205]

PLAY RECAP *************************************************************************************************************************
51.250.77.205              : ok=20   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```