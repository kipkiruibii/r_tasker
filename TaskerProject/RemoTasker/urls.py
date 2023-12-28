from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('about_task/', views.aboutTask, name='aboutTask'),
    path('available_tasks/', views.availableTasks, name='availableTasks'),
]
