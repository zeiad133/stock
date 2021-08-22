from django.contrib import admin
from django.urls import include, path
import  app.services.vernemq 
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    path('api/', include('app.urls'))
]