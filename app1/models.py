import datetime
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

class Add_items(models.Model):
    Group = models.ForeignKey(Stock_Groups, on_delete=models.CASCADE, null=True)
    Item_name =models.CharField(max_length=225)
    Item_unit=models.CharField(max_length=225)

class Buy_items(models.Model):
    Item_name =  models.ForeignKey(Add_items, on_delete=models.CASCADE, null=True)
    Group = models.ForeignKey(Stock_Groups, on_delete=models.CASCADE, null=True)
    Quantity =models.IntegerField(default=10)
    company = models.CharField(max_length=225)
    Rate =models.IntegerField()
    Value =models.IntegerField()
    date = models.DateField(("Date"), default=datetime.date.today)
    month=models.CharField(max_length=225,default="July")

class Sell_items(models.Model):
    Item_name =  models.ForeignKey(Add_items, on_delete=models.CASCADE, null=True)
    Group = models.ForeignKey(Stock_Groups, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=225)
    Rate =models.IntegerField()
    Value =models.IntegerField()
    date = models.DateField(("Date"), default=datetime.date.today)
    month=models.CharField(max_length=225,default="July")


class Buy_or_sell_items(models.Model):
    Item_name =  models.ForeignKey(Add_items, on_delete=models.CASCADE, null=True)
    Group = models.ForeignKey(Stock_Groups, on_delete=models.CASCADE, null=True)
    BorS =models.IntegerField(default=1)
    Quantity =models.IntegerField(default=10)
    company = models.CharField(max_length=225)
    Rate =models.IntegerField()
    Value =models.IntegerField()
    date = models.DateField(("Date"), default=datetime.date.today)
    month=models.CharField(max_length=225,default="July")
