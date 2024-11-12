## Prerequisites
- Ansible installed
- Server instance configured for Ansible access

## Installation
1. Clone the repository.
2. Install Ansible by following the [installation guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html).
3. Update your `inventory/default_aws_ec2.yml` file with your EC2 instance details.
4. Run the Ansible playbook:

   ```bash
   ansible-playbook -i ansible/inventory/default_aws_ec2.yml ansible/playbooks/dev/main.yaml
