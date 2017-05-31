
def test_apache2_webserver_is_installed(host):
    assert host.package('apache2').is_installed
