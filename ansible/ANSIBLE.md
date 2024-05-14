### Docker installation
Firstly I rewrite file for docker installation and reinstall docker with dependencies using following command ```ansible-playbook playbooks/dev/docker.yml --diff```. This command gives me output: 
```
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible
engine, or trying out features under development. This is a rapidly changing source of code and can become unstable at any point.

PLAY [Installation] ***********************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************
[WARNING]: Platform linux on host yandex_cloud is using the discovered Python interpreter at /usr/bin/python3.10, but future installation
of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/devel/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_cloud]

TASK [docker : Update apt] ****************************************************************************************************************
changed: [yandex_cloud]

TASK [docker : Python3 and pip3 installation] *********************************************************************************************
ok: [yandex_cloud]

TASK [docker : Install Docker dependencies] ***********************************************************************************************
ok: [yandex_cloud]

TASK [docker : Add Docker GPG key] ********************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Add Docker repository] *****************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Install Docker] ************************************************************************************************************
ok: [yandex_cloud]

TASK [docker : Install compose] ***********************************************************************************************************
ok: [yandex_cloud]

PLAY RECAP ********************************************************************************************************************************
yandex_cloud               : ok=8    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

### App Deployment 
finally, to make deploy I used the following command ```ansible-playbook playbooks/dev/web_app/deploy_app.yml --tags "deploy" --diff``` which gives me following output:
``` 
[WARNING]: You are running the development version of Ansible. You should only run Ansible from "devel" if you are modifying the Ansible
engine, or trying out features under development. This is a rapidly changing source of code and can become unstable at any point.

PLAY [Deploy app] *************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************
[WARNING]: Platform linux on host yandex_cloud is using the discovered Python interpreter at /usr/bin/python3.10, but future installation
of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-
core/devel/reference_appendices/interpreter_discovery.html for more information.
ok: [yandex_cloud]

TASK [web_app : create new directory] *****************************************************************************************************
ok: [yandex_cloud]

TASK [web_app : Start docker] *************************************************************************************************************
ok: [yandex_cloud]

TASK [web_app : Pull docker image] ********************************************************************************************************
ok: [yandex_cloud]

TASK [web_app : Copy docker compose file] *************************************************************************************************
ok: [yandex_cloud]

TASK [web_app : Run docker container] *****************************************************************************************************
changed: [yandex_cloud]

PLAY RECAP ********************************************************************************************************************************
yandex_cloud               : ok=6    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```

### So, now the python app are available on http://51.250.87.75:5000/ (as long as VM is up...)