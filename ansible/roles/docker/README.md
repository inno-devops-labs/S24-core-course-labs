
# Docker and docker-compose role

- It solve 2 tasks: Installing docker and Installing docker compose on the target machine.
- It meets all requirements from official documentation.

## Usage
    ```sh
    ---
    - name: Deploy Docker
    hosts: aws_ec2
    become: true
    roles:
        - role: ../../roles/docker
    ```