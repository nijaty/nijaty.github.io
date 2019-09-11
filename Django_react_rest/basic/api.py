from basic.models import Basic
from rest_framework import viewsets, permissions
from .serializers import BasicSerializer


# Basic Viewset
class BasicViewSet(viewsets.ModelViewSet):
    queryset = Basic.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BasicSerializer
