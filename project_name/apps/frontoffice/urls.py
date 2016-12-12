
from django.conf.urls import url, include

from .views import test


frontoffice_patterns = [
    url(r'^test/', test),
]


urlpatterns = [
    url(r'', include(namespace='frontoffice', arg=frontoffice_patterns)),
]
