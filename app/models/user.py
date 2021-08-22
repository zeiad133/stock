from django.db import models
from django.core.validators import MinValueValidator
from .user_stock import UserStock

from django.core.exceptions import ValidationError

class User(models.Model):
    wallet = models.IntegerField(validators = [MinValueValidator(0)])
    name = models.CharField(max_length=200) 
    money_on_hold = models.IntegerField(default=0, validators = [MinValueValidator(0)])
    stocks = models.ManyToManyField(UserStock, related_name='+')
    def save(self, *args, **kwargs):
      if self.money_on_hold > self.wallet:
        raise ValidationError({'on_hold_money': "Money on hold should be less than wallet"})
      self.full_clean()
      return super().save(*args, **kwargs)








