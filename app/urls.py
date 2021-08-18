from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app.controllers import user



# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('users', user.eventList, name='users'),
    path('users/<str:id>/', user.show, name='detail'),
    path('users/<str:id>/deposit', user.deposit, name='deposit'),
    path('users/<str:id>/withdraw', user.withdraw, name='withdraw'),

]