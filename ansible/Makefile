install:
	ansible-galaxy role install geerlingguy.docker
start:
	ansible-playbook playbooks/dev/main.yaml -i inventory/inventory.yaml
deployment:
	ansible-playbook playbooks/dev/main.yaml -i inventory/inventory.yaml --diff
inventory:
	ansible-inventory -i inventory/inventory.yaml --list
