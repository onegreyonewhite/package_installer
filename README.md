package_installer
=========

This Ansible role for manage system packages.

Requirements
------------

Nothing.

Role Variables
--------------

See default variables: `defaults/main.yml`

## Dependencies

Install dependencies using Ansible galaxy

`ansible-galaxy install -r roles/requirements.yml`


Example Playbook
----------------

        - hosts: servers
          roles:
             - { role: onegreyonewhite.package_installer }

License
-------

BSD

Author Information
------------------

[Sergey Klyuykov](https://github.com/onegreyonewhite)