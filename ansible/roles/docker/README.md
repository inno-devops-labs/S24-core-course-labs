# Docker

### Requirements: 
- For master node: 
    - Ansible latest
- For hosts: 
    - Ubuntu OS
    - pip3 installed
    - package manager e.g (`apt`)

### How to use
```yaml
- hosts: all
	- roles:
	    - role: docker
	      become: true 
```