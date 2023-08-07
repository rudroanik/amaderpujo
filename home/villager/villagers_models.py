from _decimal import Decimal
from django.db import models


class VillagersModel(models.Model):
    villager_id = models.AutoField(primary_key=True)
    villager_name = models.CharField(blank=True, max_length=100)
    villager_mobile_number = models.CharField(blank=True, max_length=13)
    villager_chada = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal(0.00))
    villager_blood_group = models.CharField(blank=True, max_length=10)
    admin_id = models.IntegerField(blank=False, default=0)
