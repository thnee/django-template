
import pytest

from django.urls import reverse

from tests.fixtures.apps_settings import backoffice_app
from tests.fixtures.users import admin_user


def test_index_prevents_unauthenticated(backoffice_app, client):
    r = client.get(reverse('backoffice:index'))
    assert r.status_code == 403
    assert r.json() == {'detail': 'Authentication credentials were not provided.'}


@pytest.mark.django_db
def test_index_responds_authenticated(backoffice_app, admin_user, client):
    client.login(email='admin@example.com', password='password')
    r = client.get(reverse('backoffice:index'))
    assert r.status_code == 200
    assert r.json() == {'content': 'backoffice_index'}
