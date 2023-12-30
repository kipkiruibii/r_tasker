# Generated by Django 5.0 on 2023-12-30 08:07

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RemoTasker', '0009_remove_taskinfo_how_to_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletasks',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 30, 11, 7, 55, 211495)),
        ),
        migrations.CreateModel(
            name='RemoAirtmDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='Username')),
                ('password', models.TextField(default='password')),
                ('country', models.TextField(default='country')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RemoTasker.availabletasks')),
            ],
        ),
    ]
