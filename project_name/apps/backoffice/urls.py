
from django.conf.urls import url, include

from .views import test


backoffice_patterns = [
    url(r'^test/', test),
]


urlpatterns = [
    url(r'', include(namespace='backoffice', arg=backoffice_patterns))
]
