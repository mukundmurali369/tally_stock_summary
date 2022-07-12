from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.

class Stock_Group(models.Model):
    Group_name = models.CharField(max_length=225)

class Stock_Group_items(models.Model):
    Group = models.ForeignKey(Stock_Group, on_delete=models.CASCADE, null=True)
    Item_name =models.CharField(max_length=225)
    Quantity =models.IntegerField()
    Rate =models.IntegerField()
    Value =models.IntegerField()
