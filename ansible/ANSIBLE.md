# Ansible

---

## Docker Role

- To install `docker` I used `ansible.builtin.apt`
- To install `pip` I used `command` to execute `ansible.builtin.apt`
- To install `docker-compose` I imported `pip` and `docker` installation roles
- In `main.yaml` of my custom docker role I just imported all installation roles

## Playbook

- Importing role by passing relative path of the role
(with respect to `main.yml` of playbook)
- I used localhost as a host to test ansible locally
- Tasks for playbook are just pulling docker image and starting docker container

## Inventory

I didn't do anything with `ansible-inventory`
