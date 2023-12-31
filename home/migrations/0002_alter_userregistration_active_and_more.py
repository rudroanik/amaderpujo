# Generated by Django 4.2.2 on 2023-06-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='admin_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='mondir_name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='password',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
