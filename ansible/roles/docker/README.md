# Ansible

## Task 1: Initial Setup

1. I installed Ansible and geerlingguy docker role with:

   ```bash
   sudo apt update
   sudo apt install software-properties-common
   sudo add-apt-repository --yes --update ppa:ansible/ansible
   sudo apt install ansible
   ansible-galaxy install geerlingguy.docker
   ```

2. I developed playbook for deploying Docker in playbooks/dev/main.yaml:

   ```yaml
   - name: Install Docker
     hosts: localhost
     become: true
     roles:
       - docker
   ```

## Task 2: Custom Docker Role

1. I created my custom Docker role following the recommended structure.

2. I developed a custom Ansible role for Docker with the following tasks:

   - Install Docker
   - Install Docker Compose

3. Docker role, its requirements and usage:

   - Name: docker
   - Requirements: geerlingguy.docker
   - Usage: ansible-playbook playbooks/dev/main.yaml --diff
   - Workflow:
     - Install Docker:
       - Add user to docker group
       - Install pip
       - Install system packages
       - Add Docker GPG Key
       - Add Docker repository
       - Update apt cache and install docker-ce
     - Install Docker Compose
       - Install Docker Compose using pip

4. Output lines of commands are in separate file ANSIBLE.md
