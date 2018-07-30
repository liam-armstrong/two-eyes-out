from . import models, serializer
from rest_framework import viewsets

class SectionViewSet(viewsets.ModelViewSet):
    queryset = models.section.objects.all()
    serializer_class = serializer.sectionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.customUser.objects.all()
    serializer_class = serializer.userSerializer
