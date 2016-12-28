
import pytest

from django.urls import reverse

from tests.fixtures.apps_settings import frontoffice_app
from tests.fixtures.users import dude_user


def test_index_prevents_unauthenticated(frontoffice_app, client):
    r = client.get(reverse('frontoffice:index'))
    assert r.status_code == 403
    assert r.json() == {'detail': 'Authentication credentials were not provided.'}


@pytest.mark.django_db
def test_index_responds_authenticated(frontoffice_app, dude_user, client):
    client.login(email='dude@example.com', password='password')
    r = client.get(reverse('frontoffice:index'))
    assert r.status_code == 200
    assert r.json() == {'content': 'frontoffice_index'}
