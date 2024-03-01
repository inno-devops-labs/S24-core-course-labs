# Custom Docker Role
## Description:
The Custom Docker Role is an Ansible role designed to install Docker and Docker Compose on target hosts. It provides a reusable and customizable solution for managing Docker environments across multiple hosts.

## Requirements:
Ansible installed on the control node.
Target hosts running compatible Linux distributions (e.g., Ubuntu).

### Usage:
1. **Test that you can remotely connect to vm using** `ssh "private key path" "username"@"ip"`
2. **Clone the Ansible project repository**:
   ```bash
   git clone <ansible_project_repo_url>
3. **Define hosts in Inventory file**
4. **execute playbook using** `ansible-playbook playbooks/dev/main.yaml`
5. **check that VM acquired docker, pip and docker-compose**
