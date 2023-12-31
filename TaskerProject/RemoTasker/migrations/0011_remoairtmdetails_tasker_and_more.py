# Generated by Django 5.0 on 2023-12-30 08:32

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoTasker', '0010_alter_availabletasks_date_uploaded_remoairtmdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='remoairtmdetails',
            name='tasker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RemoTasker.userprofile'),
        ),
        migrations.AlterField(
            model_name='availabletasks',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 11, 32, 8, 395125)),
        ),
    ]
