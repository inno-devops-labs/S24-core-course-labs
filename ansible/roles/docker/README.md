
# Docker and docker-compose role

The tasks:
- Install docker
- Install docker compose
- Meets all official documentation's requirements 

## How to use
    ```sh
    ---
    - name: Deploy Docker
    hosts: all
    become: true
    roles:
        - role: ../../roles/docker
    ```