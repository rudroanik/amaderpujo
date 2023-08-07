import datetime

from _decimal import Decimal
from django.db import models


class VillagersCollectionModel(models.Model):
    villager_collection_id = models.AutoField(primary_key=True)
    villager_name = models.CharField(blank=True,max_length=100)
    year = models.CharField(blank=True, default=str(datetime.datetime.now().year),max_length=10)
    collected_amount = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    admin_id = models.IntegerField(blank=True, default=0)
    collector_name = models.CharField(blank=True,max_length=100)
    collection_time = models.DateTimeField(auto_now=True)
