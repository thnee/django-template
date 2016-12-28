
from django.conf.urls import url, include

from .views import IndexView


backoffice_patterns = [
    url(r'^index/', IndexView.as_view(), name='index'),
]


urlpatterns = [
    url(r'', include(namespace='backoffice', arg=backoffice_patterns)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
