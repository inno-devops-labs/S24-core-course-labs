# Web App Deploy

This `web_app` role manages deployment and cleanup (wipe) for a Dockerized web application using Docker or Docker Compose. Key features include organizing tasks with blocks, implementing selective tags, and providing role dependencies to manage requirements.

## Key Points

### 1. **Group Tasks with Blocks**

Tasks in this role are organized into blocks to group related operations, such as deploying and wiping the application. This makes the playbook more modular and easier to manage.

### 2. **Role Dependency**

The `web_app` role depends on the `docker` role. This ensures Docker is installed and properly configured before deploying the application.

### 3. **Apply Tags for Task Organization**

Tags are used to logically group tasks and enable selective execution. Key tags include:
- `deploy`: Deploys the Docker container or Docker Compose project.
- `wipe`: Removes the Docker container, image, and any related files.

### 4. **Wipe Logic**

A separate `wipe.yml` file contains the logic to fully clean up the application:
- Stops and removes the Docker container.
- Deletes the Docker image.
- Removes all associated files and directories.
This process can be controlled using the `web_app_full_wipe` variable.

### 5. **Separate Tag for Wipe**

The `wipe` tag allows you to execute only the cleanup tasks independently from the main deployment.

### 6. **Docker Compose File**

A `docker-compose.yml` template is provided to define the application's Docker services.

### 7. **Template Delivery with Ansible**

The `template` module is used to deliver the `docker-compose.yml` file to the target server, allowing you to update configuration dynamically.

## Usage Example
Deploy the application:
```bash
ansible-playbook -i inventory/vm.yml playbooks/dev/main.yml --tags "deploy"
```
Wipe the application (if web_app_full_wipe is true it will happen without explicitly specifying):
```bash
ansible-playbook -i inventory/vm.yml playbooks/dev/main.yml --tags "wipe" -e "web_ap
```