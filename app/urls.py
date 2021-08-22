from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from app.controllers import users, orders, stocks



# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('users', users.eventList, name='users'),
    path('users/<str:id>/', users.show, name='detail'),
    path('users/<str:id>/deposit', users.deposit, name='deposit'),
    path('users/<str:id>/withdraw', users.withdraw, name='withdraw'),
    path('<str:id>/buy/<str:stock_id>', orders.buy, name='buy'),
    path('<str:id>/sell/<str:stock_id>', orders.sell, name='sell'),
    path('stocks/<str:id>/', stocks.show, name='detail'),


]