
# Task 1 - setup

I've successfully set up ansible and used provided docker role.

# Task 2 - custom role

Since we have already implemented role for docker it is quite cheaty to do the same but simplified in my opition.
So, I've mimic production like workflow, adding docker compose template file with simple web server on it (use caddy). Actually, think that caddy may replace nginx in my own setup, sounds like really pleasure to use server.


# Task 3 - dynamic inventory

Since I've chosen "hard way" with self hosting and I always wanna try something new, I've utilized Vagrant to provide me virtual machine for ansible tests.
Spend two days to overcome macos arm compatibility and finaly got solution.
Actually, quite cool setup for testing. And working offline!

One moment that I didn't got finally is how to pass `vagrant ssh-config` machine address to ansible automatically and not to use ansible provisioning for it. So, as temporal solution past it with shell script. But would be glad for any comment

Refer to `../vagrant`

## Development output

Provide links to files to keep report organized

[ansible-playbook playbooks/dev/main.yml --diff](./attachments/ansible-playbook-diff)
[ansible-inventory --list](./attachments/ansible-inventory-list)