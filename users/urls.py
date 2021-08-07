from django.urls import path
from . import users
from . import orders
from . import stocks


urlpatterns = [
    path('user', users.userView, name='index'),
    path('stock', stocks.stockView, name='index'),
    path('deposit', users.deposit, name='index'),
    path('withdraw', users.withdraw, name='index'),
    path('buy', orders.buy, name='index'),
    path('sell', orders.sell, name='index'),

]