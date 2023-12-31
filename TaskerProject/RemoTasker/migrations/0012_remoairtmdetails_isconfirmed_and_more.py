# Generated by Django 5.0 on 2023-12-30 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoTasker', '0011_remoairtmdetails_tasker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='remoairtmdetails',
            name='isConfirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='availabletasks',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 11, 33, 35, 954196)),
        ),
    ]