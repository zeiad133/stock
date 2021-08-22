from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class UserStock(models.Model):
    user = models.ForeignKey('app.User', on_delete=models.CASCADE)
    stock_id = models.CharField(max_length=200)
    stock_name = models.CharField(max_length=200)
    total = models.IntegerField(default=0)
    stocks_on_hold = models.IntegerField(default=0, validators = [MinValueValidator(0)])

    def save(self, *args, **kwargs):
      if self.stocks_on_hold > self.total:
        raise ValidationError({'stocks_on_hold': "Stocks on hold should be less than current stocks"})
      self.full_clean()
      return super().save(*args, **kwargs)






