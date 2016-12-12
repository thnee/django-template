
from django.conf.urls import url, include

from apps.backoffice.urls import backoffice_patterns
from apps.frontoffice.urls import frontoffice_patterns


urlpatterns = [
    url(r'', include(namespace='backoffice', arg=backoffice_patterns)),
    url(r'', include(namespace='frontoffice', arg=frontoffice_patterns)),
]
