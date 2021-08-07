from django.db import models

class User(models.Model):
    wallet = models.FloatField()
    name = models.CharField(max_length=200)
    def stocks(self):
      return UserStocks.objects.filter(user_id=self.id)
    def __str__(self):
      return self.name
class UserStocks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_id = models.CharField(max_length=200)
    stock_name = models.CharField(max_length=200)
    total = models.IntegerField(default=1)





