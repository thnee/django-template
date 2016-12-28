
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class IndexView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response({'content': 'backoffice_index'})
