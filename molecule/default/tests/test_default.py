import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_traceroute_installed(host):
    assert host.package('traceroute').is_installed
    # assert host.file('/usr/bin/traceroute').exists


def test_update_system(host):
    if host.system_info.distribution.lower() in ['ubuntu', 'debian']:
        assert not host.ansible(
            "apt", "update_cache=yes upgrade=dist"
            )["changed"]
    elif host.system_info.distribution.lower() == 'centos':
        module_name = 'dnf' if host.system_info.release >= '8' else 'yum'
        assert not host.ansible(
                module_name, "name='*' state=latest"
        )["changed"]
    else:
        raise AssertionError(
            'Unknown distribution: {}.'.format(
                host.system_info.distribution
            )
        )
