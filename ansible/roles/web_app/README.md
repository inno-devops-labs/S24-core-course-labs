# Python Web App Role

This Ansible role that runs python web app on a remote server

## Requirements

- Ansible 2.16 or later
- Target hosts running Ubuntu

## Usage

Here is an example of playbook contents:

```yaml
- name: Deploy Python App Docker Image
  hosts: all
  become: true
  roles:
     - name: "Deploy"
       role: web_app
       web_app_full_wipe: false
       tags: [deploy]

     - name: "Wipe"
       role: web_app
       web_app_full_wipe: true
       tags: [never, wipe]
```


