# Ansible
To setup ansible, I divided inventory, roles, and playbooks in different directories and configured their path in ansible.cfg file.

For the first task, I used [this role](https://github.com/geerlingguy/ansible-role-docker). You can see the commented part of the main playbook.

For the second task, I used [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04) as the reference. I didn't include docker compose, since it's already shipped with the newest version of docker.

Here are the logs of the `ansible-playbook playbooks/dev/main.yml --diff` command:

```

PLAY [task2] *******************************************************************

TASK [Gathering Facts] *********************************************************
ok: [10.225.203.190]

TASK [docker : include_tasks] **************************************************
included: /home/rinri/edu/S24-core-course-labs/ansible/roles/docker/tasks/install-docker.yml for 10.225.203.190

TASK [docker : Update apt] *****************************************************
changed: [10.225.203.190]

TASK [docker : install dependencies] *******************************************
The following NEW packages will be installed:
  apt-transport-https
0 upgraded, 1 newly installed, 0 to remove and 1 not upgraded.
changed: [10.225.203.190]

TASK [docker : add docker gpg keys] ********************************************
changed: [10.225.203.190]

TASK [docker : add docker apt repositories] ************************************
--- before: /dev/null
+++ after: /etc/apt/sources.list.d/download_docker_com_linux_ubuntu.list
@@ -0,0 +1 @@
+deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu jammy stable

changed: [10.225.203.190]

TASK [docker : Update apt after adding docker repos] ***************************
changed: [10.225.203.190]

TASK [docker : install docker] *************************************************
The following additional packages will be installed:
  containerd.io docker-buildx-plugin docker-ce-cli docker-ce-rootless-extras
  docker-compose-plugin libltdl7 libslirp0 pigz slirp4netns
Suggested packages:
  aufs-tools cgroupfs-mount | cgroup-lite
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli
  docker-ce-rootless-extras docker-compose-plugin libltdl7 libslirp0 pigz
  slirp4netns
0 upgraded, 10 newly installed, 0 to remove and 1 not upgraded.
changed: [10.225.203.190]

TASK [docker : enable docker] **************************************************
ok: [10.225.203.190]

PLAY RECAP *********************************************************************
10.225.203.190             : ok=9    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
