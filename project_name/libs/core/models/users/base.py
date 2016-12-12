
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as __


class BaseUser(AbstractBaseUser):
    class Meta:
        abstract = True

    USERNAME_FIELD = 'email'

    created_at = models.DateTimeField(__('created at'), default=timezone.now)
    updated_at = models.DateTimeField(__('updated at'), default=timezone.now)

    email = models.EmailField(
        max_length=1000,
        unique=True,
    )
