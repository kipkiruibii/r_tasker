# Generated by Django 5.0 on 2023-12-30 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoTasker', '0018_alter_availabletasks_date_uploaded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletasks',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 15, 54, 13, 721762)),
        ),
        migrations.AlterField(
            model_name='usernotifications',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 15, 54, 13, 723765)),
        ),
        migrations.AlterField(
            model_name='withdrawalrequests',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 15, 54, 13, 723765)),
        ),
    ]