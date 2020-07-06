"""two-eyes-out api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import re_path, include
from core import views

section_list = views.SectionsViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'delete': 'remove',
    'patch': 'flipActivation'
})

user_functions = views.UserViewSet.as_view({
    'post': 'create',
})

urlpatterns = [
    re_path(r'api-token-auth', obtain_jwt_token),
    re_path(r'sections', section_list),
    re_path(r'users', user_functions),
]