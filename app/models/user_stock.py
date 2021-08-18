from django.db import models
from .user_stock import UserStock

class UserStocks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id = models.CharField(max_length=200)
    stock_name = models.CharField(max_length=200)
    total = models.IntegerField(default=1)





