Role Name
=========

It is auto generated file after ```ansible-galaxy init roles/docker``` commandю This role is used for Docker. Therefore, there is some additional folder in docker and web_app directories, that might be useful for further labs.

Requirements
------------

The host should have Ubuntu machine, therefore, I configured my AWS as Ubuntu. Also, ```apt``` should be installed on the VM.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

``` 
- name: Setup docker
  hosts: all
  become: yes
  roles:
    - ../../roles/docker
```

License
-------

MIT

Author Information
------------------

Alexandra Chupkova, SD-01
