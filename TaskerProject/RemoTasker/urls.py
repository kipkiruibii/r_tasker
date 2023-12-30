from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginV, name='login'),
    path('register/', views.register, name='register'),
    path('about_task/', views.aboutTask, name='aboutTask'),
    path('available_tasks/', views.availableTasks, name='availableTasks'),
    path('logout/', views.logoutV, name='logout'),
    path('submit_task_remo/', views.remoTask, name='submitTaskRemo'),
    path('trial_temp/', views.trialTemp, name='trialTemp'),
]
