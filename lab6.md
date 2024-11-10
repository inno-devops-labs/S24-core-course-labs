# Lab 6: Ansible and Application Deployment

## Overview

In this lab, you will utilize Ansible to set up a Continuous Deployment (CD) process for your application.

## Task 1: Application Deployment

**6 Points:**

1. Create an Ansible Role:
   - Develop an Ansible role specifically for deploying your application's Docker image. Call it `web_app`

2. Update the Playbook:
   - Modify your Ansible playbook to integrate the new role you've created for Docker image deployment.

3. Deployment Output:
   - Execute your playbook to deploy the role.
   - Provide the last 50 lines of the output from your deployment command in the `ANSIBLE.md` file.

## Task 2: Ansible Best Practices

**4 Points:**

1. Group Tasks with Blocks:
   - Organize related tasks within your playbooks using Ansible blocks.

2. Role Dependency:
   - Set the role dependency for your `web_app` role to include the `docker` role.

3. Apply Tags:
   - Implement Ansible tags to group tasks logically and enable selective execution.

4. Wipe Logic:
   - Create a YAML file with a **Wipe** logic for your application. This should include removing your Docker container and all related files.
   - Ensure that this wipe process can be enabled or disabled by using a variable, for example, `web_app_full_wipe=true`.

5. Separate Tag for Wipe:
   - Utilize a distinct tag for the **Wipe** section of your Ansible playbook. This allows you to run the wipe tasks independently from the main tasks.

6. Docker Compose File:
   - Create a `docker-compose.yml` file for your application.

7. Template Delivery:
   - Employ the `template` module to deliver your `docker-compose.yml` file to the target server.

   Suggested structure:

   ```sh
   .
   |-- defaults
   |   `-- main.yml
   |-- meta
   |   `-- main.yml
   |-- tasks
   |   |-- 0-wipe.yml
   |   `-- main.yml
   `-- templates
      `-- docker-compose.yml.j2
   ```

8. Create `README.md`:
   - Create a `README.md` file in the `ansible/roles/web_app` folder.
   - Use a Markdown template to describe your role, its requirements and usage.

## Bonus Task: CD Improvement

**2.5 Points:**

1. Create an Extra Playbook:
   - Develop an additional Ansible playbook specifically for your bonus application.
   - You can reuse the existing Ansible role you created for your primary application or create a new one.
   - Suggested structure:

   ```sh
   .
   `--ansible
       `-- playbooks
           `-- dev
               |-- app_python
               |   `-- main.yaml
               `-- app_go
                   `-- main.yaml
   ```

### Guidelines

- Use proper Markdown formatting and structure for documentation files.
- Organize files within the lab folder with suitable naming conventions.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.
- Follow the suggested structure for your Ansible roles, tasks, and templates.
- Utilize Ansible best practices such as grouping tasks with blocks, applying tags, and separating roles logically.

> Note: Apply diligence to your Ansible implementation, follow best practices, and clearly document your work to achieve the best results in this lab assignment.
