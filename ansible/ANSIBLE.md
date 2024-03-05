```ansible
PLAY [Install Docker] *********************************************************************************************************************
TASK [Gathering Facts] ***************************************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install pip] ********************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Add user to docker group] *************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Update packages] *********************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker] *******************************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
TASK [../../roles/docker : Install Docker Compose] ***********************************************************************************************************
ok: [ec2-3-124-209-126.eu-central-1.compute.amazonaws.com]
PLAY RECAP ***************************************************************************************************************************************************
ec2-3-124-209-126.eu-central-1.compute.amazonaws.com : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  
ansible-inventory -i ./ansible/inventory/default_aws_ec2.yml --list
```