from django.shortcuts import render, redirect
from authentication.forms import NewUserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from authlib.integrations.django_client import OAuth

# Create your views here

def home(request):
    return render(request, 'home.html')

