import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_is_installed(host):
    pkg = host.package("git")
    assert pkg.is_installed


def test_homeshick_file(host):
    file = host.file("/root/.homesick/repos/homeshick/bin/homeshick")
    assert file.exists
