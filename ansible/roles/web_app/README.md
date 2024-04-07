# `web_app` Ansible Role

The `web_app` Ansible role is designed for deploying your application's Docker image. It follows best practices and integrates seamlessly with the existing `docker` role. Below, you'll find details on how to use and configure the `web_app` role.

## Requirements

Before using the `web_app` role, ensure the following prerequisites are met:

1. **Ansible Installed**:
   - Make sure Ansible is installed on your control machine.

2. **Docker Role Dependency**:
   - The `web_app` role depends on the `docker` role. Ensure that the `docker` role is included in your playbook.

## Usage

1. **Include the `web_app` Role**:
   - In your playbook (e.g., `main.yml`), include the `web_app` role alongside the `docker` role:

     ```yaml
     - name: Deploy Application
       hosts: my_servers
       gather_facts: yes

       roles:
         - docker
         - web_app
     ```

2. **Configure Variables**:
   - Define variables specific to your application in the `defaults/main.yml` file of the `web_app` role.
   - Example variables:

     ```yaml
     # defaults/main.yml
     ---
     web_app_image_name: "myapp:latest"
     web_app_port: 5000
     # Add other relevant variables
     ```

3. **Execute the Playbook**:
   - Run your playbook to deploy both the `docker` and `web_app` roles:

     ```
     ansible-playbook -i inventory.ini site.yml
     ```

4. **Optional: Wipe Logic**:
   - If needed, enable the wipe process by setting `web_app_full_wipe: true` in your inventory or extra variables.

## Wipe Logic (Optional)

The `web_app` role includes a wipe logic section. When enabled, it stops the Docker container and removes related files. To trigger the wipe process, use the `web_app_full_wipe` variable.

## Customization

Customize the `docker-compose.yml` template and other configurations in the `web_app` role according to your application's requirements.

Feel free to adapt this template to your specific use case. If you have any further questions or need additional assistance, feel free to ask! 🚀