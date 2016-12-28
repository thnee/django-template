
import pytest

from libs.core.factories.users.admin import AdminUserFactory
from libs.core.factories.users.dude import DudeUserFactory


@pytest.fixture
def admin_user():
    return AdminUserFactory(
        email='admin@example.com',
        password='password',
    )


@pytest.fixture
def dude_user():
    return DudeUserFactory(
        email='dude@example.com',
        password='password',
    )
