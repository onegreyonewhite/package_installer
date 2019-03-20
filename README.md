package_installer
=========

This Ansible role for manage system packages. 
Just update and install functions.

Requirements
------------

Nothing.

Role Variables
--------------

See default variables: `defaults/main.yml`

```yaml
update_packages: no
```
Don't update system packages before any operations.

```yaml
enable_epel_release: no
``` 
Don't install epel-release in RHEL OS for extra-packages.
If you want to install mc or htop you should set `yes`.

```yaml
system_packages: []
```
By default role doesn't install anything, but if you set:
```yaml
system_packages:
    - traceroute
    - wget
    - nano
```
ansible will always install and update `traceroute`,
`wget` and `nano` packages.

## Dependencies

Install dependencies using Ansible galaxy

`ansible-galaxy install -r roles/requirements.yml`

You shouldn't do this if you install role from galaxy.

Example Playbook
----------------

        - hosts: servers
          vars:
            update_packages: yes
            system_packages:
                - wget
                - traceroute
                - nano
          roles:
             - { role: onegreyonewhite.package_installer }

License
-------

BSD

Author Information
------------------

[Sergey Klyuykov](https://github.com/onegreyonewhite)