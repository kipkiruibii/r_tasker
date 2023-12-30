from django.db import models
from datetime import datetime


class UserProfile(models.Model):
    firstname = models.TextField(default='firstname')
    lastname = models.TextField(default='lastname')
    username = models.TextField(default='username')
    email = models.TextField(default='email')
    paypal_email = models.TextField(default='paypal_email')
    phone_number = models.TextField(default='phone number')
    country = models.TextField(default='country')
    dial_code = models.TextField(default='dial_code')
    balance = models.IntegerField(default=0)
    withdrawn = models.IntegerField(default=0)
    pending = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class AvailableTasks(models.Model):
    task_name = models.TextField(default='task name')
    date_uploaded = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.task_name


class TaskInfo(models.Model):
    task = models.ForeignKey(AvailableTasks, on_delete=models.CASCADE, null=True)
    task_description = models.TextField(default='description', null=True)
    requirements = models.TextField(default='description', null=True)
    how_to_title = models.TextField(default='how to title', null=True)
    how_to_submit = models.TextField(default='how to submit', null=True)
    how_to_info = models.TextField(default='how to info ', null=True)
    pay = models.TextField(default='how to info ', null=True)

    def __str__(self):
        return self.task.task_name


class UserQueries(models.Model):
    message = models.TextField(default='message')
    email = models.TextField(default='email')
    username = models.TextField(default='username')

    def __str__(self):
        return self.username


class RemoAirtmDetails(models.Model):
    task = models.ForeignKey(AvailableTasks, null=True, on_delete=models.CASCADE)
    username = models.TextField(default='Username')
    password = models.TextField(default='password')
    country = models.TextField(default='country')

    def __str__(self):
        return self.task.task_name
