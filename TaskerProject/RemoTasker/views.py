from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *


def home(request):
    return render(request, 'home.html')


def loginV(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname', '')
        lastname = request.POST.get('lname', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        paypal_email = request.POST.get('p_email', '')
        phone_number = request.POST.get('phone_number', '')
        country = request.POST.get('country', '')
        dial_code = request.POST.get('dial_code', '')
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, 'Username or email already taken')
        else:
            up = UserProfile(
                firstname=firstname,
                lastname=lastname,
                username=username,
                email=email,
                paypal_email=paypal_email,
                phone_number=phone_number,
                country=country,
                dial_code=dial_code,

            )
            User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            up.save()
            print(username, password, email, paypal_email, phone_number, country, dial_code)
            return redirect('login')

    return render(request, 'signup.html')


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        if email and message:
            messages.success(request,
                             'Thank you for your feedback. Your message has been'
                             ' received.Check your email inbox for our reply')

            username = 'anonymous'
            if request.user.is_authenticated:
                username = request.user.username

            uq = UserQueries(
                message=message,
                email=email,
                username=username,
            )
            uq.save()

    return render(request, 'contact.html')


@login_required(login_url='/login/')
def aboutTask(request):
    try:
        if request.method == 'GET':
            taskName = request.GET.get('taskName', '')
            if taskName:
                tsk = AvailableTasks.objects.filter(task_name=taskName).first()
                if tsk:
                    tsk_des = TaskInfo.objects.filter(task=tsk).first()
                    if tsk_des:
                        context = {
                            'task': tsk_des
                        }
                        return render(request, 'task_description.html', context=context)

    except:
        pass
    return redirect('availableTasks')


def availableTasks(request):
    av = AvailableTasks.objects.all()
    context = {
        'av': av,
        'l_av': len(av)
    }
    return render(request, 'tasks.html', context=context)


def account(request):
    up = UserProfile.objects.filter(username=request.user).first()
    context = {
        'usr': up
    }
    if request.method == 'POST':
        amount = request.POST.get('amount', '')
        if amount:
            amt = int(amount)
            bal = UserProfile.objects.filter(username=request.user.username).first()
            bal_ = bal.balance
            if int(bal_) >= amt:
                print('allow withdraw')

    return render(request, 'account.html', context=context)


def logoutV(request):
    logout(request)
    return render(request, 'home.html')


@login_required(login_url='/login/')
def remoTask(request):
    if request.method == 'POST':
        taskName = request.POST.get('taskname', '')
        remoUsername = request.POST.get('remo_username', '')
        remoPassword = request.POST.get('remo_password', '')
        remoCountry = request.POST.get('country', '')

        tm = AvailableTasks.objects.filter(task_name=taskName).first()
        if tm:
            rm = RemoAirtmDetails(
                task=tm,
                username=remoUsername,
                password=remoPassword,
                country=remoCountry,
            )
            rm.save()
        up = UserProfile.objects.filter(username=request.user.username).first()
        up.pending += 10
        up.save()
        messages.success(request,
                         'The details were submitted successfully and are under review.\n You can continue submitting more details')
        return redirect('submitTaskRemo')
    context = {
        'tasks': AvailableTasks.objects.all()
    }

    return render(request, 'submit_remo_account.html', context=context)


def trialTemp(request):
    return render(request, 'dummy_task_desc.html')
