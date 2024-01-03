from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
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
                paypalEmail=paypal_email,
                phoneNumber=phone_number,
                country=country,
                dialCode=dial_code,

            )
            User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            up.save()
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


@login_required(login_url='/login/')
def account(request):
    up = UserProfile.objects.filter(username=request.user).first()
    unf = UserNotifications.objects.filter(user=up).order_by('-pk')

    if request.method == 'POST':
        # withdrawal request
        amount = request.POST.get('amount', '')
        if amount:
            amt = int(amount)
            bal_ = up.balanceActual
            if int(bal_) >= amt:
                un = UserNotifications(
                    user=up,
                    message=f'You request to withdraw ${amt} has been received and is under '
                            f'review. Check this page regurlarly for updates.'
                )
                un.save()
                if len(UserNotifications.objects.filter(user=up)) > 10:
                    un = UserNotifications.objects.filter(user=up)
                    un.first().delete()

                up.withdrawPending += amt
                up.balanceActual -= amt
                up.save()
                wr = WithdrawalRequests(
                    user=up,
                    amount=amt,
                )
                wr.save()

                return redirect('account')

    for r in UserNotifications.objects.filter(user=up):
        if r.timesViewed > 0:
            r.isRead = True
            r.save()
        else:
            r.timesViewed += 1
            r.save()
    context = {
        'usr': up,
        'notf': unf,
    }

    return render(request, 'account.html', context=context)


def logoutV(request):
    global count
    count = 0
    logout(request)
    return render(request, 'home.html')


@login_required(login_url='/login/')
def remoTask(request):
    global count
    count = 0
    captcha = ReCaptchaField()
    if request.method == 'POST':
        taskName = request.POST.get('taskname', '')
        remoUsername = request.POST.get('remo_username', '')
        remoPassword = request.POST.get('remo_password', '')
        remoCountry = request.POST.get('country', '')
        up = UserProfile.objects.filter(username=request.user.username).first()

        tm = AvailableTasks.objects.filter(task_name=taskName).first()
        if tm:
            rm = RemoAirtmDetails(
                task=tm,
                tasker=up,
                username=remoUsername,
                password=remoPassword,
                country=remoCountry,
            )
            rm.save()
        # india remotask
        if 'INDIA' in taskName.upper():
            if 'REMOTASK' in taskName.upper():
                # india remotask. $50
                bal_ = 50
                pass
            else:
                # india airtm  $25
                bal_ = 25

                pass
        elif 'USA' in taskName.upper():
            # usa remotask
            if 'REMOTASK' in taskName.upper():
                # 75 $
                bal_ = 75

                pass
            else:
                # usa airtm
                # 50 $
                bal_ = 50

                pass
        else:
            # canada remotask
            if 'REMOTASK' in taskName.upper():
                # 75 usd
                bal_ = 75

                pass
            else:
                # canada airtm
                # 50 usd
                bal_ = 50

                pass

        up.balanceHold += bal_
        up.save()
        un = UserNotifications(
            user=up,
            message=f'Congratulations. We have received your task. '
                    f'We have credited {bal_} USD into your holding wallet. Once we confirm the details you have'
                    f' submitted,'
                    f' you will be able to withdraw the amount. Thank you for working with us '
                    f''
        )
        un.save()
        if len(UserNotifications.objects.filter(user=up)) > 10:
            un = UserNotifications.objects.filter(user=up)
            un.first().delete()

        messages.success(request,
                         'The details were submitted successfully and are under review. '
                         'You can continue submitting more details')
        return redirect('submitTaskRemo')
    context = {
        'tasks': AvailableTasks.objects.all(),
        'captcha': captcha
    }

    return render(request, 'submit_remo_account.html', context=context)


def trialTemp(request):
    return render(request, 'dummy_task_desc.html')


def superAdmin(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            accounts = request.POST.get('confirm_accts', '')
            w_requests = request.POST.get('approve_ids', '')
            if accounts:
                ac = accounts.split(',')
                for a in ac:
                    ram = RemoAirtmDetails.objects.filter(id=int(a)).first()
                    ram.isConfirmed = True
                    ram.save()

                    usr = ram.tasker

                    # transfer balance from hold to actual account
                    usr.balanceHold -= 10
                    usr.balanceActual += 10
                    usr.save()
                    # inform user that the details were confirmed

                    messg = (f'Your task is confirmed. We have credited $10 into your actual wallet.'
                             f' Your balance now stands at ${usr.balanceActual}')

                    unot = UserNotifications(
                        message=messg,
                        user=usr
                    )
                    unot.save()
                    if len(UserNotifications.objects.filter(user=usr)) > 20:
                        un = UserNotifications.objects.filter(user=usr)
                        un.first().delete()

            if w_requests:
                wr = w_requests.split(',')
                for w in wr:
                    _r = WithdrawalRequests.objects.filter(id=w).first()
                    usr = _r.user
                    amt = _r.amount
                    _r.isApproved = True
                    _r.save()
                    # transfer balance from hold to actual account

                    usr.withdrawPending -= amt
                    usr.withdrawSuccess += amt
                    usr.save()

                    # update user
                    messg = (
                        f'Congratulations! Your request to withdraw ${amt} was accepted and processed successfully'
                        f'. Thank you for working with us. '
                        f'If you  have any problem do not hesitate to contact us via the contact form')

                    unot = UserNotifications(
                        message=messg,
                        user=usr
                    )
                    unot.save()
                    if len(UserNotifications.objects.filter(user=usr)) > 20:
                        un = UserNotifications.objects.filter(user=usr)
                        un.first().delete()

                pass

            return redirect('superAdmin')
        context = {
            'w_reqs': WithdrawalRequests.objects.filter(isApproved=False),
            'conf': RemoAirtmDetails.objects.filter(isConfirmed=False)
        }
        return render(request, 'super_admin_page.html', context=context)
    return redirect('home')
