from django.shortcuts import render
from django.http import HttpResponse
from . import models, serializer
from rest_framework import viewsets

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class SectionViewSet(viewsets.ModelViewSet):
    queryset = models.section.objects.all()
    serializer_class = serializer.sectionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.customUser.objects.all()
    serializer_class = serializer.userSerializer
