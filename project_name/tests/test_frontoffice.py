
from tests.fixtures.apps_settings import frontoffice_app


def test_test_view(frontoffice_app, client):
    r = client.get('/test/')
    assert r.status_code == 200
    assert r.content == b'frontoffice test'
