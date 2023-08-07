# Generated by Django 4.2.2 on 2023-08-07 06:54

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_villagersmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='VillagersCollectionModel',
            fields=[
                ('villager_collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('villager_name', models.CharField(blank=True, max_length=100)),
                ('year', models.CharField(blank=True, default='2023', max_length=10)),
                ('collected_amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('admin_id', models.IntegerField(blank=True, default=0)),
                ('collector_name', models.CharField(blank=True, max_length=100)),
                ('collection_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
