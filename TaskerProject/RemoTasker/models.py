from django.db import models
from datetime import datetime


class UserProfile(models.Model):
    firstname = models.TextField(default='firstname')
    lastname = models.TextField(default='lastname')
    username = models.TextField(default='username')
    email = models.TextField(default='email')
    paypalEmail = models.TextField(default='paypal_email')
    phoneNumber = models.TextField(default='phone number')
    country = models.TextField(default='country')
    dialCode = models.TextField(default='dial_code')
    balanceHold = models.IntegerField(default=0)
    balanceActual = models.IntegerField(default=0)
    withdrawSuccess = models.IntegerField(default=0)
    withdrawPending = models.IntegerField(default=0)

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
    tasker = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    username = models.TextField(default='Username')
    earnings = models.IntegerField(default=0)
    password = models.TextField(default='password')
    country = models.TextField(default='country')
    isConfirmed = models.BooleanField(default=False)
    dateSubmitted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.task.task_name} | {self.tasker.username} | {self.isConfirmed}'


class UserNotifications(models.Model):
    user = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    message = models.TextField(default='message')
    date = models.DateTimeField(default=datetime.now())
    isRead = models.BooleanField(default=False)
    timesViewed = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class WithdrawalRequests(models.Model):
    user = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    isApproved = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.user.username} || {self.amount} '


class UserSubmittedTasks(models.Model):
    user = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    taskName = models.TextField(default='text')
    username = models.TextField(default='Username')
    password = models.TextField(default='password')
    comment = models.TextField(default='comment')
    amount = models.IntegerField(default=0)
    isPending = models.BooleanField(default=False)
    isConfirmed = models.BooleanField(default=False)
    isRejected = models.BooleanField(default=False)
    dateSubmitted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.user.username} || {self.taskName}'
