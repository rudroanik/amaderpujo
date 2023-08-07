from django.db import models


# Create your models here.
class UserRegistration(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=12)
    mondir_name = models.CharField(max_length=12)
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=100)
    admin_id = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now=True)
