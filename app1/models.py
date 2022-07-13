from decimal import Decimal
import email
from itertools import groupby
from locale import currency
from optparse import make_option

from unicodedata import decimal
from django.db import models

# Create your models here.

class Stock_Groups(models.Model):
    Group_name = models.CharField(max_length=225)
    Group_total =models.IntegerField(default=0)

class Stock_Group_items(models.Model):
    Group = models.ForeignKey(Stock_Groups, on_delete=models.CASCADE, null=True)
    Item_name =models.CharField(max_length=225)
    Quantity =models.IntegerField()
    Rate =models.IntegerField()
    Value =models.IntegerField()


