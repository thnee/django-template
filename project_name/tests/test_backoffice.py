
from tests.fixtures.apps_settings import backoffice_app


def test_test_view(backoffice_app, client):
    r = client.get('/test/')
    assert r.status_code == 200
    assert r.content == b'backoffice test'
