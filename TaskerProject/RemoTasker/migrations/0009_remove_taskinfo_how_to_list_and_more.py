# Generated by Django 5.0 on 2023-12-30 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoTasker', '0008_remove_taskinfo_how_to_important_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskinfo',
            name='how_to_list',
        ),
        migrations.RemoveField(
            model_name='taskinfo',
            name='requirements_brief',
        ),
        migrations.AlterField(
            model_name='availabletasks',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 9, 36, 11, 459495)),
        ),
    ]
