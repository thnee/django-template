
from django.conf.urls import url, include

from .views import IndexView


frontoffice_patterns = [
    url(r'^index/', IndexView.as_view(), name='index'),
]


urlpatterns = [
    url(r'', include(namespace='frontoffice', arg=frontoffice_patterns)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
