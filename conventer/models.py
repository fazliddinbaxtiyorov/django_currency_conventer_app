from django.db import models


# Create your models here.

class Currency(models.Model):
    base_currency = models.CharField(max_length=5)
    target_currency = models.CharField(max_length=5)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    convert_amount = models.DecimalField(max_digits=10, decimal_places=2)