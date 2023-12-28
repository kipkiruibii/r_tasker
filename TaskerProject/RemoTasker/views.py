from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'signup.html')


def contact(request):
    return render(request, 'contact.html')


def aboutTask(request):
    return render(request, 'task_description.html')


def availableTasks(request):
    return render(request, 'tasks.html')


def account(request):
    return render(request, 'account.html')
