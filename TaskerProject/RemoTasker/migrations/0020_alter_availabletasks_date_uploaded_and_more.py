# Generated by Django 5.0 on 2023-12-30 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoTasker', '0019_alter_availabletasks_date_uploaded_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletasks',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 18, 48, 23, 974491)),
        ),
        migrations.AlterField(
            model_name='usernotifications',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 18, 48, 23, 974491)),
        ),
        migrations.AlterField(
            model_name='withdrawalrequests',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 18, 48, 23, 974491)),
        ),
    ]
