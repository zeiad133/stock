from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from enum import Enum


class OrderType(Enum):
    SELL = "SELL"
    BUY = "BUY"

    

class Order(models.Model):
    SELL = 'sell'
    BUY = 'buy'
    ORDERTYPES = (
        (SELL, 'Sell'),
        (BUY, 'Buy'),
    )
    user = models.ForeignKey('app.User', on_delete=models.CASCADE)
    stock_id = models.CharField(max_length=200)
    upper_bound = models.IntegerField(validators = [MinValueValidator(1)])
    lower_bound = models.IntegerField(validators = [MinValueValidator(0)])
    total = models.IntegerField(validators = [MinValueValidator(1)])
    order_type = models.CharField(default="SELL", max_length=200, choices=ORDERTYPES)

    def save(self, *args, **kwargs):
      if self.lower_bound > self.upper_bound:
        raise ValidationError({'lower_bound': "Lower bound be less than current stocks"})
      self.full_clean()
      return super().save(*args, **kwargs)







