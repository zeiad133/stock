from django.db import models
from django.core.validators import MinValueValidator

class User(models.Model):
    wallet = models.IntegerField(validators = [MinValueValidator(0)])
    name = models.CharField(max_length=200)








